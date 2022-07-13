from django.shortcuts import redirect


def checklogin(get_responce):
    def middleware(request):
        auth_path = ['/accounts/login/', '/accounts/signup/']
        if not request.get_full_path() in auth_path: 
            if not request.user.is_authenticated:
                return redirect('account_login')
        responce = get_responce(request)
        return responce
    return middleware