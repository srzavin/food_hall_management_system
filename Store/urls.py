from django.urls import path
from Store import views

urlpatterns = [
    path('', views.store_view,),
    path('cart/', views.cart_view, name='cart'),
    path('menu/', views.menu_view, name='menu'),
    path('merchant/', views.merchant_view, name='merchant'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('checkout/', views.checkout, name='checkout'),
    path('OPM/', views.OPM, name='OPM'),
    path('RtH/', views.RtH, name='RtH'),
    path('adminLogin/', views.adminLoginPage, name='adminLogin'),
    path('adminPanel/', views.adminPanel, name='adminPanel'),
    path('addStore/', views.addStore, name='addStore'),
    path('edit/', views.view_order_status, name="order_status"),
    path('createUser/', views.create_user)
]
