from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse



from .models import CustomModel,ViewplanModel,FoodlistModel, Foodlog, Weight
from .forms import CustomForm, FoodlistForm




def home(request):	
	if  not request.user.is_authenticated:
		return render(request,"home.html")
	else:
		return redirect("uhacks")

def ulogin(request):
	if request.method=="POST":
		un= request.POST.get("un")
		pw= request.POST.get("pw")
		user = authenticate(username=un,password=pw)
		if user is not None:
			login(request,user)
			return redirect("home")
		else:
			return render(request,"login.html",{"msg":"invalid un/pw"})
	else:
		return render(request,"login.html")

def usignup(request):
	if request.method=="POST":
		un = request.POST.get("un")
		pw1 = request.POST.get("pw1")
		pw2 = request.POST.get("pw2")
		em = request.POST.get("em")
		if pw1==pw2:
			try:
				user = User.objects.get(username=un)
				return render(request,"signup.html",{"msg":"user already exists"})
			except User.DoesNotExist:
				user = User.objects.create_user(username=un,password=pw1, email=em)
				user.save();
				return redirect("ulogin")
		else:
			return render(request,"signup.html",{"msg":"password did not match"})
	else:
			return render(request,"signup.html")
def ulogout(request):
	logout(request)
	return redirect("ulogin")

def ufoodlog(request):
    '''
    It allows the user to select food items and 
    add them to their food log
    '''
    if request.method == 'POST':
        foods = FoodlistModel.objects.all()

        # get the food item selected by the user
        food = request.POST['food_consumed']
        food_consumed = FoodlistModel.objects.get(food_name=food)

        # get the currently logged in user
        usr = request.user
        
        # add selected food to the food log
        food_log = Foodlog(usr=request.user, food_consumed=food_consumed)
        food_log.save()

    else: # GET method
        foods = FoodlistModel.objects.all()
        
    # get the food log of the logged in user
    user_food_log = Foodlog.objects.filter(usr=request.user)
    food_list = FoodlistModel.objects.all()
	
    return render(request, 'foodlog.html', {
        'food_list':food_list,
        
        'user_food_log': user_food_log
    })

def ufoodlogdelete(request,food_id=None):
	food_consumed = Foodlog.objects.filter(id=food_id)
	if request.method == 'POST':
		food_consumed.delete()
		return redirect('ufoodlog')
	return render(request, 'foodlogdelete.html')


def uaddfooditem(request):
	if request.method=="POST":
		data = FoodlistForm(request.POST, request.FILES)
		if data.is_valid():
			data.save()
			msg = "foodadded"
			fm = FoodlistForm()
			return redirect("ufoodlist")
		else:
			msg = "check errors"
			return render(request,"addfooditem.html",{"fm":data, "msg":msg})
	else:
		fm = FoodlistForm()
		return render(request,"addfooditem.html",{"fm":fm})
			
def ufoodlist(request):
	food_list = FoodlistModel.objects.all()
	return render(request,"foodlist.html",{ 'food_list':food_list})

def uhealthyrecipes(request):
	return render(request,"healthyrecipes.html")

def weight_log(request):
	
    '''
    It allows the user to record their weight
    '''
    if request.method == 'POST':

        # get the values from the form
        weight = request.POST['weight']
        entry_date = request.POST['date']

        # get the currently logged in user
        user = request.user

        # add the data to the weight log
       	weight_log = Weight(user=user, weight=weight, entry_date=entry_date)
        weight_log.save()

    # get the weight log of the logged in user
    user_weight_log = Weight.objects.filter(user=request.user)
    
    return render(request, 'weight_log.html', {'user_weight_log': user_weight_log})

def weight_log_delete(request, weight_id):
    '''
    It allows the user to delete a weight record from their weight log
    '''
    # get the weight log of the logged in user
    weight_recorded = Weight.objects.filter(id=weight_id) 

    if request.method == 'POST':
        weight_recorded.delete()
        return redirect('weight_log')
    
    return render(request, 'weight_log_delete.html')


 

	

def ucustomized(request):
	if request.method== "POST":
		form = CustomForm(request.POST)
		if form.is_valid():
			task_list = form.save(commit=False)
			task_list.name = request.user
			task_list.save()
		
			msg = " Thankyou, we will get back to you"
			fm = CustomForm()
			return render(request,"customized.html", {"fm":fm, "msg":msg})
	else:
		fm = CustomForm()
		return render(request,"customized.html",{"fm":fm})
		

def uviewdetails(request):
	if request.user.is_authenticated:
		usr = User.objects.get(username=request.user.username)
		usr=usr.username
	
	view_plan = ViewplanModel.objects.filter(usr=request.user) 
	
	return render(request,"viewdetails.html",{ 'view_plan':view_plan})

def uhacks(request):
	return render(request, "hacks.html")




	
	


