from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Technology(models.Model):
    tech_id=models.AutoField(primary_key=True)
    tech_name=models.CharField(max_length=30)
    tech_img=models.ImageField(null=True)
    tech_desc=models.CharField(max_length=60)
    tech_type=models.CharField(max_length=60,null=True)
    core = models.CharField(max_length=60,null=True)
    def __str__(self):
        return self.tech_name

class Blog(models.Model):
    notice_id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    image = models.ImageField(null=True)
    blog = RichTextField(blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class ContactUs(models.Model):
    contact_id=models.AutoField(primary_key=True)
    full_name=models.CharField(max_length=60)
    phone=models.CharField(max_length=60)
    mail=models.EmailField()
    desc=models.TextField()
    time =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.full_name

class NewsUpdates(models.Model):
    news_id=models.AutoField(primary_key=True)
    news_title=models.CharField(max_length=200)
    news_desc = RichTextField(blank=True,null=True)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.news_title

class Post_Doubt(models.Model):
    doubt_id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=1500)
    doubt_content = models.TextField()
    author = models.CharField(max_length=20)
    time_stamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class courses(models.Model):
    course_id =models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    header_img = models.ImageField()
    course_image = models.ImageField()
    atc = models.TextField()
    skills = models.TextField()
    certificate = models.ImageField(blank=True)
    whatsapp_group_link = models.CharField(max_length=300,null=True)
    def __str__(self):
        return self.title

class enrollments(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=1000)
    time_stamp = models.CharField(max_length=30)
    def __str__(self):
        return  self.username


class review(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    email = models.EmailField()
    date = models.DateField()
    rate = models.IntegerField(null=True)
    course = models.CharField(max_length=200)
    msg = models.TextField()
    status = models.CharField(max_length=20,default='Reject')

    def __str__(self):
        return f"{self.username} from {self.course}"


class Internship_Enrollments(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    date = models.DateTimeField()
    internship = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.name} for {self.internship} on {self.date}"



