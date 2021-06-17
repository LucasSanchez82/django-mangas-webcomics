from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item

# Create your views here.
def index(request):
    items = Item.objects.all()
    data = {'items': items}
    return render(request, 'home_mangas_webcomics/index.html', data)