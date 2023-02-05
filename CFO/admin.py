
# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(TaskMaster)
admin.site.register(RecurrenceMaster)
admin.site.register(COEMaster)
admin.site.register(RoleMaster)
admin.site.register(UserMaster)
