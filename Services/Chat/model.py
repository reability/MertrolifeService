from bson.objectid import ObjectId


class ChatRoom:
    def __init__(self, db):
        self.db = db
        self.collection = self.db['CHATROOM']

    async def fetchChatRoom(self, user_id):
        query = {"user_id": user_id}
        chat_room = await self.collection.find_one(query)
        return chat_room

    async def create(self, user_id):
        result = await self.collection.insert_one(
            {
                "user_id": user_id,
                "messages": []
            }
        )
        return result

    async def update(self, user_id, message):
        query = {"user_id": user_id}
        chat_room = await self.collection.find_one(query)
        result = await self.collection.update_one(query, {"$set": {"messages": chat_room["messages"].append(message)}})
        return result

