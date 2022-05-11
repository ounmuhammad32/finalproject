import logging

from app import db
from app.db.models import User, Transaction


def test_add_user(application, client):
    log = logging.getLogger("myApp")
    with application.app_context():
        # create a new user:
        user = User('test@test', 'testtest')
        db.session.add(user)
        db.session.commit()
        assert db.session.query(User).count() == 1
        assert db.session.query(Transaction).count() == 0
        user = User.query.filter_by(email='test@test').first()
        log.info(user)
        # asserting that the user retrieved is correct
        assert user.email == 'test@test'
        user.transactions = [
            Transaction("3000", "CREDIT"),
            Transaction("4000", "DEBIT"),
            Transaction("1700", "DEBIT"),

        ]
        # commit is what saves the transactions
        db.session.commit()

        response = client.get('/transactions/current')
        assert response.data == b'8700'
        assert db.session.query(Transaction).count() == 3
        # checking cascade delete
        db.session.delete(user)