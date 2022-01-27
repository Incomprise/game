from django.db import models

class Weapon(models.Model):
    name = models.CharField(max_length=50)
    damage = models.IntegerField(default=0)
    icon = models.TextField()

    def __str__(self):
        return self.name

class Armor(models.Model):
    name = models.CharField(max_length=50)
    defense = models.IntegerField()
    icon = models.TextField()

class Spell(models.Model):
    name = models.CharField(max_length=50)
    mana = models.IntegerField(default=0)
    damage = models.IntegerField(default=0)

class CharacterType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    icon = models.TextField()
    
class Character(models.Model):
    hp = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)
    armor = models.ForeignKey(Armor, on_delete=models.CASCADE)
    mana = models.IntegerField(default=0)
    spell = models.ForeignKey(Spell, on_delete=models.CASCADE)
    character_type = models.ForeignKey(CharacterType, on_delete=models.CASCADE)