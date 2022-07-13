from django import forms
from .models import ProfileModel
from django.forms import FileInput


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ('pm_name', 'pm_avatar', 'pm_description', 'pm_kind_of_activity', 'pm_interests', 'pm_place_of_work')
        
        widgets = {
            'pm_avatar': FileInput(attrs={
                'accept': 'image/jpeg, image/png'
            })
        }