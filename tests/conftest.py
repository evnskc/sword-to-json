from pathlib import Path

import pytest


@pytest.fixture
def sword():
    return Path(__file__).resolve().parent.parent.joinpath('KJV.zip')


@pytest.fixture
def module():
    return "KJV"
