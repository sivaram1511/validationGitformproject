from django import forms
class StudentForm(forms.Form):
    name=forms.CharField(max_length=124)
    rollno=forms.IntegerField()
    gmail=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)