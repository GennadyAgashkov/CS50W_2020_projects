from django import forms

class EditEntryForm (forms.Form):
    title = forms.CharField(
        label = "Title", 
        widget = forms.TextInput(
            attrs={
                'class': 'form-control'
        }))
    md_content = forms.CharField(
        label = "MarkDown content",
        widget = forms.Textarea(
            attrs={
                'class': 'form-control'
        }))