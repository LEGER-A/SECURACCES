import  pytest
from app import check_uid


def test_uid_autorise():

    assert check_uid("uid1") == "allow"


def test_uid_refuse():

    assert check_uid("uid5") == "deny"