from django.shortcuts import render


def test(request):
    return render(request, 'main_page/publication_list.html')