from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView, UpdateView
from .models import ProfileModel
from .forms import ProfileEditForm
from utils.view_manager.sprofile import SprofileManager


class ProfileDetail(DetailView):
    model = ProfileModel
    template_name = 'sprofile/profile_detail.html'
    context_object_name = 'profile'
    slug_field = 'pm_url'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if 'follow_id' in request.POST:
                SprofileManager.create_follow(request, int(request.POST.get('follow_id')))
                print(request.POST.get('follow_id'))
                return HttpResponse('Follow')


def edit(request):
    return render(request, 'sprofile/edit_profile.html')

class ProfileEdit(UpdateView):
    model = ProfileModel
    template_name = 'sprofile/edit_profile.html'
    context_object_name = 'profile'
    form_class = ProfileEditForm
    slug_field = 'pm_url'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if 'pm_name' in request.POST:
                SprofileManager.update(request)
                return redirect('home')
