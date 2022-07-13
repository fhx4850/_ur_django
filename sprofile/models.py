from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse



def generate_url(id):
    ids = str(id)
    h = str(hash(str(id)))[-3::]
    url = ids + h
    return url


class ProfileModel(models.Model):
    pm_user = models.OneToOneField(User, on_delete=models.CASCADE)
    pm_avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    pm_name = models.CharField(max_length=100, null=True, blank=True, default='Not specified.')
    pm_description = models.TextField(max_length=500, null=True, blank=True, default='Not specified.')
    pm_kind_of_activity = models.CharField(max_length=150, null=True, blank=True, default='Not specified.')
    pm_interests = models.TextField(max_length=300, null=True, blank=True, default='Not specified.')
    pm_place_of_work = models.CharField(max_length=150, null=True, blank=True, default='Not specified.')
    pm_url = models.SlugField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.pm_user.username

    def get_absolute_url(self):
        return reverse('profile', kwargs={'slug': self.pm_url})

    def get_edit_url(self):
        return reverse('edit_profile', kwargs={'slug': self.pm_url})

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, *args, **kwargs):
        if created and instance.username != 'root':
            ProfileModel.objects.create(pm_user=instance)
            instance.profilemodel.pm_avatar = 'static_media/no_image.png'
            instance.profilemodel.pm_url = generate_url(instance.profilemodel.id)
            instance.profilemodel.save()

            ProfileSocialModel.objects.create(psm=instance.profilemodel)


class ProfileSocialModel(models.Model):
    psm = models.OneToOneField(ProfileModel, on_delete=models.CASCADE, null=True)
    psm_twitter = models.CharField(max_length=200, null=True, blank=True)
    psm_github = models.CharField(max_length=200, null=True, blank=True)
    psm_linkedin = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.psm.pm_user.username


class FollowModel(models.Model):
    p_follow = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='follow')
    p_followed = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='followed')
    
    def __str__(self):
        return f'{self.p_follow}-{self.p_followed}'