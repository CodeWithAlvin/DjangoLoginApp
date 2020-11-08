from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def Index(request):
	if request.user.is_anonymous:
		return redirect("/login")
	else:
		username=request.user
		return render(request,"index.html",{'name':username})
		
				
def Login(request):
	name=request.POST.get("USERNAME")
	password=request.POST.get("PASSWORD")
	user=authenticate(username=name, password=password)
	if user is not None:
		login(request,user)
		username=request.user
		return render(request,"index.html",{'name':username})
	else:
		return render(request,"login.html")	
	
def Logout(request):
	logout(request)
	return render(request,"login.html")
	
 	