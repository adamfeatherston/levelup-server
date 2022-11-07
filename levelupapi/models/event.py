from django.db import models



class Event(models.Model):

    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='game')
    organizer = models.ForeignKey('Gamer', on_delete=models.CASCADE, related_name='gamer')
    description = models.CharField(max_length=155)
    date = models.DateField()
    time = models.TimeField()
