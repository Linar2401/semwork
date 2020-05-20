from django.contrib import admin

# Register your models here.
from utils.models import *

admin.site.register(Post)
admin.site.register(CustomUser)