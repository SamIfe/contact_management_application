from datetime import datetime
from bson import ObjectId
import bcrypt

class User:
    def __init__(self, username, email, password):
        self._id = ObjectId()
        self._username = username
        self._email = email
        self.password_hash = self._hash_password(password)
        self.last_login = None

    def _hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

