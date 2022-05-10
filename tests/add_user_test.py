import logging

from app import db
from app.db.models import User, Transaction


def test_add_user(application):
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
            Transaction("2000", "CREDIT"),
            Transaction("2500", "DEBIT")
        ]
        # commit is what saves the transactions
        db.session.commit()
        assert db.session.query(Transaction).count() == 2
        transaction1 = Transaction.query.filter_by(amount='2000').first()
        assert transaction1.type == "CREDIT"
        transaction2 = Transaction.query.filter_by(amount='2500').first()
        assert transaction2.type == "DEBIT"
        assert db.session.query(Transaction).count() == 2
        # checking cascade delete
        db.session.delete(user)
        # check to see if the delete worked:
        assert db.session.query(User).count() == 0