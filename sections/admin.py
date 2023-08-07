from django.contrib import admin
from django.apps import apps

app = apps.get_app_config('sections')

exclude_models = ('user_user_permissions','user_groups')

# for model_name, model in app.models.items():
#     if model_name.lower() not in exclude_models:
#         admin.site.register(model)