from django.http import HttpResponse

# Create your views here.
def index(request):
    print("IN VIEW FUNCTION")
    return HttpResponse("Index Called")

