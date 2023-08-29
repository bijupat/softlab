from django.shortcuts import render


# Create your views here.
def index(request):
    
    return render(request, 'website/index.html')

def get_price(request):
    if request.method == "POST":
        pass
        
    return render(request, 'website/get_price.html')


