#Note: The openai-python library support for Azure OpenAI is in preview.
      #Note: This code sample requires OpenAI Python library version 0.28.1 or lower.
import os
import openai

openai.api_type = "azure"
openai.api_base = "https://oai-generated.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

class Oai_create_discription:

    def get_response(self, element):
        message_content = 'タイトルが' + element + 'の映画が魅力的に思えるような説明文を想像で出力' # 聞き方は要検討
        message_text = [{"role":"system","content": message_content}]

        response = openai.ChatCompletion.create(
            engine="gpt-35-turbo-16k",
            messages = message_text,
            temperature = 0.4,
            max_tokens = 250,
            top_p = 0.95,
            frequency_penalty = 0,
            presence_penalty = 0,
            stop = None
        )
        
        return response['choices'][0]['message']['content']