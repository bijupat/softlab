from django.contrib import admin
from .models import *

class PatientAdmin(admin.ModelAdmin):
    list_display =('id', 'get_usual_name','active', 'gender', 'age','get_mobile')
class ChargeItemDefinitionAdmin(admin.ModelAdmin):
    # filter_horizontal = ('observations', 'specimen',  'includes', 'replaces')
    list_display =('id', 'title','alias', 'is_profile',  'outsourced_to', 'status')
    list_filter = ('status','is_profile', 'outsourced_to', 'heading')
    search_fields = ['title']
class PriceAdmin(admin.ModelAdmin):
    # filter_horizontal = ('chargeitemdef', 'specimen', 'pricelist_included', 'includes', 'replaces')
    list_display =('id', 'chargeitemdef','pricelist', 'price')
class PractitionerAdmin(admin.ModelAdmin):
    # filter_horizontal = ('chargeitemdef', 'specimen', 'pricelist_included', 'includes', 'replaces')
    list_display =('id', 'fullname','active', 'gender', 'birthDate')
class ObservationDefinitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'test', 'method', 'unit', 'specimen', 'tat', 'equipment', 'dept', 'loinc_code' )
class EncounterAdmin(admin.ModelAdmin):
    list_display = ('id', 'timedate','patient','practitioner', 'account', 'invoice','urgent')
class ObservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'timedate', 'chargeitem', 'testfield','value', 'unit', 'high', 'low')
class ChargeItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'definitionCanonical', 'subject', 'context','occurrenceDateTime','enterer', 'priceOverride', 'account')
class PricelistAdmin(admin.ModelAdmin):
    # Controlling which fields are displayed and laid out
    fields = [('category', 'pricelist')]
    list_display = ('id', 'pricelist', 'category',)

# Register your models here.
admin.site.register(Period)
admin.site.register(Name)
admin.site.register(Address)
admin.site.register(Contact)
admin.site.register(Practitioner, PractitionerAdmin)
admin.site.register(Note)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Telecom)
admin.site.register(Account)
admin.site.register(Encounter, EncounterAdmin)
admin.site.register(Observation, ObservationAdmin)
admin.site.register(User)
admin.site.register(Pricelist, PricelistAdmin)
admin.site.register(Specimen)
admin.site.register(ObservationDefinition, ObservationDefinitionAdmin)
admin.site.register(TestCategory)
admin.site.register(QualifiedInterval)
admin.site.register(DiagnosticReport)
admin.site.register(Organization)
admin.site.register(Invoice)
admin.site.register(PaymentReconciliation)
admin.site.register(ChargeItemDefinition, ChargeItemDefinitionAdmin)
admin.site.register(ChargeItem, ChargeItemAdmin)
admin.site.register(Device)
admin.site.register(Headings)
admin.site.register(Appointment)
admin.site.register(Price, PriceAdmin)





