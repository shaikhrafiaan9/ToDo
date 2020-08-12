from django.contrib import admin
from basictodo.models import Todo
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Todo,TodoAdmin)
