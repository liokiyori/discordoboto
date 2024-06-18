from dotenv import load_dotenv
import discord
from datetime import datetime
from discord.ext import commands, tasks
from modules.rssflux import fetch_rss
import os


load_dotenv()

token = os.getenv("discord_token")
guild_id = os.getenv("guild_id")
last_article_date = None

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.tree.command(name="hello", description="Say hello to the bot")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello !")

@bot.tree.command(name="ping", description="Get the bot latency")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong ! {round(bot.latency*1000)}ms")

@tasks.loop(minutes=30)
async def rss():
    global last_article_date
    channel = bot.get_channel(int(os.getenv("channel_bfm")))
    feed = fetch_rss()
    new_articles = []
    for entry in feed.entries:
        article_date = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %Z")
        if last_article_date is None or article_date > last_article_date:
            new_articles.append(entry)
    if new_articles:
        new_articles.sort(key=lambda x: datetime.strptime(x.published, "%a, %d %b %Y %H:%M:%S %Z"))
        for article in new_articles:
            titre = article.title
            link = article.link  
            await channel.send(f"{titre} : {link}")
        last_article_date = datetime.strptime(new_articles[-1].published, "%a, %d %b %Y %H:%M:%S %Z")

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')
    await bot.change_presence(activity=discord.Game(name="Bretons supérieur XD"))
    guild = discord.Object(id=int(guild_id)) 
    bot.tree.copy_global_to(guild=guild)
    await bot.tree.sync(guild=guild)
    rss.start()

bot.run(token)