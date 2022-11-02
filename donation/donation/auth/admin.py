from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from project.models import Usuario
from donation.mailer import send_email


class CustomUserAdmin(UserAdmin):
    def save_model(self, request, obj, form, change):
        if 'is_active' in form.changed_data and obj.is_active:
            # active state was changed and the user is now active,
            # send email telling the user their account was activated
            send_email(obj.email, 1, {
                'user': obj
            })

        super().save_model(request, obj, form, change)


admin.site.unregister(Usuario)
admin.site.register(Usuario, CustomUserAdmin)
