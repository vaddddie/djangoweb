from django.contrib import admin
from .models import Status, Mode, CoolerStatistics, PumpStatistics, LightStatistics


admin.site.register(Status)
admin.site.register(Mode)
admin.site.register(CoolerStatistics)
admin.site.register(PumpStatistics)
admin.site.register(LightStatistics)
