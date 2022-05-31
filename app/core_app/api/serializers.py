from datetime import date

from core_app.models import Atendee, Event
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class AtendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atendee
        fields = "__all__"

    computed_age = serializers.SerializerMethodField()

    def get_computed_age(self, obj) -> bool:
        today = date.today()

        age = (
            today.year
            - obj.birth_date.year
            - ((today.month, today.day) < (obj.birth_date.month, obj.birth_date.day))
        )

        return age
