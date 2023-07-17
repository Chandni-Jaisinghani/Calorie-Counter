from django import forms
from .models import  CustomModel,ViewplanModel,FoodlistModel


CHOICES1 = [('',''),('male','Male'),('female','Female'),('other','Other')]
CHOICES2 = [('',''),('no activity', 'No Activity'),('lightly active', 'Lightly Active'), ('moderately active', 'Moderatively Active'), ('very active', 'Very Active')]
CHOICES3 = [('',''),('lose weight', 'Lose Weight'),('be fitter', 'Be Fitter'),('gain muscle','Gain Muscle')]
CHOICES4 =[('',''),('veg','Veg'),('nonveg','NonVeg')]
class CustomForm(forms.ModelForm):
	gender = forms.ChoiceField(choices=CHOICES1)
	daily_activity = forms.ChoiceField(choices=CHOICES2)
	primary_goal = forms.ChoiceField(choices=CHOICES3)
	preference = forms.ChoiceField(choices=CHOICES4)
	class Meta:
		model= CustomModel
		fields = [ "gender", "age", "height", "current_weight", "preference" , "daily_activity", "primary_goal", "goal_pace", "allergies", "city"]


class ViewplanForm(forms.ModelForm):
	class Meta:
		model = ViewplanModel
		fields = [ "usr", "total_carbs", "total_protein", "total_fats", "bmi", "food_intake", "avoid_such_foods", "breakfast_options", "mid_snack_options", "lunch_options", "dinner_options", "tips"]

class FoodlistForm(forms.ModelForm):
	class Meta:
		model = FoodlistModel
		fields = ["food_name", "category", "calories", "fat", "carbs", "protein", "image"]

