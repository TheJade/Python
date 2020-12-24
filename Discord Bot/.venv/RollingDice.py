# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='d', help='Roll the dice " /d A B C " - A is sides \n - B is constant added \n - C number of dice rolled')
async def roll(ctx, number_of_sides: int, *therest):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)) + int(therest[0]) if len(therest) > 0 else 0)
        for _ in range(int(therest[1]) if len(therest) > 1 else 1)
    ]
    await ctx.send(', '.join(dice))

bot.run(TOKEN)