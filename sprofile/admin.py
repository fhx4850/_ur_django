from django.contrib import admin
from .models import ProfileModel, ProfileSocialModel, FollowModel


admin.site.register(ProfileModel)
admin.site.register(ProfileSocialModel)
admin.site.register(FollowModel)