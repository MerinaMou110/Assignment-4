from django.urls import path,include
from . import views

urlpatterns = [
   
    path("/addCategory",views.add_category,name="add_category"),
  
   
]