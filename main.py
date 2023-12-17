from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

import requests

from oai_create_image import Oai_create_image
from oai_create_discription import Oai_create_discription

app = FastAPI()

image_obj = Oai_create_image()
description_obj = Oai_create_discription()

class Item(BaseModel):
    movie_id: int # 映画id
    image_url: str = None # 画像URL
    title: str = "Spirited Away" # タイトル
    description: str = None # 説明
    category: str # 映画カテゴリ
    play_time: int # 再生時間
    evaluation: float # 評価
    evaluated_count: int # 評価した人数
    release_year: int # 公開年


def item_remold(item):
    count = 3
    while count > 0:
        item.description = create_discription(item.title)
        if (item.description == "error!"):
            print("ERROR (create_discription)!")
            count -= 1
        else:
            # item.image_url = create_image(item.title) # タイトルよりも生成した説明文をもとに画像を作成した方がいい気がした。
            item.image_url = create_image(item.description)

            if (item.image_url == "error!"):
                print("ERROR (create_image)!")
                count -= 1
            elif (item.image_url == "discription error"):
                print("ERROR! disciption remold")
                count -= 1
            else :
                print("ERRORなし!!")
                break

    # item.description = create_discription(item.title)
    # # item.image_url = create_image(item.title) # タイトルよりも生成した説明文をもとに画像を作成した方がいい気がした。
    # item.image_url = create_image(item.description)

    return item

def create_discription(title):
    description = description_obj.get_response(title)
    return description

def create_image(title):
    image_url = image_obj.get_response(title)
    return image_url

def request_createData(item):
    request_url = ""
    requests.post(request_url, data=item)
    return

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/dataRemold/")
def create_item(item: Item):
    item = item_remold(item)
    # request_createData(item) # /createDataにデータを投げる
    return item

@app.post("/datasRemold/")
def create_items(items: List[Item]):
    new_items = []
    for item in items:
        item = item_remold(item)
        new_items.append(item)
    # request_createData(new_items) # /createDataにデータを投げる
    return new_items
