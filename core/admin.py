"""
Django admin customization.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core.models import Compra, ItensCompra, Produto, User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ["id"]
    list_display = ["email", "name"]
    search_fields = ["email", "name"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("name", "foto", "passage_id")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
        (_("Groups"), {"fields": ("groups",)}),
        (_("User Permissions"), {"fields": ("user_permissions",)}),
    )
    readonly_fields = ["last_login"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "name",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


# @admin.register(ItensCompra)
class ItensCompraInline(admin.TabularInline):
    model = ItensCompra
    extra = 1

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('user', 'status')
    search_fields = ('user', 'status')
    list_filter = ('user', 'status')
    ordering = ('user', 'status')
    list_per_page = 25
    inlines = [ItensCompraInline]

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tier', 'caminho', 'elemento',)
    search_fields = ('nome', 'tier', 'caminho', 'elemento',)
    list_filter = ('nome', 'tier', 'caminho', 'elemento',)
    ordering = ('nome',)
    list_per_page = 10