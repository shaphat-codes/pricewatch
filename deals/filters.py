from . models import *
import django_filters

class BroadbandFilter(django_filters.FilterSet):
    class Meta:
        model = Broadband
        fields = ['sub', 'company', 'speed', ]