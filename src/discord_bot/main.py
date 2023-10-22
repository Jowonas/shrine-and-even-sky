import discord
from discord.ext import commands
from src.discord_bot.commands.owoify import make_owoify


description = "Not Shrine Bot"

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='s!', description=description, intents=intents)


@bot.command()
async def owoify(ctx, *message: str):
    await ctx.send(make_owoify(message))

token = input("Enter your Token: ")
bot.run(token)

# Invite:
# https://discord.com/oauth2/authorize?client_id=1165739276596695150&scope=bot&permissions=8
