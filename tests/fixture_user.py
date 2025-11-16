import pytest


@pytest.fixture
def user_client():
    from rest_framework.test import APIClient

    client = APIClient()
    return client


@pytest.fixture
def password():
    return '1234567'


@pytest.fixture
def user(django_user_model, password):
    return django_user_model.objects.create_user(
        username='TestUser',
        password=password
    )


@pytest.fixture
def another_user(django_user_model, password):
    return django_user_model.objects.create_user(
        username='TestUser2',
        password=password
    )

