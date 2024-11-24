import pytest


@pytest.mark.parametrize("Username,Password",
                         [
                             ("Selenium","Webdriver"),
                             ("Python","Pytest"),
                             ("Chrome","Firefox"),
                             ("API","WebAutomation")
                        ]
                        )
def test_login(Username,Password):
    print(Username)
    print(Password)