from django.shortcuts import HttpResponse
from .models import Category

# Create your views here.
def index(request):
    categories = Category.objects.all()
    return HttpResponse(' '.join([str(category) + '<br>' for category in categories]))
