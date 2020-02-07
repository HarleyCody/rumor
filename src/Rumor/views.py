from django.core.paginator import Paginator, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from src.RumorValidator import settings
from django.utils import timezone
from django.views import View
from .models import Rumor
# Create your views here.

def no_rumor_view(request, name):
    time = timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S")
    p = "截止到:" + time + ", " + name + "无谣言传播"
    return render(request, 'Rumor/404.html', {'p': p})

def rumors_view(request, context = None):
    if context["keywords"]:
        context["results"] = Rumor.objects.filter(province= context["province"],
                                        rumor__icontains= context["keywords"]).order_by("-timestamp")

    paginator = Paginator(context["results"], 10)
    page = request.GET.get('page')

    try:
        context["results"] = paginator.page(page)
    except PageNotAnInteger:
        context["results"] = paginator.page(1)

    return render(request, "Rumor/result.html", context)

class HomeView(View):
    context = {
        "provinces" :settings.PROVINCE_DICTIONARYS
    }
    def get(self, request, *args, **kwargs):
        return render(request, "Rumor/home.html", self.context)

    def post(self, request, *args, **kwargs):
        province = request.POST.get("province")

        return redirect(reverse('results', kwargs={'province' : province}))

class ResultRedirectView(View):
    context = {
        "province"  :None,
        "results"   :None,
        "title"     :None,
        "keywords"  :None,
    }
    def get(self, request, province = None, *args, **kwargs):
        self.context["province"] = province
        self.context["name"] = settings.PROVINCE_DICTIONARYS[province]
        self.context["title"] = "Rumor results in " + self.context["name"]
        #not valid province in China 404
        if province not in settings.PROVINCE_DICTIONARYS:
            return get_object_or_404(Rumor, province = province)

        self.context["keywords"] = request.GET.get("keywords")
        objs = Rumor.objects.filter(province = province).order_by("-timestamp")
        self.context["results"] = objs

        # No results
        if(len(objs) == 0):
            return no_rumor_view(request, self.context["name"])

        # return results
        return rumors_view(request, self.context)

    def post(self, request, *args, **kwargs):
        self.context["keyword"] = request.POST.post('keyword')
        return rumors_view(request, self.context)