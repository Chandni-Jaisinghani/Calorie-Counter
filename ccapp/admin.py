from django.contrib import admin

from .models import CustomModel, ViewplanModel,FoodlistModel, Foodlog, Weight

class FoodlistAdmin(admin.ModelAdmin):
    list_display = ("food_name", "category", "calories", "fat","carbs","protein","image")

class CustomAdmin(admin.ModelAdmin):
	list_display = ("name", "gender", "age", "height", "current_weight", "preference", "daily_activity", "primary_goal", "goal_pace", "allergies", "city",)
	list_filter = ("customdt",)

admin.site.register(CustomModel, CustomAdmin)

class ViewplanAdmin(admin.ModelAdmin):
	list_display = ("usr", "total_carbs", "total_protein", "total_fats", "bmi", "food_intake", "avoid_such_foods", "breakfast_options", "mid_snack_options", "lunch_options", "dinner_options", "tips")
	
admin.site.register(ViewplanModel, ViewplanAdmin)
admin.site.register(FoodlistModel)

class FoodlogAdmin(admin.ModelAdmin):	
	list_display = ("usr", "food_consumed")

admin.site.register(Foodlog,FoodlogAdmin)

admin.site.register(Weight)
