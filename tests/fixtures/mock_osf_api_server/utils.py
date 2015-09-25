from decorator import decorator
from flask import request
from tests.fixtures.mock_osf_api_server.common import Session
from tests.fixtures.mock_osf_api_server.models import User
from flask import jsonify

session = Session()

# helpers
@decorator
def must_be_logged_in(func, *args, **kwargs):
    try:
        get_user()
    except:
        print('user not logged in: {}'.format(request.headers.get('Authorization','NO AUTHORIZATION HEADER')))
        return jsonify({'FAIL':'user not logged in'})

    return func(*args, **kwargs)

def save(item=None):
    if item is not None:
        session.add(item)
    session.commit()

def get_user():
    auth_header = request.headers['Authorization']
    user_id = auth_header.split(' ')[1]

    user = session.query(User).filter(User.id == user_id).one()
    return user
