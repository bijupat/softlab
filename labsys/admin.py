from django.contrib import admin
from .models import *
from django.contrib.contenttypes.admin import GenericTabularInline


class NameInline(GenericTabularInline):
    model = Name
    max_num = 2
class TelecomInline(GenericTabularInline):
    model = Telecom
    max_num = 4
class AddressInline(GenericTabularInline):
    model = Address
    max_num = 2
class NoteInline(GenericTabularInline):
    model = Note
    max_num = 2
class PatientAdmin(admin.ModelAdmin):
    list_display =['id', 'get_usual_name','active', 'gender', 'age','get_mobile','get_email']
    inlines = [NameInline,TelecomInline,AddressInline,]
class ChargeItemDefinitionAdmin(admin.ModelAdmin):
    filter_horizontal = ['observations', 'specimentypes',  'includes', 'replaces']
    list_display =['id', 'title','alias', 'is_profile',  'outsourced_to', 'status']
    list_filter = ['status','is_profile', 'outsourced_to', 'heading']
    search_fields = ['title']
class PriceAdmin(admin.ModelAdmin):
    #filter_horizontal = ['chargeitemdef', 'specimentype, 'pricelist_included', 'includes', 'replaces')
    list_display =['id', 'chargeitemdef','pricelist', 'price']
class PractitionerAdmin(admin.ModelAdmin):
    # filter_horizontal = ['chargeitemdef', 'specimentype', 'pricelist_included', 'includes', 'replaces']
    list_display =['id', 'fullname','active', 'gender', 'birthDate']
    inlines = [NameInline,TelecomInline,AddressInline,]

class ObservationDefinitionAdmin(admin.ModelAdmin):
    list_display = ['id', 'test', 'method', 'unit', 'unit', 'tat', 'equipment', 'dept', 'loinc_code' ]
class EncounterAdmin(admin.ModelAdmin):
    list_display = ['id','sample_id', 'timedate','patient','practitioner', 'account', 'invoice','urgent']
    inlines = [NoteInline,]

class ObservationAdmin(admin.ModelAdmin):
    list_display = ['id', 'timedate', 'chargeitem', 'testfield','value', 'unit', 'high', 'low']
class ChargeItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'definitionCanonical', 'subject', 'context','occurrenceDateTime','enterer', 'priceOverride', 'account']
class PricelistAdmin(admin.ModelAdmin):
    # Controlling which fields are displayed and laid out
    fields = [('category', 'pricelist')]
    list_display = ['id', 'pricelist', 'category',]
class ServiceRequetAdmin(admin.ModelAdmin):
    filter_horizontal = [ 'specimentypes']
    list_display =['id',    'status', 'priority', 'practitioner', 'requester']
    list_filter = ['status','subject', 'requester', 'occurrenceDateTime']
    search_fields = ['title']
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
admin.site.register(SpecimenType)
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
admin.site.register(Sample)
admin.site.register(ServiceRequet, ServiceRequetAdmin)





