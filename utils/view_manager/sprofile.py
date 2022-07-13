from sprofile.models import ProfileModel
from sprofile.models import FollowModel


class SprofileManager:
    @staticmethod
    def update(request):
        _ = request.POST | request.FILES
        profile = ProfileModel.objects.get(id = int(_['profile_id'][0]))
        profile.pm_name=_['pm_name'][0]
        if 'delete_avatar' in _:
            profile.pm_avatar='static_media/no_image.png'
        elif _['pm_avatar'][0]:
            profile.pm_avatar=_['pm_avatar'][0]
        profile.pm_description=_['pm_description'][0]
        profile.pm_kind_of_activity=_['pm_kind_of_activity'][0]
        profile.pm_interests=_['pm_interests'][0]
        profile.pm_place_of_work=_['pm_place_of_work'][0]
        profile.profilesocialmodel.psm_twitter = _['psm_twitter'][0]
        profile.profilesocialmodel.psm_github = _['psm_github'][0]
        profile.profilesocialmodel.psm_linkedin = _['psm_linkedin'][0]
        profile.save()

    @staticmethod
    def create_follow(request, followed_id):
        """Create and delete follows"""
            
        profile = SprofileManager.get_current_profile(request)
        followed_profile = SprofileManager.get_profile_by_id(followed_id)
        if not profile.follow.all():
            FollowModel.objects.create(p_follow=profile, p_followed=followed_profile)
        else:
            follow = FollowModel.objects.filter(p_follow=profile, p_followed=followed_profile)
            if follow:
                follow.delete()
            else:
                FollowModel.objects.create(p_follow=profile, p_followed=followed_profile)

    @staticmethod
    def get_current_profile(request):
        return ProfileModel.objects.get(pm_user=request.user)
    
    @staticmethod
    def get_profile_by_id(profId):
        return ProfileModel.objects.get(id=int(profId))

    @staticmethod
    def get_detailview_instance_slug(self):
        """Returns a detailView object using slug"""
            
        slug = self.kwargs.get(self.slug_url_kwarg)
        return slug