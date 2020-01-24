from django.shortcuts import render, redirect
from .models import Gym
from .forms import GymCreate
from django.http import HttpResponse
import os
from django.conf import settings
from django.http import HttpResponse, Http404

from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist


from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from gymapp.models import Gym, Trainer, Members, abc, Payment
from django.contrib.auth.models import Permission,User
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from .forms import TrainerForm,AbcForm,MemberForm,PaymentForm
from .models import  Trainer


def index(request):
    shelf = Gym.objects.all()
    return render(request, 'gymapp/premium.htm', {'shelf': shelf})

    
def upload(request):
    upload = GymCreate()
    if request.method == 'POST':
        upload = GymCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'gymapp/upload_form.htm', {'upload_form':upload})


             
def update_form(request, gym_id):
    gym_id = int(gym_id)
    try:
        values = Gym.objects.get(id = gym_id)
    except Gym.DoesNotExist:
        return redirect('index')
    gym_form = GymCreate(request.POST or None, instance = values)
    if gym_form.is_valid():
       gym_form.save()
       return redirect('index')
    return render(request, 'gymapp/upload_form.htm', {'upload_form':gym_form})




def delete_form(request, gym_id):
    gym_id = int(gym_id)
    try:
        values = Gym.objects.get(id = gym_id)
    except Gym.DoesNotExist:
        return redirect('index')
    values.delete()
    return redirect('index')

"""
Search Functionality

"""

def search_function_hai(request):
    if request.method =='GET':
        finds = request.GET['hacsac']
        if finds:
            match = Gym.objects.filter(Q(workoutname__icontains=finds))                             
            if match:                
                return render(request,'gymapp/upload_form.htm', {'sac':match})
            else:
                messages.error(request, "The word, You type did  not Exist")
        else:
            return HttpResponseRedict('gymapp/upload_form.htm')  
    return render(request, 'gymapp/upload_form.htm')         


def view_register_users(request):
    if request.method =="GET":
        return render(request,'Registration/signup.htm')
    else:
        user = User.objects.create_user(username=request.POST['username'],password=request.POST['password'],email=request.POST['email'])
        user.save()
        return redirect('/')


def view_authenticate_users(request):
    if request.method =="GET":
        return render (request,'Login/login.htm')
    else:
        print(request.POST)
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            login(request, user)
            return render(request,"additionalhtml/access.htm")
        else:
            return render(request,'Login/home.htm')

def logout(request):
    auth.logout(request)   
    return render(request,'login/login.htm')

def view_accesspage_by_authorized_user(request):
    if request.user.is_authenticated:
        return render(request, "additionalhtml/access.htm")
    else:
        return HttpResponse("Error, Please Register First!!!")




def contact(request):
    return render(request,'gymapp/contact.htm')      

def home(request):
  return render(request,'login/home.htm')

def course(request):
    return render(request,'gymapp/course.htm')

def singuppage(request):
    return render(request,'registration/signup.htm')

def accesspage(request):
    return render(request,'additionalhtml/access.htm')

def schedulepage(request):
    return render(request,'gymapp/schedule.htm')

def trainderdet(request):
    return render(request,'gymapp/trainerdet.htm')

def trainer_create_form(request):
    form = TrainerForm(request.POST)
    if form.is_valid():
        form.save()

    context ={
        'form':form
    }    
    return render(request, 'gymapp/trainer.htm', context)

def abc_create_form(request):
    form1 = AbcForm(request.POST)
    if form1.is_valid():
        form1.save()

    context={
        'form1':form1
    }
    return render(request,'gymapp/abc.htm',context)

def members_create_form(request):
    form2 = MemberForm(request.POST)
    if form2.is_valid():
        form2.save()

    context={
        'form2':form2
    }
    return render(request,'gymapp/members.htm',context)
    
def Payment_create_form(request):
    form3 = PaymentForm(request.POST)
    if form3.is_valid():
        form3.save()
    context={
        'form3':form3
    }
    return render(request,'gymapp/payment.htm',context)

