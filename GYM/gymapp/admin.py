from django.contrib import admin
from .models import Gym
from .models import Members
from .models import Trainer
from .models import abc
from .models import Payment

# Register your models here.



admin.site.register(Gym)
admin.site.register(Members)
admin.site.register(Trainer)
admin.site.register(abc)
admin.site.register(Payment)