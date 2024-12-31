from django.contrib import admin
# Register your models here.





from .models import Books , Category

admin.site.register(Books)
admin.site.register(Category)

