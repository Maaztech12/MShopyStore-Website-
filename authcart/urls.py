from django.urls import path
from authcart import views
from authcart import utils





urlpatterns =[
    path('signup/',views.signup,name='signup'),
    path('login/',views.handlelogin,name='handlelogin'),
    path('logout/',views.handlelogout,name='handlelogout'),
    path('payment/',views.payment,name="payment"),
    path('updatestatus/',views.updatestatus,name="updatestatus"),
    
    #path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
    #path('TokenGenerator',utils.TokenGenerator,name='TokenGenerator'),
    

]