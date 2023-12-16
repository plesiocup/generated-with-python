from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    movie_id: int # 映画id
    image_url: str # 画像URL
    title: str # タイトル
    description: str # 説明
    category: str # 映画カテゴリ
    play_time: int # 再生時間
    evaluation: int # 評価
    evaluated_count: int # 評価した人数
    release_year: int # 公開年

class User(BaseModel):
    user_id: int
    name: str


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/item/")
def create_item(item: Item):
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
def create_item(items: List[Item]):
    new_items = []
    for item in items:
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
    return new_users

