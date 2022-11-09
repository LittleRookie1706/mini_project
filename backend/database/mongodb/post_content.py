from fastapi import HTTPException

from .base import dtbs

db1=dtbs['news_data']
db2=dtbs['load_news_data']

news_count = db1.count_documents({})

class PostContentDB:

    def get(self, url: str):
        data = db1.find_one({"name": url })
        print(data)
        if data:
            return data
        raise HTTPException(status_code=404, detail="Post not found")
        

class MinimumPostContentDB:

    def list(self, pos_list: list):
        data = db2.find({"position": { '$in': pos_list }  })
        result = [dat for dat in data]
        return result

    def get_slideshow(self):
        pass

    def get_most_views(self):
        pass

    def get_page(self, page: int):
        pass