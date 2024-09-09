from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text', 'image']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Type your message...'}),
        }