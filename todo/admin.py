from django.contrib import admin
from .models import Record
# Register your models here.


class RecordAdmin(admin.ModelAdmin):
    list_display = ('title', 'tasks_done')
    search_fields = ('title', )

admin.site.register(Record, RecordAdmin)