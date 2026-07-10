from django import forms
from Website.models import Coment

class formName (forms.Form):
    name = forms.CharField(max_length=225)
    email = forms.EmailField()
    subject = forms.CharField(max_length=225)
    message = forms.CharField(max_length=255,widget=forms.Textarea)


class Coment_form(forms.ModelForm):
    class Meta:
        model = Coment
        fields = "__all__"