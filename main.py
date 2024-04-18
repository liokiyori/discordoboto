import os
from dotenv import load_dotenv


import disnake
from disnake.ext import commands


load_dotenv()

guild_id = os.getenv("guild_id")

# Initialisation du bot
bot = commands.InteractionBot(test_guilds=[int(guild_id)])


@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

@bot.event
async def on_member_join(member):
    channel_id = os.getenv("channel_id")
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(f"Bienvenue a notre alsacien préféré {member.mention}!")
    else:
        print("Channel not found")

@bot.slash_command(name = "test")
async def test(inter):
    await inter.response.send_message("Hello World")


bot.run(os.getenv("discord_token"))
