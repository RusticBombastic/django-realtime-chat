from django.forms import ModelForm
from django import forms
from .models import ChatMessage


class ChatMessageCreateForm(ModelForm):
    class Meta:
        model = ChatMessage
        fields = ["body"]
        widgets = {
            "body": forms.TextInput(
                attrs={
                    "placeholder": "Add message...",
                    "class": "pt-4 text-black",
                    "maxlength": "300",
                    "autofocus": True,
                }
            ),
        }
