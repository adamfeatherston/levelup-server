"""View module for handling requests about event types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event
from levelupapi.models import Game
from levelupapi.models import Gamer


class EventView(ViewSet):
    """Level up event types view"""

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        organizer = Gamer.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.data["gameId"])

        event = Event.objects.create(
            description=request.data["description"],
            date=request.data["date"],
            time=request.data["time"],
            organizer=organizer,
            game=game
        )
        serializer = EventSerializer(event)
        return Response(serializer.data)
    
    def update(self, request, pk):

        event = Event.objects.get(pk=pk)
        event.description = request.data["description"]
        event.date = request.data["date"]
        event.time = request.data["time"]

        game = Game.objects.get(pk=request.data["game"])
        event.game = game
        event.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk):
        """Handle GET requests for single event type

        Returns:
            Response -- JSON serialized event type
        """

        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def destroy(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        """Handle GET requests to get all event types

        Returns:
            Response -- JSON serialized list of event types
        """

        events =  []
        events = Event.objects.all()
        if "game" in request.query_params:
            events = events.filter(game_id=request.query_params['game'])
            if request.query_params['game'] == "all":
                pass

        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ('id', 'title')

class GamerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gamer
        fields = ('id', 'full_name')

class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for event types
    """

    game = GameSerializer(many=False)
    organizer = GamerSerializer(many=False)

    class Meta:
        model = Event
        fields = ('id', 'description', 'date', 'time', 'game', 'organizer')   