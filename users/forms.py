from django import forms
from .models import Chat



CHOICES=[('one','one'),
         ('two','two'),
         ('three','three'),
         ('four','four')]

class CHOICES(forms.Form):
    CHOICES = forms.CharField(widget = forms.RadioSelect(choices=CHOICES))

class ChatForm(forms.ModelForm):

    class Meta:
        model = Chat
        fields = ('message', )
