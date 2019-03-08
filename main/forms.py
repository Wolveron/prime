from django import forms

class Test_Form(forms.Form):
	name = forms.CharField()
	description = forms.CharField(widget = forms.Textarea(attrs={"class":"form-control"}))
	file = forms.FileField()