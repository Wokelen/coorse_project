from django.contrib import admin

from ads.models import Ad, Comment
from users.models import User

# TODO здесь можно подкючить ваши модели к стандартной джанго-админке

admin.site.register(User)
