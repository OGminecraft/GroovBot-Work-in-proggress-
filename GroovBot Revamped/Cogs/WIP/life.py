import discord
import json
from discord.ext import commands
import json

from Utils.jsonloader import read_json, write_json

bot = commands.Bot(command_prefix="=",case_insensitive=True)

lives = int(6)
bot.users_started = []

class Life(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
    @bot.event
    async def on_ready():
        pass
    
    @commands.command()
    async def start(self, ctx, user: discord.Member):
        data = read_json("started")
        data["userstarted"].append(user.id)
        write_json(data, "started")



        

    @commands.command()
    async def kill(self, ctx):
        pass