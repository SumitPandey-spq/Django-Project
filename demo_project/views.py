from django.http import HttpResponse
def homepage(request):
    return HttpResponse('<h1>First Django Project</h1>')