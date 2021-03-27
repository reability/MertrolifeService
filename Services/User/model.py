from bson.objectid import ObjectId


class User:
    def __init__(self, db):
        self.db = db
        self.collection = self.db["USERS"]

    async def fetchUserInfo(self, user_id):
        query = {"_id": ObjectId(user_id)}
        user = await self.collection.find_one(query)
        return user

    async def create(self, fullname, login, password):
        result = await self.collection.insert_one(
            {
                "name": fullname,
                "login": login,
                "password": password
            }
        )

        return result