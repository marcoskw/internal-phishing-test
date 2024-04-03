from django.contrib import admin
from . models import Click


class ClickAdmin(admin.ModelAdmin):
    list_display = (
                    'id',
                    'ip_address',
                    'machine_name',
                    'username',
                    'clicked_at',
    )

    list_display_links = ('id',
                          'ip_address',
                          'machine_name',

    )

admin.site.register(Click, ClickAdmin)