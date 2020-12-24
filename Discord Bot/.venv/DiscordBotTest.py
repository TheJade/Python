#    # bot.py
#    import os
#    import random
#    
#    from discord.ext import commands
#    from dotenv import load_dotenv
#    
#    load_dotenv()
#    TOKEN = os.getenv('DISCORD_TOKEN')
#    
#    bot = commands.Bot(command_prefix='!')
#    
#    @bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
#    async def nine_nine(ctx):
#        brooklyn_99_quotes = [
#            'I\'m the human form of the 💯 emoji.',
#            'Bingpot!',
#            (
#                'Cool. Cool cool cool cool cool cool cool, '
#                'no doubt no doubt no doubt no doubt.'
#            ),
#        ]
#    
#        response = random.choice(brooklyn_99_quotes)
#        await ctx.send(response)
#    
#    @bot.command(name='roll_dice', help='Simulates rolling dice.')
#    async def roll(ctx, number_of_dice: int, number_of_sides: int):
#        dice = [
#            str(random.choice(range(1, number_of_sides + 1)))
#            for _ in range(number_of_dice)
#        ]
#        await ctx.send(', '.join(dice))
#    
#    bot.run(TOKEN)

#           # bot.py
#           import os
#           
#           import discord
#           import random
#           from dotenv import load_dotenv
#           
#           load_dotenv()
#           TOKEN = os.getenv('DISCORD_TOKEN')
#           GUILD = os.getenv('DISCORD_GUILD')
#           
#           client = discord.Client()
#           
#           @client.event
#           async def on_ready():
#               for guild in client.guilds:
#                   if guild.name == GUILD:
#                       break
#           
#               print(
#                   f'{client.user} is connected to the following guild:\n'
#                   f'{guild.name}(id: {guild.id})\n'
#               )
#           
#               members = '\n - '.join([member.name for member in guild.members])
#               print(f'Guild Members:\n - {members}')
#           
#           @client.event
#           async def on_message(message):
#               if message.author == client.user: #checks if the message is from a bot if it is then it returns (this prevents recursion)
#                   return
#           
#               brooklyn_99_quotes = [
#                   'I\'m the human form of the 💯 emoji.',
#                   'Bingpot!',
#                   (
#                       'Cool. Cool cool cool cool cool cool cool, '
#                       'no doubt no doubt no doubt no doubt.'
#                   ),
#               ]
#           
#               if message.content == '99!':
#                   response = random.choice(brooklyn_99_quotes)
#                   await message.channel.send(response)
#           
#           client.run(TOKEN)