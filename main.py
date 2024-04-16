# This example requires the 'message_content' intent.
from discord.ext import commands
import discord
import typing

bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
    
@bot.tree.command(name= "bateau")
async def réponse_bateau(self, ctx: commands.Context):
    print("test je te baise")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run("")
