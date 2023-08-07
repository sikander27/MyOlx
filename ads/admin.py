from django.contrib import admin
from django.apps import apps
from .models import Ad, Spec, Category

app = apps.get_app_config('ads')

exclude_models = ()

# for model_name, model in app.models.items():
#     if model_name.lower() not in exclude_models:
#         admin.site.register(model)


class SpecInline(admin.StackedInline):
    model = Ad
    verbose_name = "Specification"
    verbose_name_plural = "Specifications"
    classes = ("collapse",)
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
    # inlines = (SpecInline,)


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    exclude = ('deleted',)
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('title', 'price', 'sold')
    # inlines = (SpecInline,)