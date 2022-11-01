class TestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Antes do get_response")
        request.corporation = "corporation"
        response = self.get_response(request)
        print("Depois do get_response")
        return response