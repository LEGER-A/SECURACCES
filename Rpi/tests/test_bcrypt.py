import pytest
from flask_bcrypt import Bcrypt


def test_bcrypt_password():

    bcrypt = Bcrypt()

    password = "1234"
    hashed = bcrypt.generate_password_hash(password)

    assert bcrypt.check_password_hash(hashed, password) is True

    assert bcrypt.check_password_hash(hashed,"mauvais_password") is False