from django.contrib import admin

from base.models import Article, Author

# Register your models here.
admin.site.register([Article, Author])