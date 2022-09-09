from urllib import response
import requests
from api.user import usersEndPoint
from utilities.user_utilities import UserUtilities

users = usersEndPoint()


def test_create_user():
    
    #Preconditions
    user = UserUtilities()

    #test
    response = users.create_user(user.user_as_json)
    assert response.status_code == 200
