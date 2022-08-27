from django.contrib import admin
from clientes.models import User

class AdminUser(admin.ModelAdmin):
    pass
    
admin.site.register(User,AdminUser)
