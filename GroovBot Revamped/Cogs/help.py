import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument
from Utils import utils
from Utils.utils import info

from utilsx.console import Colors

y = Colors.yellow.value
lm = Colors.magenta.value
class HelpReWorked(commands.Cog):
    
    info(f"{y}Cog Loaded ~ {lm}HelpReWorked")

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        utils.inforan(f"Command Ran ~ Help")
        author = ctx.author
        
        ln = discord.Embed(
            title = "Help Commands",
            description = "Use =chelp to get more info about any command",
            colour = discord.Colour.orange()
            )
        ln.add_field(name="Fun", value="**8ball:** \nThe =8ball command is a 8ball with costum responces!\n\n**coin:**\nFlips a Coin! \n\n**pootis:** \nThe credits command but with a big pootis :)\n\n**OwO**\nConverts Your Message To UwU language")
        ln.add_field(name="Music", value="**play:** \nPlays a song or queues a song when a songs already playing.\n\n**stop:**\nMakes the bot leave the channel\n\n**queue:**\nShows Whats In the queue\n\n**search:**\nSearchs for the song that you put after it\n\n**skip:**\nPuts up a vote to skip the song\n\n**pause:**\nPauses the song\n\n**unpause:**\nUpauses the song currently playing")
        ln.add_field(name="Other", value="**credits:** \nThe =credits command will show the credits of who made the bot :)\n\n**ping**\nThe =Ping command tells you your Ping in ms\n\n**poll**\nLets you put up a poll\n\n**giveaway**\nLets you do a giveaway")
        ln.set_footer(text="Hope This Helped!")
        await author.send(embed=ln)

    @commands.command()
    async def chelp(self, ctx, command: str):
        utils.inforan(f"Command Ran ~ CHelp ~{utils.y} {command}")
        author = ctx.author
               
        if command == "help":
            h = discord.Embed(
                title = "Help",
                description = "Shows The Help Command",
                colour = discord.Colour.red()
            )
            await author.send(embed=h)

        if command == "poll":
            h = discord.Embed(
                title = "Poll",
                description = f"how to put up a poll\n =poll 'time' 'question' 'answer1' 'answer2' 'answer3' 'answer4' \n Its optional to have 4 answers but 4 is the max amount of answers you can have and 2 is the minimum",
                colour = discord.Colour.red()
            )
            await author.send(embed=h)

        if command == "ping":
            h = discord.Embed(
                title = "Ping",
                description = "Tells You Your Ping",
                colour = discord.Colour.red()
            )
            await author.send(embed=h)

        if command == "giveaway":
            h = discord.Embed(
                title = "Giveaway",
                description = "How to Setup a Giveaway\n=giveaway time 'what you want to giveaway'",
                colour = discord.Colour.red()
            )
            await author.send(embed=h)

        if command == "credits":
            h = discord.Embed(
                title = "Credits",
                description = "Shows The Credits of who made the bot",
                colour = discord.Colour.red()
            )
            await author.send(embed=h)

        if command == "coin":
            h = discord.Embed(
                title = "Coin",
                description = "Flips a Coin",
                colour = discord.Colour.red()
            )
            await author.send(embed=h)

        if command == "pootis":
            h = discord.Embed(
                title = "Pootis",
                description = "The credits command but with a big pootis :)",
                colour = discord.Colour.red()
            )
            await author.send(embed=h)

        if command == "8ball":
            h = discord.Embed(
                title = "8Ball",
                description = "just put your question after =8ball to get your answer!",
                colour = discord.Colour.red()
            )
            await author.send(embed=h)

        if command == "play":
            h = discord.Embed(
                title = "Play",
                description = "Plays a song or queues a song when a songs already playing.",
                colour = discord.Colour.red()
            )
            await author.send(embed=h)

        if command == "skip":
            h = discord.Embed(
                title = "Skip",
                description = "Puts up a vote to skip the song",
                colour = discord.Colour.red()
            )
            await author.send(embed=h)

        if command == "stop":
            h = discord.Embed(
                title = "Stop",
                description = "Makes the bot leave the channel",
                colour = discord.Colour.red()
            )
            await author.send(embed=h)

        if command == "queue":
            h = discord.Embed(
                title = "Queue",
                description = "Shows Whats Currently In the queue",
                colour = discord.Colour.red()
            )
            await author.send(embed=h)

        if command == "search":
            h = discord.Embed(
                title = "Search",
                description = "Searchs for the song that you put after it",
                colour = discord.Colour.red()
            )
            await author.send(embed=h)

        if command == "pause":
            h = discord.Embed(
                title = "Pasue",
                description = "Pauses the song currently playing",
                colour = discord.Colour.red()
            )
            await author.send(embed=h)

        if command == "owo":
            h = discord.Embed(
                title = "OwO",
                description = "Converts Your Message To UwU language",
                colour = discord.Colour.red()
            )
            await author.send(embed=h)

        if command == "unpause":
            h = discord.Embed(
                title = "Unpause",
                description = "Unpauses the song currently playing",
                colour = discord.Colour.red()
            )
            await author.send(embed=h)

        if command == "chelp":
            h = discord.Embed(
                title = "Chelp",
                description = "Get help on a specific command",
                colour = discord.Colour.red()
            )
            await author.send(embed=h)

        if command == "debug":
            h = discord.Embed(
                title = "Debug",
                description = "Its for debuging, Not for you.",
                colour = discord.Colour.red()
            )
            await author.send(embed=h)

        if command == "mute":
            h = discord.Embed(
                title = "Mute",
                description = "How to use Mute\n=mute 'person' time",
                colour = discord.Colour.red()
            )
            await author.send(embed=h)

    
    @chelp.error
    async def chelpError(self, author, exc):
        if isinstance(exc, MissingRequiredArgument):
            await author.send("```You Need To Specify A Command You Need Help With```")

    @commands.command()
    async def shelp(self, ctx, code):
        """Seceret Help"""
        utils.inforan(f"Command Ran ~ CHelp ~{utils.y} {code}")
        sem = discord.Embed(title = "Seceret Help", description = "Seceret Stuff For Important People UnLike Spypugg", colour = discord.Colour.blue())
        sem.add_field(name = "Stuff", value = "**Pain**\n```PAIN```")
        sem.set_footer(text="Seceret Help")
        author = ctx.author
        if code == "6969":
            await author.send(embed=sem)
        else:
            await ctx.send("**WRONG CODE GO TO JAIL**")
            role = discord.utils.get(ctx.guild.roles, name="Muted")
            await author.add_roles(role)
            await asyncio.sleep(15)
            await author.remove_roles(role)

    @shelp.error
    async def shelpError(self, ctx, exc):
        if isinstance(exc, MissingRequiredArgument):
            print("NULL")