from .models import *

#To order fruits by name through the project

def orderby_fruits(request):
    fruits = Fruits.objects.all().order_by('name')
    return {'fruits':fruits}