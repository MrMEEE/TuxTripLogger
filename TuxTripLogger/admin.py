from django.contrib import admin
from TuxTripLogger.models import log,location
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(log, AuthorAdmin)
admin.site.register(location, AuthorAdmin)

