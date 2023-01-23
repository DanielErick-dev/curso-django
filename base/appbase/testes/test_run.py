from django.test import Client
from django.urls import reverse

from base.django_assertions import assert_contains
import pytest

@pytest.fixture
def resp(client: Client):
    resp = client.get(reverse('index'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, f'<title>Python Pro</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("index")}">Daniel Pro</a>')


