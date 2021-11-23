from django import forms
from .models import Data
from datetime import date
#from.serializers import DataSerializer

class DateInput(forms.DateInput):
    input_type = 'date'



class childform(forms.ModelForm):

    class Meta:
        model = Data
        fields = ['gender', 'dob', 'weight', 'height', 'age']

       # def cal(self):
       #     return date.today() - self['dob']
        widgets = {
            'dob': DateInput()
        }
      #  fields['age'] = date.today() - fields['dob']






 #   def __init__(self, *args, **kwargs):
 #       super(childform,self).__init__(*args, **kwargs)
 #       self.fields['gender'].empty_label = "Select"

class chkform(forms.Form):
    age_when_last_weighed = forms.FloatField(label='Previous Age (in weeks)', max_value=100)
    previous_weight = forms.FloatField(label= 'Previous Weight (in kg) ', max_value=100)
    weight_at_birth = forms.FloatField(label= 'Weight at Birth (in kg) ', max_value=100)
