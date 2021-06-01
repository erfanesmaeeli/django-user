from django.db import models
from django.contrib.auth.models import AbstractUser
from django_jalali.db import models as jmodels


class User(AbstractUser):
	date_joined = jmodels.jDateTimeField(verbose_name="تاریخ عضویت", auto_now_add=True, null=True)
	date_updated = jmodels.jDateTimeField(verbose_name="آخرین به‌روزرسانی", auto_now=True, null=True)
	last_login = jmodels.jDateTimeField(verbose_name="آخرین ورود", null=True, blank=True)

	REQUIRED_FIELDS = []

	def get_date_joined(self):
		return self.date_joined.strftime("%Y/%m/%d - %H:%M")
	get_date_joined.short_description = 'تاریخ عضویت'

	def get_date_updated(self):
		return self.date_updated.strftime("%Y/%m/%d - %H:%M")
	get_date_updated.short_description = 'آخرین ویرایش'

	def get_last_login(self):
		return self.last_login.strftime("%Y/%m/%d - %H:%M")
	get_last_login.short_description = 'آخرین ورود'

	def __str__(self):
		return "%s - %s" % (self.username, self.get_full_name())

	class Meta:
		ordering = ['-date_joined']
		verbose_name = 'کاربر'
		verbose_name_plural = 'کاربران'