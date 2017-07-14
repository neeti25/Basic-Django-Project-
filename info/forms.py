from django import forms
from .models import UserInfo

class PostForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = [
            "first_name",
            "last_name",
            "email_id",
            #"contact",
            #"dob",
        ]
