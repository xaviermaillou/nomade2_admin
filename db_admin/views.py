from django.views.generic import ListView
from .models import Place

class PlaceListView(ListView):
    model = Place
    template_name = 'place_list.html'
    context_object_name = 'places'