from django import forms
from .models import Chats


class ChatsForm(forms.ModelForm):

    class Meta:
        model = Chats
        fields = ('content',)
