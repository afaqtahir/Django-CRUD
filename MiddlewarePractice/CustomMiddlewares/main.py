
class Middleware1:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("Middleware1 before")

        response = self.get_response(request)

        print("Middleware1 after")
        # Code to be executed for each request/response after
        # the view is called.

        return response


class Middleware2:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("HTTP Method:", request.method)
        print("Headers:", request.headers)
        print("GET Query Parameters:", request.GET)
        print("POST Data:", request.POST)
        # Add more attributes as needed

        # You can also inspect specific attributes like the path or URL
        print("Path:", request.path)
        print("URL:", request.build_absolute_uri())
        print("Middleware2 before")

        response = self.get_response(request)

        print("Middleware2 after")
        # Code to be executed for each request/response after
        # the view is called.

        return response