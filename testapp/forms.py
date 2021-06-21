from django import forms
from django.core import validators
class StudentForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    gmail=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)
    def clean_name(self):
        inputname=self.cleaned_data['name']
        if len(inputname)<4:
            raise forms.ValidationError("the length of the name should be >=4")
        else:
            return inputname

def starts_with_z(value):
    if value[0].lower() !='z':
        raise forms.ValidationError("the name should be start with Z")

def starts_with_alpha(value):
    if value.isalnum()!=True:
        raise forms.ValidationError("names should be alphabets")
def gmail_verification(value):
    if value[len(value)-9:]!="gmail.com":
        raise forms.ValidationError("must be gmail")
def max_salary(value):
    if value >=9999999:
        raise forms.ValidationError("salary less tha 10lakhs")
class Employee(forms.Form):
    name=forms.CharField(validators=[starts_with_alpha])
    eno=forms.IntegerField()
    salary=forms.FloatField(validators=[max_salary])
    gmail=forms.EmailField(validators=[gmail_verification])
    feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])

