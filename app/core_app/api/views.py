from core_app.models import Atendee, Event
from rest_framework import mixins, viewsets

from .serializers import AtendeeSerializer, EventSerializer


class AtendeeSerializerViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,

    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):

    serializer_class = AtendeeSerializer
    queryset = Atendee.objects.all().order_by("id")


class EventSerializerViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,

    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):

    serializer_class = EventSerializer
    queryset = Event.objects.all().order_by("id")
