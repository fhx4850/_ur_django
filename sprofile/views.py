from django.shortcuts import render


def prof(request):
    return render(request, 'sprofile/profile_detail.html')