from django.utils.deprecation import MiddlewareMixin


class MyMiddle(MiddlewareMixin):
    def process_request(self,request):
        remote_addr=request.META['REMOTE_ADDR']
