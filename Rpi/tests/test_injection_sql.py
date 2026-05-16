import  pytest
from app import check_uid


def test_injection_refuse():

    assert check_uid("OR 1=1 --") == "deny"


