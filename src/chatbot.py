import poe
import logging


class Chatbot:
    def __init__(self, token, bot_name: str = "chinchilla"):
        self.bot_name = bot_name
        try:
            poe.logger.setLevel(logging.INFO)
            self.client = poe.Client(token)

        except Exception as e:
            print(e)

    def query_from_api(self, query):
        response = ""
        for chunk in self.client.send_message(self.bot_name, query, with_chat_break=True):
            word = chunk["text_new"]
            response += word

        return response
