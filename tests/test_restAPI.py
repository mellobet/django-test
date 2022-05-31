import pytest
from django.forms.models import model_to_dict
from django.urls import reverse


@pytest.mark.django_db
@pytest.mark.parametrize(
    "reverse_url",
    [
        "atendee-list",
        "event-list",
    ],
)
def test_get_api_roots_ret_200(api_client, reverse_url):
    endpoint = reverse(reverse_url)

    response = api_client.get(endpoint, format="json")

    assert response.status_code == 200


@pytest.mark.django_db
def test_post_event_ret_201_and_matches(api_client, event_factory):
    endpoint = reverse("event-list")

    # Create the data in memory.
    data = model_to_dict(event_factory.build())

    # Persist via RestAPI.
    response = api_client.post(
        endpoint,
        data=data,
        format="json",
    )

    assert response.status_code == 201
