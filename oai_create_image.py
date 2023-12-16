#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
openai.api_type = "azure"
openai.api_base = "https://oai-generated.openai.azure.com/"
openai.api_version = "2023-06-01-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

class Oai_create_image:

    def get_response(self, element):

        # prompt = '' + element + '今の文章が説明文が映画の感動的なシーン' # 良さげな画像になるようにpromptの文章をそのうち考える

        response = openai.Image.create(
            prompt = element, # そのうちpromptに差し替える
            size = '1024x1024',
            n = 1
        )
        image_url = response["data"][0]["url"]

        # print('________________________\n__get_response_success__\n________________________\n')

        return image_url