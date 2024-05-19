from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import *
from bookings.models import *

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegiterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegiterForm()

    return render(request, 'users/register.html', {'form':form})    

def UserLoggedIn(request):
    if request.user.is_authenticated == True:
        username = request.user.username
    else:
        username = None
    return username

def logout_view(request):
    username = UserLoggedIn(request)
    if username != None:
        logout(request)
        return redirect('home')

def add_to_favourite(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if profile.users_favourite.filter(pk=request.user.pk).exists():
        profile.users_favourite.remove(request.user)
    else:
        profile.users_favourite.add(request.user)
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
        
def favourite_list(request):
    profiles = Profile.objects.filter(users_favourite=request.user)
    return render(request, 'users/favourite_list.html', {'favourites':profiles})


@login_required 
def edit_work_info(request):
    if request.method == 'POST':
        #u_form = UserUpdateForm(request.POST, instance=request.user)
        w_form = WorkUpdateForm(request.POST, instance=request.user.profile)
        if w_form.is_valid():
            #u_form.save()
            w_form.save()
            
            messages.success(request, f'Your Work Info has been updated!')
            
            return redirect('profile')
    else:
        #u_form = UserUpdateForm(instance=request.user)
        w_form = WorkUpdateForm(instance=request.user.profile)
    context = {
        #'u_form':u_form,
        'w_form':w_form
    }
    return render(request, 'users/edit_work_info.html', context)

@login_required  
def edit_profile(request):
    if request.method == 'POST':
        #u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            #u_form.save()
            p_form.save()
            
            messages.success(request, f'Your account has been updated!')
            
            if request.user.profile.is_craftsman :
                return redirect('edit_work_info')
            return redirect('profile')
    else:
        #u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        #'u_form':u_form,
        'p_form':p_form
    }
    
    return render(request, 'users/edit_profile.html', context)

def profile(request, pk=None):
    # if request.user.profile.is_craftsman :
    #     messages.success(request, "Welcome to this application, starting your job here!")
    if pk:
        user = get_object_or_404(User, pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'users/profile.html', args)


def settings(request):
    return render(request, 'users/settings.html')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # To keep the user logged in
            return redirect('password_change_done')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/password_change.html', {'form': form})

def password_change_done(request):
    return render(request, 'users/password_change_done.html')

@login_required
def change_email(request):
    if request.method == 'POST':
        form = ChangeEmailForm(request.POST)
        if form.is_valid():
            new_email = form.cleaned_data['new_email']
            current_password = form.cleaned_data['current_password']
            
            user = request.user
            if user.check_password(current_password):
                user.email = new_email
                user.save()
                messages.success(request, 'Email changed successfully.')
                return redirect('profile')  # Redirect to profile page or any other page
            else:
                messages.error(request, 'Incorrect current password.')
    else:
        form = ChangeEmailForm()
    return render(request, 'users/change_email.html', {'form': form})

 
@login_required
def delete_account(request):
    if request.method == 'POST':
        form = DeleteAccountForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = request.user
            if user.check_password(password) and user.email == email:
                # user.profile.delete()
                user.delete()
                messages.success(request, 'Account deleted successfully.')
                return redirect('home')  # Redirect to profile page or any other page
            else:
                messages.error(request, 'Incorrect current password or email.')
    else:
        form = DeleteAccountForm()
    return render(request, 'users/delete_account.html', {'form': form})

        