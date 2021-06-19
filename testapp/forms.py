from django import forms
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


class Employee(forms.Form):
    name=forms.CharField()
    eno=forms.IntegerField()
    salary=forms.FloatField()
    gmail=forms.EmailField()
    def clean_name(self):
        inputname=self.cleaned_data['name']
        if len(inputname)<4:
            raise forms.ValidationError("len of employee name should be>=4")
        else:
            return inputname
    def clean_eno(self):
        inputeno=self.cleaned_data['eno']
        print("eno validAdtion")

