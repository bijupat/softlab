from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
#from django.views.decorators.csrf import csrf_exempt
import csv, requests, os, json,time,io, user_agents
#import os
from django.template.defaulttags import register
from django.template.loader import get_template
from xhtml2pdf import pisa
from django_xhtml2pdf.utils import pdf_decorator
from .forms import  PatientRegistration
from .models import Patient, Appointment, Advertisement, AdLink, AdVisit, VisitorFingerprint, WebsiteVisitor
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, FileResponse, JsonResponse, HttpResponseForbidden
from django.urls import reverse
from django.utils.timezone import now
from django.db.models import Count, Q
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from .utils import generate_fingerprint, hash_ip, create_qr_code, get_client_ip
import base64
from user_agents import parse


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def is_admin(user):
    return user.is_staff or user.is_superuser


@user_passes_test(is_admin)
def AdvertisementListView(request):
    ads = Advertisement.objects.all().order_by("-created_at")
    return render(request, "website/advertisement_list.html", {"ads": ads})


@user_passes_test(is_admin)
@require_http_methods(["GET", "POST"])
def AdvertisementCreateView(request):
    if request.method == "POST":
        name = request.POST.get("name")
        platform = request.POST.get("platform")
        notes = request.POST.get("notes")
        is_active = bool(request.POST.get("is_active"))
        Advertisement.objects.create(name=name, platform=platform, notes=notes, is_active=is_active)
        return redirect("website:advertisement_list")
    return render(request, "website/advertisement_create.html")


@user_passes_test(is_admin)
@require_http_methods(["GET", "POST"])
def AdLinkCreateView(request, ad_id):
    ad = get_object_or_404(Advertisement, pk=ad_id)
    if request.method == "POST":
        target_url = request.POST.get("target_url")
        is_active = bool(request.POST.get("is_active"))
        link = AdLink.objects.create(advertisement=ad, target_url=target_url, is_active=is_active)
        # Return partial for HTMX refresh (example)
        return render(request, "website/links_table.html", {"ad": ad,"links": ad.links.all()})
    else:
        # target_url = f"https://mahidiagnostics.in/ad/r/{ad.short_code}"
        # link = AdLink.objects.create(advertisement=ad, target_url=target_url, is_active=True)
        return render(request, "website/adlink_create_form.html", {"ad": ad, "links": ad.links.all()})


@user_passes_test(is_admin)
def QRCodeView(request, link_id):
    link = get_object_or_404(AdLink, pk=link_id)
    url = request.build_absolute_uri(reverse("website:redirect_tracking", args=[link.short_code]))
    qr_content = create_qr_code(url)
    qr_b64 = base64.b64encode(qr_content.read()).decode('utf-8')
    if request.GET.get("download") == "1":
        response = HttpResponse(qr_content, content_type="image/png")
        response["Content-Disposition"] = f'attachment; filename="qr_{link.short_code}.png"'
        return response
    return render(request, "website/qr_code.html", {"qr_image": qr_b64, "link": link, "url": url})


@require_http_methods(["GET"])
def RedirectTrackingView(request, code):
    start_time = time.monotonic()
    link = get_object_or_404(AdLink, short_code=code, is_active=True)

    ip = get_client_ip(request)
    user_agent_str = request.META.get("HTTP_USER_AGENT", "")
    accept_headers = request.META.get("HTTP_ACCEPT", "")
    fingerprint_hash = generate_fingerprint(ip, user_agent_str, accept_headers)

    fingerprint, created = VisitorFingerprint.objects.get_or_create(
        fingerprint_hash=fingerprint_hash,
        defaults={"hashed_ip": hash_ip(ip), "user_agent": user_agent_str, "accept_headers": accept_headers},
    )

    ua = user_agents.parse(user_agent_str)
    device_type = "mobile" if ua.is_mobile else "tablet" if ua.is_tablet else "desktop"
    browser = ua.browser.family
    os = ua.os.family
    referrer = request.META.get("HTTP_REFERER", "")

    AdVisit.objects.create(
        ad_link=link,
        visitor_fingerprint=fingerprint,
        hashed_ip=hash_ip(ip),
        user_agent=user_agent_str,
        browser=browser,
        os=os,
        device_type=device_type,
        referrer=referrer,
        timestamp=now(),
    )

    # Redirect fast, non-blocking (no expensive ops here)
    elapsed = time.monotonic() - start_time
    # Could log if needed for slow requests
    return redirect('website:index')

@user_passes_test(is_admin)
def AnalyticsDashboardView(request):
    ads = Advertisement.objects.filter(is_active=True).order_by("-created_at")
    ad_id = request.GET.get("ad")
    print(ads)
    ad = None
    visits = AdVisit.objects.none()
    stats = {}

    if ad_id:
        ad = get_object_or_404(Advertisement, pk=ad_id)
        visits = AdVisit.objects.filter(ad_link__advertisement=ad)
        total_clicks = visits.count()
        unique_visitors = visits.values("visitor_fingerprint").distinct().count()
        repeat_visitors = total_clicks - unique_visitors

        # Aggregated stats for charts and tables
        clicks_per_link = (
            visits.values("ad_link__short_code")
            .annotate(clicks=Count("id"))
            .order_by("-clicks")
        )
        device_breakdown = (
            visits.values("device_type").annotate(count=Count("id")).order_by("-count")
        )
        browser_breakdown = (
            visits.values("browser").annotate(count=Count("id")).order_by("-count")
        )
        os_breakdown = visits.values("os").annotate(count=Count("id")).order_by("-count")
        top_referrers = (
            visits.values("referrer")
            .exclude(referrer__exact="")
            .annotate(count=Count("id"))
            .order_by("-count")[:10]
        )

        stats = {
            "total_clicks": total_clicks,
            "unique_visitors": unique_visitors,
            "repeat_visitors": repeat_visitors,
            "clicks_per_link": clicks_per_link,
            "device_breakdown": device_breakdown,
            "browser_breakdown": browser_breakdown,
            "os_breakdown": os_breakdown,
            "top_referrers": top_referrers,
        }

    return render(
        request,
        "website/analytics.html",
        {"ads": ads, "selected_ad": ad, "stats": stats},
    )


# Helper function to get client IP (works behind proxies if configured)
def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0].strip()
    else:
        ip = request.META.get("REMOTE_ADDR", "")
    return ip





#register filter for template
@register.filter(name='split')
def split(value, key): 
    value.split("key")
    return value.split(key)



@pdf_decorator(pdfname='Mahi Pricelist.pdf')
def pricelistview(request):
    if request.method == "POST":
        pass    
    context = []
    with open(os.path.join(BASE_DIR,'pricelist.csv')) as file:
        reader = csv.DictReader(file)
        for row in reader:
            context.append(row)
    return render(request, 'website/pricelist.html', {'context' : context})


def profilespreview(request):
    context = []
    with open(os.path.join(BASE_DIR,'profiles.csv')) as file:
        reader = csv.DictReader(file)
        for row in reader:
            context.append(row)
    template_path = 'website/profileview.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf') 


    # if dawnload 
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if display 
    response['Content-Disposition'] = f'filename="Mahi Diagnostics Profiles.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render({'context': context})

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
# Create your views here.
def index(request):
    ip = get_client_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT', '')

    # Log visitor
    WebsiteVisitor.objects.create(ip_address=ip, user_agent=user_agent)

    visitor_count = WebsiteVisitor.objects.count()
    return render(request, 'website/index.html' , {"visitor_count": visitor_count})



def visitors_list_view(request):
    visitors = WebsiteVisitor.objects.order_by('-visit_time')[:100]
    detailed_visitors = []
    for v in visitors:
        ua = parse(v.user_agent or "")
        detailed_visitors.append({
            "ip_address": v.ip_address,
            "user_agent": v.user_agent,
            "visit_time": v.visit_time,
            "browser": f"{ua.browser.family} {ua.browser.version_string}",
            "os": f"{ua.os.family} {ua.os.version_string}",
            "device": f"{ua.device.family} ({'Mobile' if ua.is_mobile else 'Tablet' if ua.is_tablet else 'PC' if ua.is_pc else 'Other'})",
            "is_bot": ua.is_bot,
        })
    return render(request, "website/visitors_list.html", {"visitors": detailed_visitors})


#@csrf_exempt
def get_price(request):
    if request.method == "POST":
        pass    
    context = []
    with open(os.path.join(BASE_DIR,'pricelist.csv')) as file:
        reader = csv.DictReader(file)
        for row in reader:
            context.append(row)
    return render(request, 'website/get_price.html', {'context' : context})


#@pdf_decorator(pdfname='new_filename.pdf')
def profiles(request):
    if request.method == "POST":
        pass 
    context = []
    with open(os.path.join(BASE_DIR,'profiles.csv')) as file:
        reader = csv.DictReader(file)
        for row in reader:
            context.append(row)
    return render(request, 'website/profiles.html', {'context' : context})

def book_visit(request):
    if request.method == "POST":
        form = PatientRegistration(request.POST)
        if form.is_valid():
            fname = form.cleaned_data["f_name"].title()
            mname = form.cleaned_data["m_name"].title()
            lname = form.cleaned_data["l_name"].title()
            gender = form.cleaned_data["gender"]
            birth_date = form.cleaned_data["birth_date"]
            mobile = form.cleaned_data["mobile"]
            email = form.cleaned_data["email"].lower()
            visit_time = form.cleaned_data["visit_time"]
            tests = form.cleaned_data["tests"].title()
            address = form.cleaned_data["address"].title()
            new_patient = Patient(f_name = fname, m_name = mname, l_name = lname, mobile = mobile, email = email, gender = gender,  birthDate = birth_date , address = address )
            new_patient.save()
            new_appointment = Appointment(time = visit_time, subject = new_patient, tests = tests )
            new_appointment.save()
            SMSText = f"Respected {fname} {lname}, Your Appointment on {visit_time} for blood tests {tests} is booked. Address: {address} Call 7016944046 if any query MEDI LAB"
            #SMSText = f"Patient Name: {fname} {lname} Ref No: {visit_time} Reports is: {tests} Call: {mobile} For Any Query Contact,MEDILAB DIAGNOSTIC"
            url_pat = f"https://onlysms.co.in/api/sms.aspx?UserID=MediLB&UserPass=Gurudev@101&MobileNo=91{mobile}&GSMID=MEDIDC&PEID=1301161848129500767&Message={SMSText}&UNICODE=TEXT"            
            url_lab = f"https://onlysms.co.in/api/sms.aspx?UserID=MediLB&UserPass=Gurudev@101&MobileNo=919909016867&GSMID=MEDIDC&PEID=1301161848129500767&Message={SMSText}&UNICODE=TEXT"            
            print(SMSText)
            print(url_lab)
            responce = requests.get(url_lab) 
            print(responce.status_code)
            print(responce.text)
            return render(request, 'website/thankyou.html',{"patient": form.cleaned_data,})
        # if form is not valid
        else:
            return render(request, 'website/book_visit.html', {"form": form, "message":form.errors })   
    # if request method get
    return render(request, 'website/book_visit.html',{ "form": PatientRegistration, })

@login_required(login_url='/lab/login/')
def manage_visit(request):
    if request.method == "POST":
        pass
    
    appointments  = Appointment.objects.all()
    return render(request, 'website/view_visit.html',{"appointments": appointments})

def contactus(request):
    if request.method == "POST":
        pass
    
    return render(request, 'website/contactus.html')

def aboutus(request):
    if request.method == "POST":
        pass

    return render(request, 'website/aboutus.html')

def privacy(request):
    if request.method == "POST":
        pass

    return render(request, 'website/privacy.html')

def camp(request):
    if request.method == "POST":
        pass

    return render(request, 'website/camp.html')

def termsconditions(request):
    if request.method == "POST":
        pass

    return render(request, 'website/termsconditions.html')
