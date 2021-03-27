from bson.objectid import ObjectId


class PointOfInterest:
    def __init__(self, db):
        self.db = db
        self.collection = self.db['POI']

    async def fetchPOIInfo(self, poi_id):
        query = {"_id": ObjectId(poi_id)}
        poi = await self.collection.find_one(query)
        return poi

    async def fetchPOIAll(self):
        pois = await self.collection.find().to_list(length=100)
        return pois

    async def create(self, type, title, content):
        result = await self.collection.insert_one(
            {
                "poi_type": type,
                "title": title,
                "content": content
            }
        )
        return result
