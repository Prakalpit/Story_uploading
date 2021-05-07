from django import forms


class StoryForm(forms.Form):
    title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title here!!',}))
    story=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Start writing stories here!!'}))
