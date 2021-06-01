from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AbstractUserAdmin
from django.contrib.auth.models import Group
from .models import User
from .utils import make_active, make_deactive

admin.site.unregister(Group)  # if you want to unregister group in django admin

@admin.register(User)
class UserAdmin(AbstractUserAdmin):
	list_display = ['username', 'first_name', 'last_name', 'email', \
		 'get_date_joined', 'is_active', 'is_superuser']
	list_filter = ['is_active', 'is_superuser']
	search_fields = ['username', 'first_name', 'last_name', 'email']
	readonly_fields = ['date_joined', 'date_updated', 'last_login']
	list_display_links = ['username']
	list_editable = []
	ordering = []
	list_per_page = 100
	actions = [make_active, make_deactive]

	fieldsets = (
		('اطلاعات ورود', {
			'fields': ('username', 'password')
		}),

		('اطلاعات شخصی', {
			'classes': ('grp-collapse grp-closed',),
			'fields': ('first_name', 'last_name', 'email')
		}),

		('دسترسی‌ها', {
			'classes': ('collapse', 'close'),
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions'
            )
        }),

        ('تاریخ‌های مهم', {'fields': ('date_joined', 'date_updated', 'last_login')})
	)

	add_fieldsets = (
		('اطلاعات ورود', {
			'fields': ('username', 'password1', 'password2')
		}),

		('اطلاعات شخصی', {
			'fields': ('first_name', 'last_name', 'email')
		}),

		('دسترسی‌ها', {
			'classes': ('collapse', 'close'),
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions'
            )
        })
	)
