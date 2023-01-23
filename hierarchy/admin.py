from django.contrib import admin
from .models import Worker


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ["surname", "name", "patronymic", "position", "boss"]
    list_editable = ["position"]



