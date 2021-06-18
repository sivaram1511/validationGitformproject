from django.shortcuts import render

#from testapp import forms
from testapp.forms import StudentForm
# Create your views here.
def student_info_view(request):
    if request.method=='GET':
       form=StudentForm()
    if request.method=='POST':
       form=StudentForm(request.POST)
       if form.is_valid():
            print("validation completed..printing student info")
            print("student name",form.cleaned_data['name'])
            print("student rollno:",form.cleaned_data['rollno'])
            print("student email:",form.cleaned_data['gmail'])
    return render(request,'testapp/index.html',{'form':form})