from django.shortcuts import render, render_to_response, redirect
from django.contrib.localflavor.us.us_states import STATE_CHOICES
from cart.models import Cart, CartItem
import hashlib
import forms
import models

def signup(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            account = form.instance
            account.password = _md5_encode(account.password)           
            account.save()
            Cart(account=account).save()
            request.session['account'] = account
            request.session['cart'] = []
            return redirect('/profile')
        else:           
            return render_to_response('test_signup.html', { 'error_message':form.errors.items, 'state_choice':STATE_CHOICES })
    else:
        return render_to_response('test_signup.html', {'state_choice':STATE_CHOICES})
    
def login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        error = 0
        if form.is_valid():
            cleaned_data = form.cleaned_data
            try:
                account = models.Account.objects.get(email=cleaned_data['email'])
                if account and account.password == _md5_encode(cleaned_data['password']):
                    request.session['account'] = account
                    request.session['cart'] = CartItem.objects.filter(cart=account.cart)
                    return redirect('/profile') 
                else:
                    error = 2
            except:
                print 'error'
                error = 1               
        return render_to_response('test_login.html', { 'error':error, 'error_message':form.errors.items })
    else:
        return render_to_response('test_login.html')
    
def logout(request):
    try:
        del request.session['account']
        del request.session['cart']
    except KeyError:
        pass
    return redirect('/login')

def profile(request):
    if request.session.get('account'):
        return render(request, 'test_profile.html', { 'state_choice':STATE_CHOICES })
    else:
        return redirect('/login')

def update_profile(request):
    if request.method == 'POST':
        error = 0
        try:
            account = models.Account.objects.get(id=request.session['account'].id)
            account.address = request.POST.get('address', '')
            account.city = request.POST.get('city', '')
            account.phone = request.POST.get('phone', '')
            account.state = request.POST.get('state', '')
            account.zip = request.POST.get('zip', '')
            account.save()
            request.session['account'] = account
            return redirect('/profile')
        except:
            raise
            error = 1
            del request.session['account']
    return redirect('/profile', { 'error':error })

def set_password(request):
    if request.method == 'POST':
        error = 0
        try:
            account = models.Account.objects.get(id=request.session['account'].id)
            new_password = request.POST.get('new_password', '')
            if _md5_encode(request.POST.get('old_password', '')) != account.password:
                error = 1
            elif new_password != request.POST.get('new_password', ''):
                error = 2
            else:
                account.password = _md5_encode(new_password)
                account.save()
                request.session['account'] = account
        except:
            error = 3
            del request.session['account']
    return redirect('/profile', { 'error':error })
    
def _md5_encode(text):
    return hashlib.new("md5", text).hexdigest()