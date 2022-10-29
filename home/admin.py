from django.contrib import admin
from . models import *
# Register your models here.


###class contactdesc(admin.ModelAdmin):
    #list_display = ('name','email')

admin.site.register(Contact)