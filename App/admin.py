from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

# Register your models here.
from .models import Technology
from .models import Blog
from .models import ContactUs
from .models import NewsUpdates
from .models import Post_Doubt
from .models import courses
from .models import enrollments
from .models import review
from .models import Internship_Enrollments
admin.site.register(Technology)
admin.site.register(ContactUs)
admin.site.register(NewsUpdates)
admin.site.register(Blog)
admin.site.register(Post_Doubt)
admin.site.register(courses)
admin.site.register(enrollments)
admin.site.register(review)
admin.site.register(Internship_Enrollments)

#admin.site.register(Doubt)


