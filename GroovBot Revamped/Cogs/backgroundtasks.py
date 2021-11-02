import discord
import datetime
from discord.ext import commands, tasks
from discord.user import User
from Utils import utils
from utilsx.console import Colors
from config.config import ON_MEMBER_JOIN_MESSAGE_SERVER, ON_MEMBER_JOIN_DM, WELLCOME_MESSAGE_CHANNEL, GOODBYE_MESSAGE_CHANNEL, GIVE_ROLE_ON_JOIN, ROLE

y = Colors.yellow.value
lm = Colors.magenta.value
bot = commands.Bot(command_prefix="=",intents=discord.Intents.all())

class BackGroundTasks(commands.Cog):
    """
    Handels All The Background Tasks That The Bot Has To Deal With
    """
    utils.info(f"{y}Cog Loaded ~ {lm}BackGroundTasks")
            
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        utils.event(f"{member} joined the Server")
        if ON_MEMBER_JOIN_DM is True:
            if member is User.bot:
                embeddm = discord.Embed(
                        title = "Welcome!", 
                        description = f"Welcome {member.mention} to **{member.guild.name}**!", #f"Welcome {member.mention} to {guild.name}"
                        colour= discord.Colour.purple()
                        )
                embeddm.set_footer(text=f"from {member.guild.name}")
                embeddm.timestamp = datetime.datetime.utcnow()
                await member.send(embed=embeddm)

        if ON_MEMBER_JOIN_MESSAGE_SERVER is True:
            channel = discord.utils.get(member.guild.text_channels, name=WELLCOME_MESSAGE_CHANNEL)
            
            if channel:
                embed = discord.Embed(
                    title = "Welcome!", 
                    description = f"Welcome {member.mention} to **{member.guild.name}**!", 
                    colour= discord.Colour.purple()
                    )
                embed.timestamp = datetime.datetime.utcnow()
                await channel.send(embed=embed)
        if GIVE_ROLE_ON_JOIN is True:
            await member.add_roles(ROLE)


    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        utils.event(f"{member} Left the Server")
        if ON_MEMBER_JOIN_DM == True:
            if member is User.bot:
                embeddm = discord.Embed(
                        title = "Goodbye.", 
                        description = f"Goodbye {member.mention}. You get a goodbye from all of us.", 
                        colour= discord.Colour.purple()
                        )
                embeddm.set_footer(text=f"from {member.guild.name}")
                embeddm.timestamp = datetime.datetime.utcnow()
                await member.send(embed=embeddm)
        if ON_MEMBER_JOIN_MESSAGE_SERVER is True:
            channel = discord.utils.get(member.guild.text_channels, name=GOODBYE_MESSAGE_CHANNEL)
            
            if channel:
                embed = discord.Embed(
                    title = "Goodbye.", 
                    description = f"Goodbye {member.mention}. You get a goodbye from all of us.", 
                    colour= discord.Colour.purple()
                    )
                embed.timestamp = datetime.datetime.utcnow()
                await channel.send(embed=embed)
