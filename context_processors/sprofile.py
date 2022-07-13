from sprofile.models import FollowModel

def mfollows(request):
    if request.user.username != 'root':
        follows = []
        my_follows = FollowModel.objects.filter(p_follow=request.user.profilemodel)
        for f in my_follows:
            follows.append(f.p_followed)
        return {'follows': follows}
    else: 
        return {'follows': None} 
