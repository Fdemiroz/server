import os
from dotenv import load_dotenv
load_dotenv()

user_id = os.environ["ID"]

def get_user_id(id):
	return id

def get_number():
	return True

def test_check_user_id():
	assert get_user_id(user_id) == "1234"
	
def test_check_number():
	assert get_number() is True