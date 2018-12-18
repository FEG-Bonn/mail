# Create your views here.
from django.http import HttpResponse


def Index(request):
    return HttpResponse("Hi")
