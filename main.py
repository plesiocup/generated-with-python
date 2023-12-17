from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

import requests

from oai_create_image import Oai_create_image
from oai_create_discription import Oai_create_discription

app = FastAPI()

image_obj = Oai_create_image()
description_obj = Oai_create_discription()
prompt_obj = Oai_create_discription()

class Item(BaseModel):
    Id: int # 映画id
    Title: str = "Spirited Away" # タイトル
    Description: str = None # 説明
    Category: str # 映画カテゴリ
    Evaluation: float # 評価
    Playtime: int # 再生時間
    ImageURL: str = None # 画像URL
    ReleaseYear: int # 公開年
    EvaluatedCount: int # 評価した人数


def item_remold(item):
    count = 3
    while count > 0:
        item.Description  = create_discription(item.Title)
        prompt = create_prompt(item.Title, item.Category)
        # print(prompt)
        if (item.Description  == "error!"):
            print("ERROR (create_discription)!")
            count -= 1
        else:
            # item.ImageURL  = create_image(item.Title) # タイトルよりも生成した説明文をもとに画像を作成した方がいい気がした。
            item.ImageURL  = create_image(prompt)

            if (item.ImageURL  == "error!"):
                print("ERROR (create_image)!")
                count -= 1
            elif (item.ImageURL  == "discription error"):
                print("ERROR! disciption remold")
                count -= 1
            else :
                print("ERRORなし!!")
                break

    # item.Description  = create_discription(item.Title)
    # # item.ImageURL  = create_image(item.Title) # タイトルよりも生成した説明文をもとに画像を作成した方がいい気がした。
    # item.ImageURL  = create_image(item.Description )

    return item

def create_discription(title):
    description = description_obj.get_discription_response(title)
    return description

def create_prompt(title, category):
    prompt = prompt_obj.get_prompt_response(title, category)
    return prompt

def create_image(element):
    image_url = image_obj.get_response(element)
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
