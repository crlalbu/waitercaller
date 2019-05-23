MOCK_USERS = {'carlos@gmail.com': '12345'}

class MockDBHelper:

    def get_user(self, email):
        if email in MOCK_USERS:
            return MOCK_USERS[email]
        return None