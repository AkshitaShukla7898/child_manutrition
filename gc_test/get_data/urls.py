from django.urls import path
from django.views.generic import TemplateView
#from rest_framework.routers import DefaultRouter
#from .views import data_list
from .views import child_list
from .views import child_form
from .views import growth_checker
from .views import child_gr
from .views import height


#router = DefaultRouter('data', DataViewset)
app_name='get_data'

urlpatterns = [

   # path('data/', data_list),
    path('list/', child_list),
    path('growth/', child_gr),
    path('height/', height),
    path('form/', child_form),
    path('form/checker/', growth_checker),

]
