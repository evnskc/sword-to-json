import pytest


@pytest.fixture
def sword():
    return "KJV.zip"


@pytest.fixture
def module():
    return "KJV"


@pytest.fixture
def name():
    return "King James Version"


@pytest.fixture
def abbreviation():
    return "KJV"
