import discord
import asyncio


class Trainingbot:
    def __init__(self, token, channel_id) -> None:
        self.token = token
        self.channel_id = channel_id
        self.loss_dict = {"train": [], "eval": []}

        intents = discord.Intents.default()
        self.client = discord.Client(intents=intents)
        self.channel = self.client.get_channel(channel_id)

    def append_loss(self, train_loss, eval_loss=None):
        self.loss_dict.append(train_loss)
        if eval_loss:
            self.loss_dict.append(eval_loss)

    async def log_loss(self):
        if len(self.loss_dict["eval"]) > 0:
            await self.channel.send(f"Train loss: {self.loss_dict['train'][-1]} \n Eval loss: {self.loss_dict['eval'][-1]}")
        else:
            await self.channel.send(f"Train loss: {self.loss_dict['train'][-1]}")

if __name__ == '__main__':
    