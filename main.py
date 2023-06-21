import os
import discord
from discord.ext import commands
from src.chatbot import Chatbot
from src.imagebot import Imagebot


def main():
    intents = discord.Intents.default()
    intents.message_content = True
    client = commands.Bot(command_prefix="!", intents=intents)
    chatbot = Chatbot(os.environ["poe_api_token"])
    imagebot = Imagebot(os.environ["replicate_api_token"])

    @client.command(name="q")
    async def q(ctx, *query):
        query = " ".join(query)
        await ctx.send(f"{chatbot.query_from_api(query=query)}")

    @client.command(name="gen")
    async def gen(ctx, *query):
        query = " ".join(query)
        await ctx.send(imagebot.generate_image(query=query))

    client.run(os.environ["discord_token"])


if __name__ == "__main__":
    main()
