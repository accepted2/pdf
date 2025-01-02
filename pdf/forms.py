from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "name",
            "phone",
            "email",
            "summary",
            "degree",
            "school",
            "university",
            "previous_work",
            "skils",
        ]
