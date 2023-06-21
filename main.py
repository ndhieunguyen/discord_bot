import poe
import logging
import discord
from discord.ext import commands
import os  


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
    
    
if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.message_content = True
    client = commands.Bot(command_prefix="!", intents=intents)
    chatbot = Chatbot(os.environ['poe_api_token'])
    
    @client.command(name='q')
    async def query(ctx, *query):
        query = " ".join(query)
        await ctx.send(f"{chatbot.query_from_api(query=query)}")
        
    client.run(os.environ['discord_token'])