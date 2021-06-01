from django.contrib import admin
from django.contrib import messages


@admin.action(description='فعال کردن کار‌بر‌های انتخاب شده')
def make_active(modeladmin, request, queryset):
    updated = queryset.update(is_active=True)
    messages.success(request, f'وضعیت {updated} کاربر به فعال تغییر یافت.')


@admin.action(description='غیرفعال کردن کار‌بر‌های انتخاب شده')
def make_deactive(modeladmin, request, queryset):
    updated = queryset.update(is_active=False)
    messages.info(request, f'وضعیت {updated} کاربر به غیرفعال تغییر یافت.')
