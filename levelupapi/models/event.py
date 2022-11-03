from django.db import models


class Event(models.Model):

    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    organizer = models.ForeignKey('Gamer', on_delete=models.CASCADE)
    description = models.CharField(max_length=155)
    date = models.DateField()
    time = models.TimeField()
