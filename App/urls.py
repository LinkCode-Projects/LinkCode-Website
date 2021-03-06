from django.urls import path
from . import views
urlpatterns = [
    path('', views.home2, name="home"),
    path('Course/<str:title>', views.Courses, name="Course"),
    path('base/', views.base, name="base"),
    path('compiler/', views.CompilerRep, name="CompilerRepl"),
    path('explore/', views.Explore, name="explore"),
    path('ContactUs/', views.contactus, name="ContactUs"),
    path('Notice/', views.NoticePage, name="Notice"),
    path('mid/<str:For>', views.mid, name="mid"),
    path('DSALGO/', views.DS_ALGO, name="DSALGO"),
    path('Explore/', views.Explore, name="BigDataCourse"),
    path('registration/', views.profile_reg, name="reg"),
    path('handlelogin/', views.handlelogin, name="handlelogin"),
    path('NoticeDetails/<str:date>', views.NoticeDetails, name="NoticeDetails"),
    path('UpdateNotifications/', views.UpdateNotifications, name="UpdateNotifications"),
    path('WebDevCourse/', views.WebDevCourse, name="WebDevCourse"),
    path('News/', views.News, name="News"),
    path('Blog/', views.Blog_Posts, name="Blog"),
    path('Classes_Enrolled/', views.Classes_Enrolled, name="features"),
    path('AI/', views.AI, name="AI"),
    path('Automation/', views.Automation, name="Automation"),
    path('AppDev/', views.AppDev, name="AppDev"),
    path('AdminNotifications/', views.Admin_Side_Notifications, name="AdminSideNotifications"),
    path('login/', views.handlelogin, name="login"),
    path('logout/', views.profile_logout, name="logout"),
    path('UpdateNotificationDetails/<str:date>', views.NotficationDetailsUpdate, name="UpdateNotificationDetails"),
    path('ReadBlog/<int:id>',views.ReadBlog,name="ReadBlog"),
    path('review/',views.Reviews,name="review"),
    path('post_review/',views.post_review,name="post_review"),
    path('review_processing/',views.Review_Processing,name="review_processing"),
    path('review_update/<int:id>',views.review_update,name="review_update"),
    path('internship/',views.internship,name="internship"),
    ]
