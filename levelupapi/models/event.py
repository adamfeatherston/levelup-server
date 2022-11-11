from django.db import models



class Event(models.Model):

    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='events')
    organizer = models.ForeignKey('Gamer', on_delete=models.CASCADE, related_name='gamer')
    description = models.CharField(max_length=155)
    date = models.DateField()
    time = models.TimeField()
    attendees= models.ManyToManyField("Gamer", through="EventGamer", related_name="events")

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value
