from django.contrib import admin
from .models import *


admin.site.site_header = 'Windows Factory'


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    search_fields = (
        'first_name',
        'surname',
    )
    list_display = (
        'first_name',
        'surname',
        'position',
        'department',
    )
    list_display_links = (
        'first_name',
        'surname',
    )


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
        'tax_id',
        'city',
        'street',
    )
    list_display = (
        'name',
        'tax_id',
        'city',
        'street',
    )


@admin.register(Window)
class WindowAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        '__str__',
        'type',
        'direction_of_opening',
        'acoustics',
        'thermics',
        'additional_vent',
        'security_lock',
        'rc2',
    )
    list_display_links = (
        'id',
        '__str__',
    )


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'offer_date',
        'client',
        'accepted',
        'employee',
    )
    search_fields = (
        'id',
        'client__name',
    )
    list_filter = (
        'accepted',
        'employee',
    )


@admin.register(Bom)
class BomAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'cost_of_materials',
        'cost_of_work',
    )


@admin.register(CategoryOfMaterial)
class CategoryOfMaterialAdmin(admin.ModelAdmin):
    pass


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'city',
        'street',
        'category',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'category',
    )


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'description',
        'unit',
        'quantity',
        'cost_per_unit',
        'total_cost',
    )
    list_filter = (
        'category',
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        '__str__',
        'offer',
        'status',
    )
    list_filter = (
        'status',
    )


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'supplier',
        'material',
        'quantity',
        'unit',
        'cost_per_unit',
        'total_cost',
    )
    search_fields = (
        'supplier',
    )


@admin.register(Api)
class ApiAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        '__str__',
        'description',
    )
