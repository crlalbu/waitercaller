import datetime
MOCK_USERS = [{"email":'carlos@gmail.com', "salt":
                "mbD//+Sve3b9EzWSivb42ka6JjI=", "hashed": 
                'b02f4e29ca87c5971f7c54cb65c4b4f1f6faecf0c1b47f37db57a754f077565992e7b3ea027a509e6db10612fbe932b6f71b267bcb21595e069cb9d9dc30d761'}]

MOCK_TABLES = [{"_id": "1", "number": "1", "owner": "carlos@gmail.com", "url": "mockurl"}]


MOCK_REQUESTS = [{"_id": 1, "table_number": "1", "table_id": "1", "time": datetime.datetime.now()}]

class MockDBHelper:

    def get_user(self, email):
        user = [x for x in MOCK_USERS if x.get("email") == email]
        if user:
            return user[0]
        return None

    def add_user(self, email, salt, hashed):
        MOCK_USERS.append({"email": email, "salt": salt, "hashed": hashed})

    def add_table(self, number, owner):
        MOCK_TABLES.append({"_id": number, "number": number, "owner": owner})
        return number

    def update_table(self, _id, url):
        for table in MOCK_TABLES:
            if table.get("_id") == _id:
                table["url"] = url
                break

    def get_tables(self, owner_id):
        return MOCK_TABLES
    
    def delete_table(self, table_id):
        for i, table in enumerate(MOCK_TABLES):
            if table.get("_id") == table_id:
                del MOCK_TABLES[i]
            break

    def add_table(self, number, owner):
        MOCK_TABLES.append(
            {"_id": str(number), "number": number, "owner": owner}
        )
        return number

    def get_requests(self, owner_id):
        return MOCK_REQUESTS

    def delete_request(self, request_id):
        for i, request in enumerate(MOCK_REQUESTS):
            if request.get("_id") == int(request_id):
                del MOCK_REQUESTS[i]
                break
        
        

