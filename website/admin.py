from django.contrib import admin
from .models import Advertisement, AdLink, VisitorFingerprint, AdVisit, Appointment, Patient# Register your models here.



@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("f_name", "m_name", "l_name", "mobile", "email", "gender", "birthDate", "address")
    search_fields = ("f_name", "m_name", "l_name", "mobile", "email", "address")
    list_filter = ("gender",)
    ordering = ("f_name", "l_name")
    readonly_fields = ()
    

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "subject",
        "time",
        "status",
        "priority",
        "cancelationreason",
        "updated_by",
        "created",
        "description",
        "tests",
    )
    autocomplete_fields = ("subject",)
    list_filter = ("status", "priority", "time", "created")
    search_fields = ("subject__f_name", "subject__l_name", "description", "tests", "cancelationreason")
    ordering = ("-time",)
    readonly_fields = ("created",)



@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ("name", "platform", "is_active", "created_at", "updated_at")
    list_filter = ("platform", "is_active", "created_at")
    search_fields = ("name", "platform", "notes")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(AdLink)
class AdLinkAdmin(admin.ModelAdmin):
    list_display = ("short_code", "advertisement", "target_url", "is_active", "created_at", "updated_at")
    list_filter = ("is_active", "advertisement")
    search_fields = ("short_code", "target_url")
    ordering = ("-created_at",)
    readonly_fields = ("short_code", "created_at", "updated_at")
    autocomplete_fields = ("advertisement",)


@admin.register(VisitorFingerprint)
class VisitorFingerprintAdmin(admin.ModelAdmin):
    list_display = ("fingerprint_hash", "hashed_ip", "created_at")
    search_fields = ("fingerprint_hash", "hashed_ip", "user_agent")
    readonly_fields = ("hashed_ip", "user_agent", "accept_headers", "fingerprint_hash", "created_at")
    ordering = ("-created_at",)


@admin.register(AdVisit)
class AdVisitAdmin(admin.ModelAdmin):
    list_display = (
        "ad_link",
        "timestamp",
        "browser",
        "os",
        "device_type",
        "hashed_ip",
        "referrer",
    )
    list_filter = ("device_type", "browser", "os", "timestamp")
    search_fields = ("ad_link__short_code", "hashed_ip", "referrer", "user_agent")
    readonly_fields = (
        "ad_link",
        "visitor_fingerprint",
        "hashed_ip",
        "user_agent",
        "browser",
        "os",
        "device_type",
        "referrer",
        "timestamp",
        "geo_info",
    )
    ordering = ("-timestamp",)
    autocomplete_fields = ("ad_link", "visitor_fingerprint")