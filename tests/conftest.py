import os

import django
from django.test.utils import override_settings
import pytest


def pytest_configure():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.settings")
    django.setup()


@pytest.fixture(scope="session", autouse=True)
def custom_settings(tmpdir_factory):
    overrides = override_settings(MEDIA_ROOT=str(tmpdir_factory.mktemp("media")))
    overrides.enable()