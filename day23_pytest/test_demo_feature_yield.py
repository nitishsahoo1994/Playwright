import pytest

@pytest.fixture(scope='session', autouse=True)
def setup():
    print("setup browser....")

    yield
    print("close browser")

def test_one():
    print("this is my test one")

def test_two():
    print("this is my test two")


def test_three():
    print("this is my test three")