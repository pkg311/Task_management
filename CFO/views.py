from email import message
from unicodedata import category
from django.shortcuts import render, redirect
from CFO.models import TaskMaster, COEMaster, UserMaster, RecurrenceMaster
import math
from django.contrib.auth.models import User

from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse

from django.conf import settings
import base64


def login1(request):
    return render(request, 'login.html')


def Register(request):
    coe = COEMaster.objects.all()
    context = {
        'coe': coe
    }
    return render(request, 'register.html', context)


def Reg(request):
    if request.method == "POST":
        Uname = request.POST.get('Uname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        C_password = request.POST.get('confirm-password')
        Utype = request.POST.get('User_Type')
        CID = request.POST.get('Division')
        if password == C_password:
            user = UserMaster(
                Uname=Uname,
                email=email,
                password=password,
                Utype=Utype,
                CID=CID
            )
            user.save()
            return redirect('login1')
        else:
            msg = "Password and Confirm Password not Matched"
            return render(request, 'register1.html', msg)
    return redirect('login1')


def logout(request):
    try:
        del request.session['email']
    except KeyError:
        pass
    return redirect('login1')


def log(request):
    if request.method == "POST":
        email = request.POST['email']
        pwd = request.POST['password']
        # Utype=request.POST['Utype']
        val = UserMaster.objects.filter(email=email, password=pwd).count()
        if val == 1:
            request.session['Email'] = email
            print(request.session['Email'])
        else:
            return redirect('login1')

    if 'Email' in request.session:
        queryset = UserMaster.objects.filter(email=request.session['Email']).values('Utype')

        Task = TaskMaster.objects.all()

        ## user
        if queryset[0]['Utype'] == "Employee":
            
            queryset1 = UserMaster.objects.filter(email=request.session['Email']).values('Uname')
            user=queryset1[0]['Uname']
            Task = TaskMaster.objects.filter(UID=queryset1[0]['Uname'])
            T1 = TaskMaster.objects.filter(UID=queryset1[0]['Uname']).count()
            if T1==0:
                PT=0
                PPT=0
                CT=0
                PCT=0
                OT=0
                OPT=0
            else:
                PT = TaskMaster.objects.filter(UID=queryset1[0]['Uname'], status='Pending').count()
                PPT = round(((PT / T1) * 100), 0)
                CT = TaskMaster.objects.filter(UID=queryset1[0]['Uname'], status='Completed').count()
                PCT = round(((CT / T1) * 100), 0)
                OT = TaskMaster.objects.filter(UID=queryset1[0]['Uname'], status='InProgress').count()
                OPT = round(((OT / T1) * 100), 0)

            context1 = {
                'Task': Task,
                'T1': T1,
                'CT': CT,
                'PT': PT,
                'PCT': PCT,
                'PPT': PPT,
                'OPT': OPT,
                'OT': OT,
                'user': user

            }
            return render(request, 'dashuser.html', context1)
        ## COE_Lead
        elif queryset[0]['Utype'] == "COE Leads":
            
            queryset1 = UserMaster.objects.filter(email=request.session['Email']).values('CID')
            Task = TaskMaster.objects.filter(CID=queryset1[0]['CID'])
            T1 = TaskMaster.objects.filter(CID=queryset1[0]['CID']).count()
            PT = TaskMaster.objects.filter(CID=queryset1[0]['CID'], status='Pending').count()
            PPT = round(((PT / T1) * 100), 0)
            CT = TaskMaster.objects.filter(UID=queryset1[0]['CID'], status='Completed').count()
            PCT = round(((CT / T1) * 100), 0)
            OT = TaskMaster.objects.filter(UID=queryset1[0]['CID'], status='InProgress').count()
            OPT = round(((OT / T1) * 100), 0)
            queryset2 = UserMaster.objects.filter(email=request.session['Email']).values('Uname')
            user=queryset2[0]['Uname']

            context1 = {
                'Task': Task,
                'T1': T1,
                'CT': CT,
                'PT': PT,
                'PCT': PCT,
                'PPT': PPT,
                'OPT': OPT,
                'OT': OT,
                'user':user
                
            }
            print("Coe_lead")
            return render(request, 'dashcoe.html', context1)
        ##COE_HEAD
        elif queryset[0]['Utype'] == "COE Head":
            return render(request, 'dashuser.html', )
        else:
            return redirect('login1')

    else:
        return redirect('Logout_process')


def home(request):
    if request.session:
        return redirect('Login_process')
    else:
        return render(request, 'login.html')


def CTask(request):
    task = TaskMaster.objects.all()
    context = {
        'task': task
    }
    if request.method == "POST":
        Tname = request.POST.get('name')
        TDescription = request.POST.get('email')
        Category = request.POST.get('name')
        CID = request.POST.get('name')
        Role_id = request.POST.get('name')
        Tpriority = request.POST.get('name')
        status = request.POST.get('name')
        Rid = request.POST.get('name')
        Attachment = request.POST.get('name')
        UID = request.POST.get('name')

    return render(request, 'create_task.html', context)


def Viewuser(request):
    user = UserMaster.objects.all()
    context = {
        'user': user
    }
    return render(request, 'userview.html', context)


def Working(request, id):
    task = TaskMaster.objects.get(TId=id)
    task.status = 'InProgress'
    task.save()
    return redirect('login-page')


def Completed(request, id):
    task = TaskMaster.objects.get(TId=id)
    task.status = 'Completed'
    task.save()
    return redirect('login-page')

def Dashuser(request):
    return redirect('login-page')

def COEApproveUser(request):
    if 'Email' in request.session:
         queryset1 = UserMaster.objects.filter(email=request.session['Email']).values('CID')
         user = UserMaster.objects.filter(CID=queryset1[0]['CID'],Utype ='Employee'or'COE Leads')
         context={
             'user':user
         }
         return render(request, 'COEapprove_user.html',context)
    else:
        return redirect('login1')


def COEAssignTask(request):
    if 'Email' in request.session:
         queryset1 = UserMaster.objects.filter(email=request.session['Email']).values('CID')
         Task = TaskMaster.objects.filter(CID=queryset1[0]['CID'])
         user = UserMaster.objects.filter(CID=queryset1[0]['CID'],isactive='active')
         context={
             'Task':Task,
             'user':user
         }
         return render(request, 'COEassign_task.html',context)
    else:
        return redirect('login1')


def COEInsights(request):
    return render(request, 'COEInsights.html')

def COEViewUsers(request):
    if 'Email' in request.session:
         queryset1 = UserMaster.objects.filter(email=request.session['Email']).values('CID')
         user = UserMaster.objects.filter(CID=queryset1[0]['CID'],Utype ='Employee'or'COE Leads')
         context={
             'user':user
         }
         return render(request, 'COEview_users.html',context)
    else:
        return redirect('login1')

def COEAddUsers(request):
    coe= COEMaster.objects.all()
    context={
        'coe':coe
    }
    return render(request, 'COEAddUser.html',context)

def LUserAdd(request):
    
    if request.method == "POST":
        Uname = request.POST.get('Uname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        Utype = request.POST.get('Utype')
        if Utype=="Employee":
            isactive="active"
        else:
            isactive="inactive"
        CID = request.POST.get('CID')
        user = UserMaster(
                Uname=Uname,
                email=email,
                isactive=isactive,
                password=password,
                Utype=Utype,
                CID=CID
            ) 
        user.save()
        return redirect('login-page')
    

def UserTask(request,id):
    queryset1 = UserMaster.objects.filter(Uid=id).values('Uname')
    user=queryset1[0]['Uname']
    print(user)
    Task = TaskMaster.objects.filter(UID=queryset1[0]['Uname'])
    T1 = TaskMaster.objects.filter(UID=queryset1[0]['Uname']).count()
    if T1==0:
        PT=0
        PPT=0
        CT=0
        PCT=0
        OT=0
        OPT=0
    else:
        PT = TaskMaster.objects.filter(UID=queryset1[0]['Uname'], status='Pending').count()
        PPT = round(((PT / T1) * 100), 0)
        CT = TaskMaster.objects.filter(UID=queryset1[0]['Uname'], status='Completed').count()
        PCT = round(((CT / T1) * 100), 0)
        OT = TaskMaster.objects.filter(UID=queryset1[0]['Uname'], status='InProgress').count()
        OPT = round(((OT / T1) * 100), 0)
        
    
    context1 = {
                'Task': Task,
                'T1': T1,
                'CT': CT,
                'PT': PT,
                'PCT': PCT,
                'PPT': PPT,
                'OPT': OPT,
                'OT': OT,
                'user': user

            }
    return render(request, 'Coedashuser.html', context1)

def ApproveUser(request,id):
    user=UserMaster.objects.get(Uid=id)
    user.isactive='active'
    user.save()
    return redirect('COEApproval')

def BlockedUser(request,id):
    user=UserMaster.objects.get(Uid=id)
    user.isactive='Inactive'
    user.save()
    return redirect('COEApproval')

def COEAssignTaskUser(request,id):
    if request.method == "POST":
        Uname = request.POST.get('Auser')
        Task=TaskMaster.objects.get(TId=id)
        Task.UID=Uname
        Task.save()
        return redirect('COEassignTask')
        