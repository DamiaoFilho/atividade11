from django import forms
from .models import Course, City, Student

class CityForm(forms.ModelForm):
    name = forms.CharField(label="Cidade")
    city = forms.CharField(label="Sigla")

class CourseForm(forms.ModelForm):
    name = forms.CharField(label="Cidade")

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'