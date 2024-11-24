import pytest


@pytest.mark.smoke
def test_login():
    print("login Success")


@pytest.mark.skip
def test_addProduct():
    print("product added successfully")


@pytest.mark.smoke
def test_logout():
    print("logout successfully")
