from django.contrib import admin
from .models import Category, Board, Tag, Thread, Post, Attachment, ApplicationUser

# Register your models here.


admin.site.register(Category)
admin.site.register(Board)
admin.site.register(Tag)
admin.site.register(Thread)
admin.site.register(Post)
admin.site.register(Attachment)
admin.site.register(ApplicationUser)

#так?