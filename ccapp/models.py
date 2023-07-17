from django.db import models
from django.contrib.auth.models import User

class FoodlistModel(models.Model):
    food_name = models.CharField(max_length=40)
    category = models.CharField(max_length=40)
    calories = models.FloatField()
    fat = models.FloatField()
    carbs = models.FloatField()
    protein = models.FloatField()
    image= models.ImageField()
    
    def __str__(self):
        return self.name	
	

class CustomModel(models.Model):
	name = models.ForeignKey(User, on_delete=models.CASCADE,editable=False)
	gender = models.CharField(max_length=10)
	age = models.IntegerField()
	height = models.FloatField()
	current_weight = models.FloatField()
	preference = models.CharField(max_length=20)
	daily_activity = models.CharField(max_length=40)
	primary_goal =  models.CharField(max_length=40)
	goal_pace =  models.FloatField()
	allergies = models.CharField(max_length=40)
	city = models.CharField(max_length=40)
	customdt = models.DateTimeField(auto_now_add=True)


	def register(self):
		self.save()
	
class ViewplanModel(models.Model):
	usr = models.ForeignKey(User, on_delete=models.CASCADE)
	total_carbs = models.CharField(max_length=100)
	total_protein = models.CharField(max_length=100)
	total_fats = models.CharField(max_length=100)
	bmi = models.CharField(max_length=500)
	food_intake = models.CharField(max_length=500)
	avoid_such_foods = models.CharField(max_length=500)
	breakfast_options = models.CharField(max_length=500)
	mid_snack_options =  models.CharField(max_length=500)
	lunch_options = models.CharField(max_length=500)
	dinner_options = models.CharField(max_length=500)
	tips = models.CharField(max_length=500)

class Foodlog(models.Model):
	usr = models.ForeignKey(User, on_delete=models.CASCADE)
	food_consumed = models.ForeignKey(FoodlistModel, on_delete=models.CASCADE )

	def __str__(self):
      		return f'{self.user.username} - {self.food_consumed.food_name}'

class Weight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=7, decimal_places=2)
    entry_date = models.DateField()

    def __str__(self):
        return f'{self.user.username} - {self.weight} kg on {self.entry_date}'

	
	
	

	
	
		
	

	
