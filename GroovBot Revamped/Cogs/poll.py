
import random
import discord
import asyncio
import numpy
import datetime
from discord.ext import commands
from discord.ext.commands import CommandInvokeError
from Utils import utils
from utilsx.console import Colors

bot = commands.Bot(command_prefix="=")

class Giveaway(commands.Cog):
    """Handles all the Poll/Givaway Commands"""
    def __init__(self, bot):
        self.bot = bot
        self.polls = []
        self.answers = {}
        y = Colors.yellow.value
        lm = Colors.magenta.value
        utils.info(f"{y}Cog Loaded ~ {lm}Giveaway")

    @commands.command(help=("Lets you put up a poll \n =poll '"'Time'"' '"'Your question'"' '"'Option 1'"' '"'Option 2'"' '"'Option 3'"' '"'Option 4'"' "))
    async def poll(self, ctx, Time, question, *options: str):
        utils.inforan(f"Command Ran ~ Poll")
#Error Messages
        try:
            int(Time)
        except:
            await ctx.send("```Error! You Must Specify A Time For The Bot To Keep The Poll Up For.```")
            return
        if int(Time) <= 0:
            await ctx.send("```Error! You Must Specify A Time For The Bot To Keep The Poll Up For.```")
            return
        if len(options) <= 1:
            await ctx.send("```Error! A poll must have more than one option.```")
            return
        if len(options) > 4:
            await ctx.send("```Error! Poll can have no more than four options.```")
            return

        if len(options) == 2 and options[0] == "yes" and options[1] == "no":
            reactions = ['👍', '👎']
        else:
            reactions = ["1️⃣", "2️⃣", "3️⃣", "4️⃣" ]
            
        description = []
        for x, option in enumerate(options):
            description += '\n {} {} '.format(reactions[x], option)

        embed = discord.Embed(title = question, colour=discord.Colour.green(), description = ''.join(description))
        embed.add_field(name=f"The Poll Ends in {Time} seconds", value="**Waiting For Results**")
        embed.timestamp=datetime.datetime.utcnow()
        embed.set_footer(text=f"Poll by {ctx.author.name}")

        react_message = await ctx.send(embed = embed)

        for reaction in reactions[:len(options)]:
            await react_message.add_reaction(reaction)

        poll_id2 = react_message.id

        react_message = await ctx.channel.fetch_message(poll_id2)
        await asyncio.sleep(int(Time))

        message = await ctx.channel.fetch_message(poll_id2)

        most_voted = max(message.reactions, key=lambda r: r.count)

        embed = discord.Embed(title = f"Poll Over! \n Question: \n {question} \n Answers:", colour=discord.Colour.red(), description = ''.join(description))
        embed.add_field(name=f"**The Result Is {most_voted}**", value=f"Poll by {ctx.author.name}")
        embed.timestamp=datetime.datetime.utcnow()
        embed.set_footer(text=f"")

        await react_message.edit(embed=embed)


    @commands.command(help=("Lets you do a giveaway"))
    async def giveaway(self, ctx, Time : int, *, giveaway):
            utils.inforan(f"Command Ran ~ Giveaway")

            poll = discord.Embed(title=f"{ctx.author.name}#{ctx.author.discriminator} Started a Giveaway For {giveaway}", description=f"\n **Giveaway - {giveaway}**", colour=discord.Colour.blue())
            poll.add_field(name="React With The Check Mark To Enter The Giveaway!", value=":white_check_mark:")
            poll.timestamp=datetime.datetime.utcnow()
            poll.set_footer(text=f"Voting ends in {Time} seconds.")
            global poll_msg
            poll_msg = await ctx.send(embed=poll) # only returns temporary message, we need to get the cached message to get the reactions
            poll_id = poll_msg.id

            await poll_msg.add_reaction("🎉") # yes

            await asyncio.sleep(Time) # 15 seconds to vote

            poll_msg = await ctx.channel.fetch_message(poll_id)

            votes = {"🎉": 0}
            reacted = []

            for reaction in poll_msg.reactions:
                if reaction.emoji in ["🎉"]:
                    async for user in reaction.users():
                        votes[reaction.emoji] += 1
                        reacted.append(user.id)
                        print(str(user.id))
            
            users = await reaction.users().flatten()
            users.pop(0)

            embed = discord.Embed(title="Giveaway Over!", description=f"**The Winner is {random.choice(users)}**", colour=discord.Colour.green())
            await poll_msg.edit(embed=embed)
            await poll_msg.clear_reactions()
            print(str(users))

    @giveaway.error
    async def GivawayError(self, ctx, exc):
        if isinstance(exc, CommandInvokeError):
            await poll_msg.delete()
            em = discord.Embed(title="No One Voted", colour=discord.Colour.red())
            await ctx.send(embed=em)
