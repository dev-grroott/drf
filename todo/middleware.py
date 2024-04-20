from django.utils.deprecation import MiddlewareMixin

from django.http import HttpResponseRedirect

class CustomMiddleware(MiddlewareMixin):
    
    def __init__(self, get_response):
        self.get_response = get_response

    # request
    def process_request(self, request):
        pass
        # hostname = request.get_host()
        # path = request.get_full_path()
        
        # if hostname == "127.0.0.1:8000":
        #     return HttpResponseRedirect("http://localhost:8000" + path)
    
    # response
    def process_response(self, request, response):
        # if response.status_code == 204:
        #     response.status_code = 200

        return response