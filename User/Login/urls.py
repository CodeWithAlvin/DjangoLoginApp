from django.contrib import admin
from django.urls import path,include
from Login import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.Index,name="home"),
    path('login',views.Login,name="Login"),
    path('logout',views.Logout,name="Logout")
]    
    
    