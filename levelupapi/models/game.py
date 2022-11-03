from django.db import models


class Game(models.Model):

    game_type = models.ForeignKey('GameType', on_delete=models.CASCADE)
    gamer = models.ForeignKey('Gamer', on_delete=models.CASCADE)
    title = models.CharField(max_length=35)
    maker = models.CharField(max_length=25)
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()