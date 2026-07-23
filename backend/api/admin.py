from django.contrib import admin
from .models import User, Artist, Album, Song, Scrobble

admin.site.register(User)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Scrobble)
