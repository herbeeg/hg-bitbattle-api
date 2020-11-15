import pytest

from pathlib import Path

from app.main import app, db, Activation, User

TEST_DB = 'test.db'

class TestMainCase:
    @pytest.fixture
    def client(self):
        BASE_DIR = Path(__file__).resolve().parent.parent

        app.config['TESTING'] = True
        app.config['DATABASE'] = BASE_DIR.joinpath(TEST_DB)
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{BASE_DIR.joinpath(TEST_DB)}'

        db.create_all()

        with app.test_client(self) as client:
            yield client

        db.drop_all()

    def testActivationKeyGeneration(self, client):
        assert True == False