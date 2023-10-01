from django.contrib import admin

# Register your models here.
from .models import Skole, Fag, Skoleklasse, Eksamen, Personale, WishDates

admin.site.register(Skole)
admin.site.register(Fag)
admin.site.register(Skoleklasse)
admin.site.register(Eksamen)
admin.site.register(Personale)
admin.site.register(WishDates)