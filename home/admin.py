from django.contrib import admin

from home.models import District, Group, Region, Teacher

# Register your models here.


admin.site.register(Group)
admin.site.register(Region)
admin.site.register(District)
admin.site.register(Teacher)
