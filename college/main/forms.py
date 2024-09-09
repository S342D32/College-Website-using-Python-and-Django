# forms.py

from django import forms
from .models import Student, Course

# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'course']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['course'].queryset = Course.objects.all()

class usersForm(forms.Form):
    num1 =forms.CharField()
    num2 =forms.CharField()