from django.shortcuts import render, redirect

from django.core.files.base import ContentFile


from .forms import *


from .models import *
from users.models import *
# Create your views here.
def home(request):
    s = Service.objects.all()
    serv = {'serv':s} 
    return render(request,'services\home.html',serv)

def providers_list(request, pk):
    service = Service.objects.get(pk=pk)
    providers = Profile.objects.filter(is_craftsman=True).filter(service=service)
    return render(request, 'services/providers_list.html', {'providers': providers})


def about_us(request):
    return render(request, 'services/about_us.html')

def contact_us(request):
    return render(request, 'services/contact_us.html')

# def login(request):
#     pass

# def settings(request):
#     pass

# def profile(request):
#     pass


# def rate(request, providerid):
#     provider = Provider.objects.get(provider_id=providerid)

#     customer = request.customer

#     if request.method == 'POST':
#         form = RateForm(request.POST)
#         if form.is_valid():
#             rat = form.save(commit=False)
#             rat.customer = customer
#             rat.provider = provider
#             rat.save()
#             return HttpResponseRedirect(reverse(''),args=[providerid])
#     else :
#         form = RateForm()
#     template = loader.get_template()
#     context = {
#         'form':form,
#         'provider':provider,
#     }

#     return HttpResponse(template.render(context,request))