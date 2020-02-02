from django.contrib import admin
from .models import Rumor
from django.contrib.auth.models import Group
#Register your models here.


class RegionRumorFilter(admin.SimpleListFilter):
    title = 'Region'
    parameter_name = 'rumor'

    def lookups(self, request, admin):
        return [('inRegion','In Region')]

    def queryset(self, request, queryset):
        region = Group.objects.get(user=request.user).name
        if region == 'CN':
            return queryset.all()
        if self.value() == 'inRegion':
            return queryset.filter(province=region)
        return queryset.all()

class RumorAdmin(admin.ModelAdmin):
    list_display    = ('rumor', 'isReal', 'province')
    search_fields   = ('rumor', 'isReal', 'province')
    list_filter     = (RegionRumorFilter,)
    list_per_page   = 20

admin.site.register(Rumor, RumorAdmin)