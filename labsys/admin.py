from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Period)
admin.site.register(Name)
admin.site.register(Address)
admin.site.register(Contact)
admin.site.register(Practitioner)
admin.site.register(Note)
admin.site.register(Patient)
admin.site.register(Telecom)

