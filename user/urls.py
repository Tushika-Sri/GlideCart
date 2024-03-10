from django.urls import path
from . import views
urlpatterns=[
    path('index/',views.index),
    path('',views.index),
    path('about/',views.about),
    path('product/',views.product),
    path('signin/',views.signin),
    path('signup/',views.signup),
    path('signout/',views.signout),
    path('customer/',views.contact),
    path('myprofile/',views.myprofile),
    path('mycart/',views.mycart),
    path('cartitems/',views.cartitems),
    path('order/',views.morder),
    path('indexcart/',views.indexcart),
    path('privacy/',views.privacy),
    path('mprofile/',views.mprofile),
    path('orderslist/', views.orderslist),

]