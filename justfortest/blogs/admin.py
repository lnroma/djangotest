from django.contrib import admin
from models import Post,PostAdmin,Navigation,NavigationAdmin

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Navigation,NavigationAdmin)
