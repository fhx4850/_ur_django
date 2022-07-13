from django import template
from ..models import FollowModel, ProfileModel

register = template.Library()


@register.simple_tag
def check_follow(user, followed_profile_id):
    profile = ProfileModel.objects.get(pm_user=user)
    followed_profile = ProfileModel.objects.get(id=followed_profile_id)
    if FollowModel.objects.filter(p_follow=profile, p_followed=followed_profile):
        return True
    else:
        return False
