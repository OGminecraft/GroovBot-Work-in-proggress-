import discord
import random
from discord.ext import commands, tasks, ipc
from Cogs.music import Player
from Cogs.poll import Giveaway
from Cogs.other import Fun, Other, Modtools
from random import choice
from Cogs.help import HelpReWorked
from Cogs.backgroundtasks import BackGroundTasks
from Utils import utils
from Cogs.errors import ErrorCog
from utilsx.console import Colors
from Cogs.SelfAssignedRoles import Sar 
from config.config import TOKEN
#Work in progress Cogs
from Cogs.WIP.life import Life

class DashBot(commands.Bot):

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)

		self.ipc = ipc.Server(self,secret_key = "what ever you want here just no spaces")

	async def on_ipc_ready(self):
		"""Called upon the IPC Server being ready"""
		utils.info(f"{utils.y}Ipc server is ready.")

	async def on_ipc_error(self, endpoint, error):
		"""Called upon an error being raised within an IPC route"""
		print(endpoint, "raised", error)


lg = Colors.light_green.value
r = Colors.red.value
y = Colors.yellow.value
lm = Colors.magenta.value

#intents
intents = discord.Intents.default()
intents.members = True
intents.reactions = True

bot = DashBot(command_prefix="=",case_insensitive=True ,intents=intents)
bot.remove_command("help")

status = ["Jammin! |=help", "Dark Souls! |=help", "SpyCrab The Game! \n| =help"]

@bot.event
async def on_ready():
    change_status.start()
    utils.info(f"{lg + bot.user.name} is ready.") 

@tasks.loop(minutes=30)
async def change_status():
    await bot.change_presence(activity=discord.Game(choice(status))) 

@bot.ipc.route()
async def get_guild_count(data):
	return len(bot.guilds) # returns the len of the guilds to the client

@bot.ipc.route()
async def get_guild_ids(data):
	final = []
	for guild in bot.guilds:
		final.append(guild.id)
	return final # returns the guild ids to the client

@bot.ipc.route()
async def get_guild(data):
	guild = bot.get_guild(data.guild_id)
	if guild is None: return None

	guild_data = {
		"name": guild.name,
		"id": guild.id,
		"prefix" : "?"
	}

	return guild_data

#Ping
@bot.command(aliases=["ms", "Pong"], help ="The =Ping command tells you your Ping in ms")
async def Ping(ctx):
    utils.inforan(f"Command Ran ~ Ping")
    pingorpong =["Ping!", "Pong!"]
    await ctx.send(f"{random.choice(pingorpong)} {round(bot.latency * 1000)}ms")


#adding Cogs when bot is ready
async def setup():
    await bot.wait_until_ready()
    bot.add_cog(Fun(bot))
    bot.add_cog(HelpReWorked(bot))
    bot.add_cog(Player(bot))
    bot.add_cog(Giveaway(bot))
    bot.add_cog(BackGroundTasks(bot))
    bot.add_cog(Other(bot))
    bot.add_cog(Modtools(bot))
    bot.add_cog(Sar(bot))
    bot.add_cog(ErrorCog(bot))
    #Work in Progress Cogs
    #bot.add_cog(Pterodactyl(bot))
    #bot.add_cog(Life(bot))
    utils.info(f"{y}All Cogs Loaded ~ {lm}Bot Completely Ready \n{r}Notifing Server!")
    

#bot run stuff
bot.loop.create_task(setup())
bot.ipc.start()
bot.run(TOKEN)   
