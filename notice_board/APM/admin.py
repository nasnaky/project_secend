from django.contrib import admin
from .models import User, FreeNoticeBoard, StoryNoticeBoard, Inquiry, Notification, \
    suggestion_story, suggestion_free, Comment_Free, Comment_Story, Comment_ip

admin.site.register(User)
admin.site.register(FreeNoticeBoard)
admin.site.register(StoryNoticeBoard)
admin.site.register(Inquiry)
admin.site.register(Notification)
admin.site.register(suggestion_story)
admin.site.register(suggestion_free)
admin.site.register(Comment_Free)
admin.site.register(Comment_Story)
admin.site.register(Comment_ip)
