from django import forms
from .models import Chats, Nicks


class ChatsForm(forms.ModelForm):

    class Meta:
        model = Chats
        fields = ('content',)


class NicksForm(forms.ModelForm):

    class Meta:
        model = Nicks
        fields = ('name',)
