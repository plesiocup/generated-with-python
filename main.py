from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

from oai_create_image import Oai_create_image

app = FastAPI()

image_obj = Oai_create_image()

def create_image(title):
    # 画像を生成して画像をストレージに送って画像のリンクを返す
    image_url = image_obj.get_response(title)
    return image_url

class Item(BaseModel):
    movie_id: int # 映画id
    image_url: str = None # 画像URL
    title: str # タイトル
    description: str = None # 説明
    category: str # 映画カテゴリ
    play_time: int # 再生時間
    evaluation: int # 評価
    evaluated_count: int # 評価した人数
    release_year: int # 公開年


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/item/")
def create_item(item: Item):
    item.image_url = create_image(item.title)
    print(item.image_url)
    return item
    # return {"res": "ok",
    #         "映画id": item.movie_id, 
    #         "画像URL": item.image_url,
    #         "タイトル": item.title,
    #         "説明": item.description,
    #         "映画カテゴリ": item.category,
    #         "再生時間": item.play_time,
    #         "評価": item.evaluation,
    #         "評価した人数": item.evaluated_count,
    #         "公開年": item.release_year}

@app.post("/items/")
def create_items(items: List[Item]):
    new_items = []
    for item in items:
        item.image_url = create_image(item.title)
        new_items.append(item)
        # new_items.append({"res": "ok",
        #                   "映画id": item.movie_id, 
        #                   "画像URL": item.image_url,
        #                   "タイトル": item.title,
        #                   "説明": item.description,
        #                   "映画カテゴリ": item.category,
        #                   "再生時間": item.play_time,
        #                   "評価": item.evaluation,
        #                   "評価した人数": item.evaluated_count,
        #                   "公開年": item.release_year})
    return new_items
