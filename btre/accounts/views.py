from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from listings.models import Listing

# Create your views here.
def register(request): 
  if request.method == 'POST': 
    # Register User
    # print('SUBMITTED REG')
    # messages.error(request, 'Testing error message')
    # return redirect('register')
    
    # Get form variables
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2: 
      # CHeck username
      if User.objects.filter(username=username).exists(): 
        messages.error(request, 'That username is already taken')
        return redirect('register')
      else: 
        if User.objects.filter(email=email).exists(): 
          messages.error(request, 'That email is already registered')
          return redirect('register')
        else: 
          # Looks good
          user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
          # Login after register
          # auth.login(request, user)
          # messages.success(request, 'Registration successful')
          # return redirect('index')
          user.save()
          messages.success(request, 'You are not registered and can log in')
          return redirect('login')
    else: 
      messages.error(request, 'Passwords do not match')
      return redirect('register')
    
  else: 
    return render(request, 'accounts/register.html')

def login(request): 
  if request.method == 'POST': 
    # Login User
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None: 
      # if user exists
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('dashboard')
    else: 
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else: 
    return render(request, 'accounts/login.html')

def logout(request): 
  if request.method == 'POST': 
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('index')

def dashboard(request): 
  user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

  # listings = Listing.objects.order_by('-list_date').filter(is_published=True)
  context = {
    # 'listings' : listings
    'contacts': user_contacts 
  }
  return render(request, 'accounts/dashboard.html', context)

def deleteContact(request): 
  if request.method == 'POST': 
    contactid = request.POST['contact_id']
    Contact.objects.filter(pk=contactid).delete()
    messages.success(request, 'Contact Successfully Deleted')
    return redirect('dashboard')
  else:  
    return redirect('dashboard')