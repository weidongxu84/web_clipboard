from django import forms

class AddClipForm(forms.Form):
    content_text = forms.CharField(label='', widget=forms.Textarea)
