import time
from django.http import HttpResponseForbidden


class LogRequestMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Process before View
        print(f"[Middleware] Request Path: {request.path}")
        response = self.get_response(request)

        # Process after View
        print(f"[Middleware] Response Staus:{response.status_code}")

        return response


class TimerMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        startTime = time.time()
        response = self.get_response(request)
        timeDuration = time.time() - startTime
        print(f"[Middleware] Request took {timeDuration:.2f} seconds")

        return response


class BlockIPMiddleware:

    BLOCK_IPS = []

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get("REMOTE_ADDR")
        if ip in self.BLOCK_IPS:
            return HttpResponseForbidden("آی پی شما بلاک است!!")

        return self.get_response(request)
