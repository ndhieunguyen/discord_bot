import os
import discord
from discord.ext import commands
from src.chatbot import Chatbot
from src.imagebot import Imagebot


intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)
chatbot = Chatbot(os.environ["poe_api_token"])
imagebot = Imagebot(os.environ["replicate_api_token"])


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")


@bot.command(name="q")
async def q(ctx, *query):
    query = " ".join(query)
    await ctx.send(f"{chatbot.query_from_api(query=query)}")


@bot.command(name="gen")
async def gen(ctx, *query):
    query = " ".join(query)
    await ctx.send(imagebot.generate_image(query=query))


bot.run(os.environ["discord_token"])
