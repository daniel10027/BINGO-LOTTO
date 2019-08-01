from django.contrib import admin
from .models import Post
from .models import Tiquet
from .models import Lotterie
from .models import Resultat

admin.site.register(Post)
admin.site.register(Tiquet)
admin.site.register(Lotterie)
admin.site.register(Resultat)