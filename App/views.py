import smtplib
import time
from datetime import date
from email.mime.text import MIMEText

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render

from .models import Blog
from .models import ContactUs
from .models import NewsUpdates
from .models import Technology
from .models import courses
from .models import enrollments
from .models import review
from .models import Internship_Enrollments

import datetime

# ------------------------------------------------------------------------------------------------------------------------------------
'''Send Mail Class Helps user to get whatsapp links to join their respective courses groups'''
'''It takes three arguments 1.Course Name,2.Username during session,3.Reciever Email'''

TimeStamp = date.today()
class Send_Mail:
    def __init__(self, course, to, reciever):
        self.course = course
        self.to = to
        self.reciever = reciever
        server = smtplib.SMTP_SSL('p3plzcpnl445405.prod.phx3.secureserver.net', 465)
        server.login('service@linkcode.in', 'Asdfghjkl@27')

        get_link = courses.objects.filter(title=self.course)
        for x in get_link:
            Email_Body = f"""<pre>
                                    <h1 style="text-align:center;color:blue">Welcome To LinkCode Family</h1>
                                    <hr>
                                    <h3 style="text-align:center">Congratulations!{self.to} You've successfully enrolled for course at LinkCode Technologies.</h3>
                                    <h3 style="text-align:center">Hope You will enjoy learning {self.course} and shaping future with us!</h3>
                                    <img style="width:300px;display:block;justify-content:center;align-items:center" src="https://images.pexels.com/photos/546819/pexels-photo-546819.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260">
                                    <h3>Join:<a class="button" style="color:white;border-radius:30px;background:gold" href="{x.whatsapp_group_link}">click here</button></a></h3>
                                    <h3>Thanks,</h3>
                                    <h3>Team LinkCode.</h3>
                                    <hr>
                                    </pre>"""
        msg = MIMEText(Email_Body, 'html')
        msg['Subject'] = f'LINKCODE TECHNOLOGIES => link to join course'
        server.sendmail('ashutoshpythonanywhere27@gmail.com', self.reciever, msg.as_string())
        server.quit()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Firebase Firestor credentials authentication and initialization

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('linkcode-24661-20479410f6dd.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()


# -----------------------------------------------------------------------
def profile_reg(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        mail = request.POST['mail']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        phone = request.POST['phone']

        if len(username) > 20:
            messages.warning(request, "Length of UserName Must Be less Than 15")

        elif User.objects.filter(email=mail):
            messages.warning(request, 'Email Already Registered')

        elif (pass1 != pass2):
            messages.warning(request, "Password Didn't Match")
        # Create User
        else:
            myuser = User.objects.create_user(username, mail, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.phone = phone
            myuser.save()
            messages.success(request, "Welcome To LinkCode Family!")
    return render(request, 'App/registration.html')
def handlelogin(request):
    if request.method == "POST":
        login_username = request.POST['username']
        login_password = request.POST['password']

        user = authenticate(username=login_username, password=login_password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully Logged In')
            return redirect(home2)
        else:
            messages.warning(request, "Invalid UserName Or Password")

    return render(request, 'App/User_login.html')
def profile_logout(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out')
    return redirect(home2)


def base(request):
    return render(request, 'App/base.html')

def home2(request):
    python = Technology.objects.filter(tech_name='Python')
    java = courses.objects.filter(title='Java')
    ml = courses.objects.filter(title='Machine-Learning')
    tech = Technology.objects.filter(tech_type='PL')
    dataBase = Technology.objects.filter(tech_type='DataBase')
    web = Technology.objects.filter(tech_type='Web')
    os = Technology.objects.filter(tech_type='OS')
    apps = Technology.objects.filter(tech_type='App')
    apple_ide = Technology.objects.filter(tech_type='Apple-IDE')
    android_ide = Technology.objects.filter(tech_type='Android-IDE')

    if request.method == "POST":
        full_name = request.POST.get('full_name', '')
        phone = request.POST.get('phone', '')
        mail = request.POST.get('mail', '')
        desc = request.POST.get('desc', '')

        contact = ContactUs(full_name=full_name, phone=phone, mail=mail, desc=desc)
        contact.save()
        messages.success(request, "Your Valuable Feedback Sent!!!")

    return render(request, 'App/home2.html',
                  {'ml': ml, 'python': python, 'java': java, 'tech': tech, 'database': dataBase, 'web': web, 'os': os,
                   'apps': apps, 'apple_ide': apple_ide, 'android_ide': android_ide})

def Courses(request, title):
    timestamp = date
    if request.method == "POST" and User.is_authenticated:
        username = request.POST.get("username", '')
        u_email = request.POST.get("email", '')
        course = request.POST.get("course", '')
        time_stamp = request.POST.get("timestamp", '')
        enrolls = enrollments(username=username, email=u_email, course=course, time_stamp=time_stamp)
        if enrollments.objects.filter(course=course).filter(email=u_email):
            messages.warning(request, 'You have already enrolled!')
        elif User.objects.filter(email=u_email):
            #messages.success(request, 'Wait for a while you will receive an email from us!....Saving....')
            enrolls.save()
            db.collection(u'Courses').document(course).collection(username).add({
                'name': username,
                'email': u_email,
                'course': course,
                'time_stamp': time_stamp,
            })
            #Send_Mail(course, request.user, u_email)
            messages.success(request, 'Congratulations You enrolled for class')
        else:
            messages.warning(request, 'You are not authorized! Please consider logging in! ')
    course = courses.objects.filter(title=title)
    return render(request, 'App/Course.html', {'course': course, 'time': timestamp.today(), 'message': messages})

def Classes_Enrolled(request):
    classes_info = enrollments.objects.filter(username=request.user)
    intern_info = Internship_Enrollments.objects.filter(name=request.user)
    return render(request, 'App/Classes_Enrolled.html', {'classes_info': classes_info,'intern_info':intern_info})

def WebDevCourse(request):
    return render(request, 'App/WebDevCourse.html')

def DS_ALGO(request):
    return render(request, 'App/DS-ALGO.html')

def AI(request):
    ai = courses.objects.filter(title='Artificial_Intelligence')
    timestamp = date
    if request.method == "POST" and User.is_authenticated:
        user_name = request.POST.get("username", '')
        u_email = request.POST.get("email", '')
        time_stamp = request.POST.get("timestamp", '')
        enrolls = enrollments(username=user_name, email=u_email, course='AI', time_stamp=time_stamp)

        if enrollments.objects.filter(course='Artificial_Intelligence').filter(email=u_email):
            messages.warning(request, 'You have already enrolled!')
        elif User.objects.filter(email=u_email):
            enrolls.save()
            db.collection(u'Courses').document('Artificial_Intelligence').collection(user_name).add({
                'name': user_name,
                'email': u_email,
                'course': 'Artificial_Intelligence',
                'time_stamp': time_stamp,
            })
            #Send_Mail('Artificial_Intelligence', request.user, u_email)
            messages.success(request, 'Congratulations You enrolled for class,')
        else:
            messages.warning(request, 'You are Unauthorized Consider Logging In!')

    return render(request, 'App/AI.html', {'AI': ai, 'time': timestamp.today(), 'message': messages})

def Automation(request):
    Auto = courses.objects.filter(title='Automation')
    timestamp = date
    if request.method == "POST" and User.is_authenticated:
        user_name = request.POST.get("username", '')
        u_email = request.POST.get("email", '')
        time_stamp = request.POST.get("timestamp", '')
        enrolls = enrollments(username=user_name, email=u_email, course='Automation', time_stamp=time_stamp)
        if enrollments.objects.filter(course='Automation').filter(email=u_email):
            messages.warning(request, 'You have already enrolled!')
        elif User.objects.filter(email=u_email):
            enrolls.save()
            db.collection(u'Courses').document('Automation').collection(user_name).add({
                'name': user_name,
                'email': u_email,
                'course': 'Automation',
                'time_stamp': time_stamp,
            })
            #Send_Mail('Automation', request.user, u_email)
            messages.success(request, 'Congratulations You enrolled for class')
            #messages.success(request, 'Email is sent to your registered mail address')
        else:
            messages.warning(request, 'You are not authorized! Please consider logging in! ')
    return render(request, 'App/Automation.html', {'Auto': Auto, 'time': timestamp.today(), 'message': messages})

def AppDev(request):
    app_courses = courses.objects.filter(title='Android')
    apps = Technology.objects.filter(tech_type='App')
    timestamp = date.today()
    if request.method == "POST" and User.is_authenticated:
        user_name = request.POST.get("username", '')
        email = request.POST.get("email", '')
        course_name = request.POST.get("course", '')
        time_stamp = request.POST.get("timestamp", '')

        enrolls = enrollments(username=user_name, email=email, course='Android', time_stamp=time_stamp)
        if enrollments.objects.filter(course='Android').filter(email=email):
            messages.warning(request,'You have already enrolled!')
        elif User.objects.filter(email=email):
            enrolls.save()
            db.collection(u'Courses').document('Android').collection(user_name).add({
                 'name': user_name,
                 'email': email,
                 'course': 'Android',
                 'time_stamp': time_stamp,
                 })
            #Send_Mail('Android', request.user, email)
            messages.success(request, 'Congratulations You enrolled for class')

        else:
            messages.warning(request,'You are not authorized! Please consider logging in! ')


    return render(request,'App/AppDev.html',{'apps':apps,'app_courses':app_courses,'time':timestamp,'message':messages})


def contactus(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name', '')
        phone = request.POST.get('phone', '')
        mail = request.POST.get('mail', '')
        desc = request.POST.get('desc', '')

        contact = ContactUs(full_name=full_name, phone=phone, mail=mail, desc=desc)
        contact.save()
        messages.success(request, "Your Valuable Feedback Sent!!!")

    return render(request, 'App/ContactUs.html')
def ReadBlog(request, id):
    readblog = Blog.objects.filter(notice_id=id)
    return render(request, 'App/ReadBlog.html', {'readblog': readblog})
def Blog_Posts(request):
    first = Blog.objects.filter(notice_id=1)
    blogs = Blog.objects.filter(notice_id__gt=1)
    return render(request, 'App/blog.html', {'blogs': blogs, 'first': first})
def Explore(request):
    return render(request, 'App/explore.html')

@login_required()
def mid(request, For):
    noti = db.collection('Notifications').where(u'to', u'==', For).get()
    return render(request, 'App/mid.html', {'noti': noti})

@login_required()
def NoticeDetails(request, date):
    get_notice = db.collection('Notifications').where(u'posted_on', u'==', date).get()
    return render(request, 'App/NoticeDetails.html', {'get_notice': get_notice})

def UpdateNotifications(request):
    notifications = db.collection('Notifications').stream()
    if request.method == "POST":
        subject_delete = request.POST.get('deletion')
        db.collection(u'Notifications').document(subject_delete).delete()
    return render(request, 'App/UpdateNotifications.html', {'notifications': notifications})

@login_required()
def Admin_Side_Notifications(request):
    if request.method == 'POST' and User.is_superuser:
        if True:
            title = request.POST.get('title')
            msg = request.POST.get('msg')
            to = request.POST.get('to')
            time_posted = str(time.ctime()).replace(" ","-")
            status = request.POST.get('send_email')
            db.collection('Notifications').document(time_posted).set({
                'title': title,
                'to': to,
                'message': msg,
                'posted_on': time_posted,
            })

            #'''if to == "All" and status == 'on':
               # server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                #All_mails = User.objects.all()
                #for x in All_mails:
                   # notification = MIMEText(msg, 'html')
                   # notification['Subject'] = f'LINKCODE TECHNOLOGIES Classroom Notification'
                   # server.sendmail('ashutoshpythonanywhere27@gmail.com', x.email, notification.as_string())
                #server.quit()
               # messages.success(request, 'Notification Posted Successfully to All your Users')'''

            '''Email Notification System'''
            #if status == 'on':
                #'''Server Establishment Settings'''
                #server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                #server.login('ashutoshpythonanywhere27@gmail.com', 'Asdfghjkl@27')
                #mails = enrollments.objects.filter(course=to)
                #for x in mails:
                    #notification_for_specifics = MIMEText(msg, 'html')
                    #notification_for_specifics['Subject'] = f'LINKCODE TECHNOLOGIES {to} Classroom Notification'
                    #server.sendmail('ashutoshpythonanywhere27@gmail.com', x.email,
                                    #notification_for_specifics.as_string())
                #server.quit()'''
            messages.success(request, 'Notification Posted Successfully')
        else:
            messages.warning(request,
                             'Connection to cloud was lost please check internet connection,or trying restarting the site')
    return render(request, 'App/AdminSideNotification.html')

@login_required
def NotficationDetailsUpdate(request, date):
    un = db.collection(u'Notifications').where(u'posted_on', u'==', date).stream()
    if request.method == "POST":
        title = request.POST.get('title')
        msg = request.POST.get('msg')
        to = request.POST.get('to')

        db.collection(u'Notifications').document(date).update({
            'title': title,
            'message': msg,
            'to': to
        })
        messages.success(request, 'Notification Updated Successfully')
    return render(request, 'App/UpdateNotificationDetails.html', {'un': un})


@login_required
def News(request):
    news = NewsUpdates.objects.all()
    return render(request, 'App/News.html', {'news': news})

@login_required
def NoticePage(request):
    user_session = enrollments.objects.filter(username=request.user)
    return render(request, 'App/Notice.html', {'classes_enrolled': user_session})

def Reviews(request):
    see_reviews = review.objects.filter(status="Approve")
    return render(request, 'App/review.html', {'review': see_reviews})

@login_required
def post_review(request):
    if User.is_authenticated:
        if request.method == "POST":
            rate = request.POST.get('rate')
            name = request.POST.get('username', '')
            course_name = request.POST.get('course_name', '')
            date = TimeStamp
            msg = request.POST.get('message', '')
            email = request.POST.get('email', '')
            self_captcha = request.POST.get('self_captcha')
    
            print(self_captcha)
    
            if (rate == ""):
                messages.warning(request, 'We need Stars!')
    
            elif (self_captcha == 'None'):
                messages.success(request, 'Please check it on if your content is correct')
    
            elif (self_captcha == 'on'):
                rating = review(username=name, email=email, rate=rate, course=course_name, date=date, msg=msg)
                rating.save()
                messages.success(request, 'Your review is successfully saved')
            else:
                messages.success(request, 'Something Went Wrong!')
    else:
        messages.warning(request,'Login Required To Proceed')
    return render(request, 'App/post_review.html')

@staff_member_required
def review_update(request, id):
    see_reviews = review.objects.filter(id=id)
    set_review_status = review.objects.filter(id=id)
    if request.method == "POST":
        review_status = request.POST.get('status')
        set_review_status.update(status=review_status)
    return render(request, 'App/review-update.html', {'review': see_reviews})

@staff_member_required
def Review_Processing(request):
    see_reviews = review.objects.all()
    return render(request, 'App/review-summary.html', {'review': see_reviews})


def internship(request):
    tech_java = Technology.objects.filter(core = "java")
    tech_python = Technology.objects.filter(core = "python")
    tech_common = Technology.objects.filter(core = "common")
    tech_mean = Technology.objects.filter(core = "mean")

    if request.method == "POST" and User.is_authenticated:
        name = request.POST.get('username','')
        email = request.POST.get('email','')
        internship = request.POST.get('course','')
        date = datetime.datetime.now()

        if Internship_Enrollments.objects.filter(email=email).filter(internship=internship):
            messages.warning(request, f"You Have Already Enrolled For {internship} internship ")

        elif User.objects.filter(email = email):
            internship_data = Internship_Enrollments(name=name,email = email,date = date,internship=internship)
            internship_data.save()
            messages.success(request,f"Congratulations You Enrolled For The {internship} Internship")

        else:
            messages.warning(request,"Please Login To Join The Internship")


    return render(request,'App/internship.html',{'tech_java':tech_java,'tech_python':tech_python,'tech_common':tech_common,'tech_mean':tech_mean})

def training(request):
    return render(request,'App/training.html')

@login_required
def CompilerRep(request):
    return render(request,'App/compiler.html')

