from django import forms

class News_Form(forms.Form):
	title = forms.CharField()
	text = forms.CharField(widget = forms.Textarea)
