from django.shortcuts import render


def pub(request):
    return render(request, 'publication/pub_detail.html')