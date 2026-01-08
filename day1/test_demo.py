import pytest


@pytest.fixture
def setup(scope="function"):
    print("setup browser...")


def test_one(setup):
    print("this is my test one")


def test_two(setup):
    print("this is test two")


def test_three(setup):
    print("this is test three")
