from django.contrib import admin
from .models import Timer, Tasks, Sounds, Notification, Theme, BlockSite

# Register your models here.
admin.site.register(Timer)
admin.site.register(Tasks)
admin.site.register(Sounds)
admin.site.register(Notification)
admin.site.register(Theme)
admin.site.register(BlockSite)
