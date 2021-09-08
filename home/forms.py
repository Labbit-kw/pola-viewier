from django import forms
from .models import Filter


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name name', max_length=7)


class IpLoad(forms.ModelForm):
    class Mata:
        model = Filter
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Filter
        # exclude = ['author', 'updated', 'created', ]
        fields = ['name','ip_1','ip_2','ip_3','ip_4']
        widgets = {
            'text': forms.TextInput(attrs={
                'name': 'post-text',
                'required': True,
                'placeholder': 'Say something...'
            }),
        }


class JoinForm(forms.Form): # or forms.ModelForm
    email = forms.EmailField()
    name = forms.CharField(max_length=120)