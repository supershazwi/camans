from django.contrib import admin

from .models import Vendor, Worker, Table, Field, Role, PermissionPrivilege

admin.site.register(Vendor)
admin.site.register(Worker)
admin.site.register(Table)
admin.site.register(Field)
admin.site.register(Role)
admin.site.register(PermissionPrivilege)