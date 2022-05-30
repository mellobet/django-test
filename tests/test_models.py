import pytest


@pytest.mark.django_db
def test_event_str_representation_matches(event_factory):

    instance_details = dict(
        name="foobar",
    )

    event = event_factory.create(**instance_details)

    assert str(event) == instance_details["name"]


@pytest.mark.django_db
def test_atendee_str_representation_matches(atendee_factory):

    instance_details = dict(
        first_name="foo",
        last_name="bar",
        salutation="MS",
        gender="F",
    )

    atendee = atendee_factory.create(**instance_details)

    assert (
        str(atendee) == f'{instance_details["salutation"]}'
        f' {instance_details["first_name"]}'
        f' {instance_details["last_name"]}'
    )

    assert atendee.gender == "F"
