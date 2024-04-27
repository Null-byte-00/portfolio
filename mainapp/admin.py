from django.contrib import admin
from .models import SiteDescription, Media, Resume, Biography, Experience
# Register your models here.

admin.site.register(SiteDescription)
admin.site.register(Media)
admin.site.register(Resume)
admin.site.register(Biography)
admin.site.register(Experience)