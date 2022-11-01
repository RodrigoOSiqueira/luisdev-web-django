from django.http import HttpResponse


class Test2Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        print("Depois do get_response")
        return response

    def process_view(self, request, view, *args, **kwargs):
        print("dentro do processview")
        request.test = "test"

    def process_exception(self, request, exception):
        return HttpResponse("Algo deu errado")
