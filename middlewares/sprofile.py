from django.shortcuts import redirect


def profile_validation(get_responce):
    def middleware(request):
        responce = get_responce(request)
        return responce

    def process_view(request, view_func, view_args, view_kwargs):
        req_path = request.get_full_path()
        if req_path.startswith('/profile/') and req_path.endswith('/edit/'):
            if not request.user.profilemodel.pm_url == view_kwargs['slug']:
                return redirect('profile', request.user.profilemodel.pm_url)
    middleware.process_view = process_view
    return middleware