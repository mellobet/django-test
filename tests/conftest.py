from datetime import date
from uuid import uuid4

import factory
import factory.fuzzy
import pytest
from core_app.models import Atendee, Event
from faker import Faker
from pytest_factoryboy import register
from rest_framework.test import APIClient

fake = Faker()


@pytest.fixture
def api_client():
    return APIClient()


@register
class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    id = uuid4()
    name = factory.Sequence(lambda n: f"event-{n}")
    description = factory.Sequence(lambda n: f"desc for event: event-{n}")
    event_topology = factory.fuzzy.FuzzyChoice(
        choices=[c[0] for c in Event.EVENT_TOPOLOGY_CHOICES]
    )


@register
class AtendeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Atendee

    id = uuid4()
    salutation = factory.fuzzy.FuzzyChoice(
        choices=[c[0] for c in Atendee.SALUTATION_CHOICES]
    )
    first_name = fake.name()
    last_name = fake.name()
    gender = factory.fuzzy.FuzzyChoice(choices=[c[0] for c in Atendee.GENDER_CHOICES])
    birth_date = date.today()

    @factory.post_generation
    def events(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for event in extracted:
                self.events.add(event)


# @pytest.fixture
# def make_specified_hosts(monkeypatch):
#     monkeypatch.setattr(MessageUtils, "send_command", lambda *args, **kwargs: None)

#     ac1 = AppCodeFactory(id="apc_1")
#     ac2 = AppCodeFactory(id="apc_2")
#     ac3 = AppCodeFactory(id="apc_3")

#     HostFactory(
#         fqdn="beispiel-1.example.local",
#         component_id="ec3b15dc-157d-420d-aae9-1f5a72b27eb0",
#         os_flavor="linux",
#         environment="production",
#         app_codes=(ac1,),
#     )
