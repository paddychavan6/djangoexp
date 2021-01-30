from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account,logimage,modelfile


class AccountAdmin(UserAdmin):
    list_display=('email','username','firstname','is_admin')
    search_fields=('email','username')
    # readonly_fields=('DOB',)

    filter_horizontal=()
    list_filter=()
    fieldsets=()

admin.site.register(Account,AccountAdmin)
admin.site.register(logimage)
admin.site.register(modelfile)