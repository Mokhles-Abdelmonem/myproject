from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.core.mail import send_mail
import uuid



# Create your views here.
@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html', {})

def welcome(request):
    return render(request, 'welcome.html', {})

def register(request):
    form = Register()
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is taken.')
                return redirect('/register/')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/register/')
            form = Register(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                user_obj = User.objects.get(username = user)

                print(user_obj)
                profile_obj = Profile.objects.create(
                    user = user_obj,
                    first_name=user_obj.first_name,
                    last_name =user_obj.last_name,
                    email_address = user_obj.email,
                    )
                profile_obj.save()
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
            messages.success(request, '''
            Email or password is not vallid ,
            Username: Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only, 
            Password: Your password can’t be too similar to your other personal information, 
                    Your password must contain at least 8 characters, 
                    Your password can’t be a commonly used password, 
                    Your password can’t be entirely numeric.
            ''')
            return redirect('/register/')      
        except Exception as e:
            print(e)
    except Exception as e:
            print(e)

    context = {'form':form}
    return render(request, 'register.html', context)

def user_login(request):
    if request.method == 'POST':
        form = Login()
        username = request.POST['username']
        password = request.POST['password']
        user_obj = User.objects.filter(username = username).first()
        nameuser = User.objects.filter(email=username.lower()).first()           #login with email
        if nameuser is None :
            if user_obj is None :
                messages.success(request, 'User not found.')
                return redirect('/login/')
            nameuser = user_obj
        user = authenticate(request, username=nameuser, password=password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('login')
        login(request, user)
        return redirect('home')

    else:
        form = Login()

    return render(request, 'login.html',{
        'form':form
    })

def Logout(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def settings(request):
    user_form = UpdateUserForm(instance=request.user)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        email = request.POST.get('email')
        if User.objects.filter(email = email).first():
            messages.success(request, 'Email is taken.')
            return redirect('/settings/')
        if user_form.is_valid():
            user_form.save()
            user_pass = User.objects.get(username=request.user.username)
            user_pass.set_password(request.POST['password'])
            user_pass.save()
            messages.success(request, 'profile settings successfully updated ')
            return redirect('home')

    return render(request, 'settings.html',{
        'user_form':user_form,
    })

def changepassword(request , token):
    context = {}
    try:
        profile_obj = Profile.objects.filter(forget_password_token = token).first()
        context = {'user_id' : profile_obj.user.id}
        
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')
            
            if user_id is  None:
                messages.success(request, 'No user id found.')
                return redirect(f'/changepassword/{token}/')
                
            if  new_password != confirm_password:
                messages.success(request, 'both should  be equal.')
                return redirect(f'/changepassword/{token}/')
                         
            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('login')
        
    except Exception as e:
        print(e)
    return render(request , 'changepassword.html' , context)

def sendingmail(request):
    form = SendingMail()
    try:
        if request.method == 'POST':
            email = request.POST['email']
            user_name = User.objects.get(email=email)
            if user_name is None:
                messages.success(request, 'email Not found')
                return redirect('sendingmail')
            profile_obj= Profile.objects.get(user = user_name)
            token = str(uuid.uuid4())
            profile_obj.forget_password_token = token
            profile_obj.save()
            subject = " reset password "
            message = f'Hi , click on the link to reset your password http://127.0.0.1:8000/changepassword/{token}/'
            from_email = 'djangooprojects@gmail.com'
            send_mail(subject, message, from_email, [email])
            messages.success(request, 'An email was sent check out your email.')
            return redirect('sendingmail')


    except Exception as e:
        print(e)
    return render(request, 'sendingmail.html',{
        'form':form,
        })

@login_required(login_url='/login/')
def search_profile(request):
	if request.method == "POST":
		searched = request.POST['searched']
		profile = Profile.objects.filter(first_name__contains=searched)
	
		return render(request, 
		'search_profile.html', 
		{'searched':searched,
		'profile':profile})
	else:
		return render(request, 
		'search_profile.html', 
		{})