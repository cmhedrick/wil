from django.contrib import admin

from app_wil import models

for attr, item in [(attr, getattr(models, attr)) for attr in dir(models)]:
	if 'django.db.models.base.ModelBase'not in str(item.__class__):
		continue
	if attr == 'User':
		continue
	admin.site.register(item)
