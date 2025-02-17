from http.client import HTTPResponse

from django.http import HttpResponseRedirect

from aplicatie1.models import Logs


# class RefreshMiddleware:
#
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         if request.user.is_authenticated:
#             print(request.path)
#         return self.get_response(request)


class RefreshMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if request.method == "GET":
                new_instance = Logs()
                new_instance.user_id = request.user.id
                new_instance.action = 'refresh'
                new_instance.url = request.path
                new_instance.save()
            elif request.method == "POST":
                action = 'created'
                for item in str(request.path):
                    if item.isdigit():
                        action = 'updated'
                        break
                Logs.objects.create(user_id=request.user.id, action=action, url=request.path)
        return self.get_response(request)


class RedirectMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.path == '/':
            return HttpResponseRedirect('locations')
        return self.get_response(request)

