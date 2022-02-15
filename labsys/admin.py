from django.contrib import admin
from .models import *

class PatientAdmin(admin.ModelAdmin):
    list_display =('id', 'active', 'gender')



class ChargeItemDefinitionAdmin(admin.ModelAdmin):
    filter_horizontal = ('observations_included','specimen', 'pricelist_included')

# Register your models here.
admin.site.register(Period)
admin.site.register(Name)
admin.site.register(Address)
admin.site.register(Contact)
admin.site.register(Practitioner)
admin.site.register(Note)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Telecom)
admin.site.register(Account)
admin.site.register(Encounter)
admin.site.register(Observation)
admin.site.register(User)
admin.site.register(Pricelist)
admin.site.register(Specimen)
admin.site.register(ObservationDefinition)
admin.site.register(TestCategory)
admin.site.register(QualifiedInterval)
#admin.site.register(DiagnosticReport)
admin.site.register(Organization)
admin.site.register(Invoice)
admin.site.register(PaymentReconciliation)
admin.site.register(ChargeItemDefinition, ChargeItemDefinitionAdmin)
admin.site.register(ChargeItem)
admin.site.register(Device)







