from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
            'text': forms.TextInput(attrs={'placeholder':"add TODO", 'required':False}),
            
            }
