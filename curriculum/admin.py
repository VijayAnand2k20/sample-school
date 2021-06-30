from django.contrib import admin
from .models import Comment,Lesson,Reply,Standard,Subject

admin.site.register(Lesson)
admin.site.register(Standard)
admin.site.register(Subject)
admin.site.register(Comment)
admin.site.register(Reply)