from django.contrib import admin

from enquetes.models import Enquete, Escolha


class EnqueteAdmin(admin.ModelAdmin):
    search_fields = ["texto"]
    list_filter = ["id"]
    list_display = ["id", "texto", "data_pub"]


class EscolhaAdmin(admin.ModelAdmin):
    list_display = ["id", "texto", "num_votos", "enquete"]


admin.site.register(Enquete, EnqueteAdmin)
admin.site.register(Escolha, EscolhaAdmin)
