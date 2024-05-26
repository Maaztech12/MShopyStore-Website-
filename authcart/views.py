from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.views.generic import View
from django.contrib import messages
#from django.template.loader import render_to_string
#from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
#from .utils import TokenGenerator,generate_token
#from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError
#from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def signup(request):
    if request.method == 'POST':
        #vendorname = request.POST['vendorname']
        email = request.POST['email']
        Password = request.POST['pass1']
        Confirm_Password = request.POST['pass2']
        if Password == Confirm_Password:
            '''if User.objects.filter(vendorname = vendorname).exists():
                messages.info(request,'Username already taken')
                #return HttpResponse('Username already taken')
                return render(request,'signup.html')'''
            if User.objects.filter(username=email).exists():

                messages.info(request,'Email already taken')
                return render(request,'signup.html')
            else:
                user=User.objects.create_user(email,email,Password)
                #user.is_active=False
                user.save()
                #email_subject="Activate your account"
                
                messages.success(request,"Account Signedup Successfully")
                return redirect('/authcart/login/')
                
                
                #return HttpResponse('User created',email)
        else:
            messages.warning(request,'Password not matching')
            return render (request,'signup.html')
    else:
        return render(request,"signup.html")
        


def handlelogin(request):
    if request.method=="POST":

        username=request.POST['email']
        userpassword=request.POST['pass1']
        myuser=authenticate(username=username,password=userpassword)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/authcart/login')

    return render(request,"login.html")

def handlelogout(request):
    logout(request)
    messages.info(request,"logout Success")
    return redirect('/authcart/login')

def payment(request):
    return render(request,'paymentpage.html')

def updatestatus(request):
    
    messages.info(request,"Thanks For Shoping at MShopy Store")
    messages.info(request,"Payment is successfull")
    messages.info(request,"Your order will be delivered soon. Thank You")
    return render(request,'updatestatus.html')





'''
class ActivateAccountView(View):
    def get(self,request,uidb64,token):
        try:
            uid=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as identifier:
            user=None
        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            messages.info(request,"Account Activated Successfully")
            return redirect('/authcart/login') 
        return render(request,'activatefail.html')
'''

'''message=render_to_string('activate.html',{
                    'user': user,
                    'domain':'127.0.0.1:8000',
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':generate_token.make_token(user)
                })
                email_message=EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email])
                email_message.send()
                messages.success(request,"Activate Your Account By Clicking The Link In Your Gmail")'''


