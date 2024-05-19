from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .forms import *
# Create your views here.

def booking_user(request, pk):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form0 = form.save(commit=False)
            customer = request.user
            provider = User.objects.get(pk=pk)
            service = provider.profile.service
            city = customer.profile.city
            home_address = customer.profile.home_address
            phone = customer.profile.phone

            booking = Booking(customer=customer, provider=provider,
                              service=service, status="pending",
                              city=city, home_address=home_address,
                              phone=phone, date=form0.date,
                              time=form0.time)
            booking.save()
            messages.success(request,"Your booking request is sent. Please wait a few minutes.")
            return redirect('my_orders')
    else:
        form = BookingForm()
    return render(request, 'users/booking_user.html',{'form':form})

def edit_booking(request, pk):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form0 = form.save(commit=False)
            booking = Booking.objects.get(pk=pk)
            booking.date = form0.date
            booking.time = form0.time
            booking.status = "pending"
            booking.save()
            messages.success(request,"Your booking request is updated.")
            return redirect('my_orders')
    else:
        form = BookingForm()
    return render(request, 'users/booking_user.html',{'form':form})


def my_orders(request):
    bookings = Booking.objects.filter(customer=request.user)
    return render(request, 'users/my_orders.html', 
                  {'bookings': bookings})
def my_orders_pending(request):
    bookings = Booking.objects.filter(customer=request.user)
    pending = bookings.filter(status="pending")
    return render(request, 'users/my_orders_pending.html', 
                  {'pending': pending})
def my_orders_confirmed(request):
    bookings = Booking.objects.filter(customer=request.user)
    confirmed = bookings.filter(status="confirmed")
    return render(request, 'users/my_orders_confirmed.html',
                   {'confirmed': confirmed})
def my_orders_completed(request):
    bookings = Booking.objects.filter(customer=request.user)
    completed = bookings.filter(status="completed")
    return render(request, 'users/my_orders_completed.html', 
                  {'completed': completed})


def my_schedule(request):
    bookings = Booking.objects.filter(provider=request.user)
    return render(request, 'users/my_schedule.html', {'bookings': bookings})

def my_schedule_pending(request):
    bookings = Booking.objects.filter(provider=request.user)
    pending = bookings.filter(status="pending")
    return render(request, 'users/my_schedule_pending.html',
                   {'pending': pending})

def my_schedule_confirmed(request):
    bookings = Booking.objects.filter(provider=request.user)
    confirmed = bookings.filter(status="confirmed")
    return render(request, 'users/my_schedule_confirmed.html',
                   {'confirmed': confirmed})

def my_schedule_completed(request):
    bookings = Booking.objects.filter(provider=request.user)
    completed = bookings.filter(status="completed")
    return render(request, 'users/my_schedule_completed.html',
                   {'completed': completed})



def appointment_details_cust(request, pk):
    booking = Booking.objects.get(pk=pk)
    return render(request, 'users/appointment_details_cust.html', {'booking':booking})
    
def appointment_details_prov(request, pk):
    booking = Booking.objects.get(pk=pk)
    return render(request, 'users/appointment_details_prov.html', {'booking':booking})
    



def delete_order(request, pk):
    booking = Booking.objects.get(pk=pk)
    booking.delete()
    messages.success(request, "The Order is deleted!")
    return redirect('my_orders')


def delete_appointment(request, pk):
    booking = Booking.objects.get(pk=pk)
    booking.delete()
    messages.success(request, "The Appointment is deleted!")
    return redirect('my_schedule')

def confirm_appointment(request, pk):
    booking = Booking.objects.get(pk=pk)
    booking.status = "confirmed"
    booking.save()
    messages.success(request, "The appointment is confirmed successfuly")
    return redirect('my_schedule_confirmed')
    
def complete_appointment(request, pk):
    booking = Booking.objects.get(pk=pk)
    booking.status = "completed"
    booking.save()
    messages.success(request, "The appointment is completed successfuly")
    return redirect('my_schedule_completed')
    
