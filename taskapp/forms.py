from django import forms
from django.forms import ModelForm

from taskapp.models import StuFac
# from taskapp.models import Fac


# class StudentForm(ModelForm):
# 	class Meta:
# 		model=Stu
# 		fields='__all__'

# 		widgets={

# 		'name':forms.TextInput(attrs={'placeholder':'enter name','class':'form-control'}),
# 		'password':forms.TextInput(attrs={'placeholder':'Enter password','class':'form-control'}),
# 		'id1':forms.TextInput(attrs={'placeholder':'Enter your id','class':'form-control'}),
# 		'email':forms.EmailInput(attrs={'class':'form-control my-1','placeholder':'Enter Email'}),
# 		'collegename':forms.TextInput(attrs={'class':'form-control my-1','placeholder':'Enter your collegename'}),
# 		'department':forms.Select(attrs={'class':'form-control'})

# 		}

class StuFacultyForm(ModelForm):
	class Meta:
		model=StuFac
		fields='__all__'

		widgets={
		'fac_name':forms.TextInput(attrs={'placeholder':'enter faculty name','class':'form-control'}),
		'fac_password':forms.TextInput(attrs={'placeholder':'Enter password','class':'form-control'}),
		'id1':forms.TextInput(attrs={'placeholder':'Enter your id','class':'form-control'}),
		'fac_email':forms.EmailInput(attrs={'class':'form-control my-1','placeholder':'Enter Email'}),
		'fac_collegename':forms.TextInput(attrs={'class':'form-control my-1','placeholder':'Enter your collegename'}),
		'fac_department':forms.Select(attrs={'class':'form-control'}),
		'salary':forms.NumberInput(attrs={'class':'form-control'}),
		'designation':forms.TextInput(attrs={'placeholder':'enter your designation','class':'form-control'})
		}