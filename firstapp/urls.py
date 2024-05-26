from django.urls import path,include

from firstapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('checkout/',views.checkout,name='checkout'),
    path('profile',views.profile,name="profile"),
    
    #path('handlerequest/', views.handlerequest, name="HandleRequest"),
    
]