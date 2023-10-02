from django.shortcuts import render 
from restaurant.models import AboutModel, Personal, Service, Menu, Contact
from restaurant.forms import ContactForm, ReserveForm

def home_view(request):
    about = AboutModel.objects.first()
    workers = Personal.objects.order_by("-created_at")[:4]
    context = {
        "index_about": about,
        "index_workers": workers,
    }
    return render(request, "index.html", context)


def about_view(request):
    about = AboutModel.objects.first()
    context = {
        "about":about
    }
    return render(request, "about.html", context)


def service_view(request):
    services = Service.objects.order_by("-created_at")
    context = {
        "services":services,
    }
    return render(request, "service.html", context)


def menu_view(request):
    foods = Menu.objects.order_by("-created_at").filter(category__name='Popular Breakfast')
    context = {
        "foods": foods,
    }
    return render(request, "menu.html", context)

def ours_team(request):
    workers = Personal.objects.all()
    context = {
        "workers":workers
    }
    return render(request,"team.html", context)

def contact_view(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
        
    name_surname = request.POST.get("ad")
    email = request.POST.get("epoct")
    subject = request.POST.get("movzu")
    message = request.POST.get("mesaj")
    obj = Contact.objects.create(
        name_and_surname=name_surname,
        email=email,
        subject=subject,
        message=message,
    )
    obj.save()
    contex ={
       " form": form,
    }
    return render(request, "contact.html",contex)

def booking_view(request):
    form = ReserveForm()
    context ={
        "form":form,
    }
    return render(request, "booking.html",context)

def our_team(request):
    contex ={}
    return render(request, "team.html",contex)



