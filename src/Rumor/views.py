from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import Rumor
# Create your views here.

class ResultRedirectView(View):
    def get(self, request, province = None, *args, **kwargs):

       obj = get_object_or_404(Rumor, province = province)
       obj_rumor = obj.rumor
       return HttpResponse("Visiting: {rumor}".format(rumor = obj_rumor))