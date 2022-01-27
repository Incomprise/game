from django.contrib import admin

from .models import Weapon
from .models import Armor
from .models import Spell
from .models import CharacterType
from .models import Character


admin.site.register(Weapon)
admin.site.register(Armor)
admin.site.register(Spell)
admin.site.register(CharacterType)
admin.site.register(Character)
