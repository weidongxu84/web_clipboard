from django import forms

class AddClipForm(forms.Form):
    content_text = forms.CharField(label='', widget=forms.Textarea(attrs={'cols': 80, 'rows': 5, 'class': 'span9'}))
