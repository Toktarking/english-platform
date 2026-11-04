from django.http import HttpResponse


OLD_HOST = (
    "english-platform-production-bd42."
    "up.railway.app"
)

NEW_ORIGIN = (
    "https://english-platform-production-4774."
    "up.railway.app"
)


class OldDomainRedirectMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        host = (
            request.get_host()
            .split(":")[0]
            .lower()
        )

        if host == OLD_HOST:

            response = HttpResponse(
                status=308
            )

            response["Location"] = (
                NEW_ORIGIN
                + request.get_full_path()
            )

            return response

        return self.get_response(request)
