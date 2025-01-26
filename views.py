from django.shortcuts import render, redirect
from .models import User


# Create your views here.
def add_cust_page(request):
    return render(request,'Atemplate/add_cust.html')


def add_cust_func(request):
    if request.method == 'POST':

        full_name = request.POST["full_name"]
        address = request.POST["address"]
        gender = request.POST["gender"]
        mob_no = request.POST["mob_no"]
        email_id = request.POST["email_id"]

        data = User(full_name=full_name, address=address, gender=gender, mob_no=mob_no, email_id=email_id)
        data.save()
        return render(request, 'dashboard.html')
    return redirect('/add_cust_page')

def dashboard(request):
    return render(request,'dashboard.html')
