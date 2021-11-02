import math
import discord
import random
import asyncio
from discord.ext.commands import MissingRequiredArgument
import datetime
from discord.ext import commands
from utilsx.console import Colors
from Utils import utils
from Utils.utils import text_to_owo, GetRole, info
from config.config import RESPONSES, MUTED_NAME

y = Colors.yellow.value
lm = Colors.magenta.value
bot = commands.Bot(command_prefix="=",case_insensitive=True)

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        utils.info(f"{y}Cog Loaded ~ {lm}Fun")

    @commands.command()
    async def owo(self, ctx):
        utils.inforan(f"Command Ran ~ OwO")
        await ctx.send(text_to_owo(ctx.message.content))

    #pootis
    @commands.command(name="pootis", help="The credits command but with a big pootis :)")
    async def Pootis(self, ctx):
        utils.inforan(f"Command Ran ~ Pootis")
        embed = discord.Embed(
            title = "Credits",
            description = "**Made By SpyCrab \n ** https://www.youtube.com/watch?v=tmY-G6sngk8 \nhttps://www.youtube.com/watch?v=BKInDainD5M&list=PL21VVD05XtNkPGuHPkdYOMNMu0nC5uF1Y&index=8 \n https://youtu.be/ScACgyrd-Eg **kat**",
            colour = discord.Colour.green()
        )
        embed.set_image(url = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c50d8b86-e1a6-4f82-83f6-b83b873fbcb1/dbvm80m-b371f3e4-9b3a-4581-a00a-d3d270f1d8d3.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2M1MGQ4Yjg2LWUxYTYtNGY4Mi04M2Y2LWI4M2I4NzNmYmNiMVwvZGJ2bTgwbS1iMzcxZjNlNC05YjNhLTQ1ODEtYTAwYS1kM2QyNzBmMWQ4ZDMuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.HPmvyd73Xw2mcBYHOrYKH-O-Y7YpgPVonGAHhngBmco")
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/731358096181559297/895805153259696138/shpee_crab.jpg")
        embed.set_author(name="SpyCrab", icon_url="https://cdn.discordapp.com/attachments/731358096181559297/895805153259696138/shpee_crab.jpg")

        await ctx.send(embed=embed)


    #8ball
    @commands.command(aliases=["8ball",], help="The =8ball command is a 8ball with costum responces!  just put your question after =8ball to get your answer!")
    async def _8ball(self, ctx, *, question):      
        utils.inforan(f"Command Ran ~ 8ball")
        embed = discord.Embed(
            title = "Magic 8Ball",
            description = f"**Your Question Was - {question}\nYour Answer Is - {random.choice(RESPONSES)}**",
            colour = discord.Colour.green()
        )
                    
        await ctx.send(embed=embed)

    #coin
    @commands.command(help="Flips a Coin!")
    async def coin(self, ctx):
        utils.inforan(f"Command Ran ~ Coin")
        Flip=["Heads", "Tales"]
        await ctx.send(f"{random.choice(Flip)}")


class Other(commands.Cog):
    """Other Commands"""
    info(f"{y}Cog Loaded ~ {lm}Other")

    @commands.command(name=("credits"), help="The =credits command will show the credits of who made the bot :)")
    async def Credits(self, ctx):
        utils.inforan(f"Command Ran ~ Credits")
        embed = discord.Embed(
            title = "Credits",
            description = "**Made By SpySkyPickleCrab \n Thanks To My Brother, CACGaming For Helping Me Fix Some Bugs And Optimizing The Code \n And For Fixing The Bot Somehow :)** \n https://youtu.be/ScACgyrd-Eg **kat**",
            colour = discord.Colour.green()
        )
        #embed.set_image(url = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c50d8b86-e1a6-4f82-83f6-b83b873fbcb1/dbvm80m-b371f3e4-9b3a-4581-a00a-d3d270f1d8d3.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2M1MGQ4Yjg2LWUxYTYtNGY4Mi04M2Y2LWI4M2I4NzNmYmNiMVwvZGJ2bTgwbS1iMzcxZjNlNC05YjNhLTQ1ODEtYTAwYS1kM2QyNzBmMWQ4ZDMuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.HPmvyd73Xw2mcBYHOrYKH-O-Y7YpgPVonGAHhngBmco")
        embed.set_thumbnail(url = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c50d8b86-e1a6-4f82-83f6-b83b873fbcb1/dbvm80m-b371f3e4-9b3a-4581-a00a-d3d270f1d8d3.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2M1MGQ4Yjg2LWUxYTYtNGY4Mi04M2Y2LWI4M2I4NzNmYmNiMVwvZGJ2bTgwbS1iMzcxZjNlNC05YjNhLTQ1ODEtYTAwYS1kM2QyNzBmMWQ4ZDMuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.HPmvyd73Xw2mcBYHOrYKH-O-Y7YpgPVonGAHhngBmco")
        embed.set_author(name="SpySkyPickleCrab#6212", icon_url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c50d8b86-e1a6-4f82-83f6-b83b873fbcb1/dbvm80m-b371f3e4-9b3a-4581-a00a-d3d270f1d8d3.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2M1MGQ4Yjg2LWUxYTYtNGY4Mi04M2Y2LWI4M2I4NzNmYmNiMVwvZGJ2bTgwbS1iMzcxZjNlNC05YjNhLTQ1ODEtYTAwYS1kM2QyNzBmMWQ4ZDMuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.HPmvyd73Xw2mcBYHOrYKH-O-Y7YpgPVonGAHhngBmco")

        await ctx.send(embed=embed)

    @commands.command(pass_context=True, aliases=["user", "u"])
    async def whois(self, ctx, user: discord.Member):
        utils.inforan(f"Command Ran ~ Whois ~ {user.display_name}")
        if user.display_name == "spycrabb":
            embed = discord.Embed(
                title=f"{user}'s info",
                description="Here's what I could find:",
                color=discord.Colour.red(),
            )
            embed.add_field(name="Username", value=user, inline=False)
            embed.add_field(name="ID", value=user.id, inline=False)
            embed.add_field(name="Status", value=user.status, inline=False)
            embed.add_field(name="Highest role", value=user.top_role, inline=False)
            embed.add_field(name="Joined at", value=user.joined_at, inline=False)
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/731358096181559297/903632349537910834/spycrab.jpg?width=766&height=676")
            embed.set_author(name=user, icon_url="https://media.discordapp.net/attachments/731358096181559297/903632349537910834/spycrab.jpg?width=766&height=676")
            await ctx.channel.send(embed=embed)
        else:
            try:
                embed = discord.Embed(
                    title=f"{user}'s info",
                    description="Here's what I could find:",
                    color=discord.Colour.red(),
                )
                embed.add_field(name="Username", value=user, inline=False)
                embed.add_field(name="ID", value=user.id, inline=False)
                embed.add_field(name="Status", value=user.status, inline=False)
                embed.add_field(name="Highest role", value=user.top_role, inline=False)
                embed.add_field(name="Joined at", value=user.joined_at, inline=False)
                embed.set_thumbnail(url=user.avatar_url)
                embed.set_author(name=user, icon_url=user.avatar_url)
                await ctx.channel.send(embed=embed)
            except Exception as e:
                
                await ctx.channel.send(
                    "```Error!```"
                )

class Modtools(commands.Cog):
    """Moderator Tools"""
    info(f"{y}Cog Loaded ~ {lm}ModTools")

    @commands.has_any_role("admin", "Owner", "Mod", "Nigel")
    @commands.has_permissions(manage_roles=True, manage_messages=True)
    @commands.command()
    async def mute(self, ctx, member: discord.Member, *, time: int):
        utils.inforan(f"Command Ran ~ Mute")
        em=discord.Embed(title="Muted", description=f"Muted {member.mention} \nfor {time} seconds", colour=discord.Colour.red())
        em.timestamp=datetime.datetime.utcnow()
        
        guild = ctx.guild
        role = discord.utils.get(ctx.guild.roles, name=MUTED_NAME)
        if not role:
            await guild.create_role(
            name=MUTED_NAME
            )
            role = discord.utils.get(ctx.guild.roles, name=MUTED_NAME)
            for channel in guild.channels:
                await channel.set_permissions(role, speak=False, send_messages=False, read_message_history=True, read_messages=False)
            await member.add_roles(role, reason="Muted")
            await ctx.send(embed=em)
        else:
            await member.add_roles(role, reason="Muted")
            await ctx.send(embed=em)

        await asyncio.sleep(time)

        um = discord.Embed(description=f"**You've been unmuted in {guild.name}**", colour=discord.Colour.green())
        um.timestamp=datetime.datetime.utcnow()

        await member.send(embed=um)
        await member.remove_roles(role, reason="Mute Time Over")

    @mute.error
    async def MuteError(self, ctx, exc):
        if isinstance(exc, MissingRequiredArgument):
            await ctx.send("```One or more Required Arguments are Missing```")

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role("admin", "Owner", "Mod", "Nigel")
    async def unmute(self, ctx, member: discord.Member):
        utils.inforan(f"Command Ran ~ Unmute")
        guild = ctx.guild
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        um2 = discord.Embed(description=f"**You've been unmuted in {guild.name}**", colour=discord.Colour.green())
        um2.timestamp=datetime.datetime.utcnow()
        um = discord.Embed(
            description = f"**Unmuted {member.mention}**",
            colour=discord.Colour.green()
        )
        um.timestamp=datetime.datetime.utcnow()
        
        await member.send(embed=um2)
        await ctx.send(embed=um)
        await member.remove_roles(role, reason="UnMuted")

    @unmute.error
    async def UnMuteError(self, ctx, exc):
        if isinstance(exc, MissingRequiredArgument):
            await ctx.send("```You Need To Specify A Member To Unmute```")

    @commands.command()
    @commands.is_owner()
    async def rules_setup(self, ctx):
        utils.inforan(f"Command Ran ~ Rules_Setup")
        author = ctx.author
        channel = discord.utils.get(author.guild.text_channels, name="rules")
        embed = discord.Embed(
            title = "Rules:", 
            description="No Racism\nNo Spamming\nNo Toxicity\nNo NSFW Stuff\nTry to keep the server not a dumpster fire\nNo Among Us\nNo Homophobia\nNo Going to far with religeous stuff\nFollow the all rules or else...",
            colour=discord.Colour.blurple()
        )
        await channel.send(embed=embed)

    @commands.is_owner()
    @commands.command(name='nick')
    @commands.bot_has_permissions(change_nickname=True)
    async def change_nick(self, ctx, *, nickname: commands.clean_content = None):
        """Change or reset the bot's nickname"""
        utils.inforan(f"Command Ran ~ Change_Nick")

        await ctx.me.edit(nick=nickname)
        await ctx.send('OwO')
        utils.inforan(f"Command Ran ~ Change_Nick ~ {utils.lg}Suceccful")

    @commands.is_owner()
    @commands.command(name='game')
    async def change_game(self, ctx, *, game: str = None):
        """Change or reset the bot's presence"""
        utils.inforan(f"Command Ran ~ Change_Game")

        game = game or f'{ctx.prefix}help'
        activity = discord.Game(game)
        await self.bot.change_presence(activity=activity)
        self.game = game
        await ctx.send(f'I\'m now playing {game}')
        utils.inforan(f"Command Ran ~ Change_Game ~ {utils.lg}Suceccful")

    @commands.is_owner()
    @commands.command(name='avatar')
    @commands.check(lambda ctx: len(ctx.message.attachments) == 1)
    async def change_avatar(self, ctx):
        """Change avatar"""
        utils.inforan(f"Command Ran ~ Change_Avatar")
        await self.bot.user.edit(avatar=await ctx.message.attachments[0].read())
        await ctx.send('OwO')
        utils.inforan(f"Command Ran ~ Change_Avatar ~ {utils.lg}Suceccful")

    @commands.has_any_role("admin", "Nigel", "Owner")
    @commands.command()
    async def RRSetup(self, ctx):
        utils.inforan(f"Command Ran ~ RRSetup")

        role = (f"{GetRole(ctx, 'Pink').mention}", f"{GetRole(ctx, 'Blue').mention}", f"{GetRole(ctx, 'Yellow').mention}", f"{GetRole(ctx, 'she/her').mention}", f"{GetRole(ctx, 'he/him').mention}", f"{GetRole(ctx, 'they/them').mention}\n", "**Select Your Games!**", f"{GetRole(ctx, 'Minecraft').mention} (Currently Dosent Work)", f"{GetRole(ctx, 'ApexLegends').mention} (Currently Dosent Work)", f"{GetRole(ctx, 'Phasmophobia').mention}")
        reactions = ["🍓", "🫐", "🍌", "♀️", "♂️", "👥", "🎮", "<:minecraft:902949359497396296>", "<:Apex:902970278139789423>", "👻"]


        description = []
        for x, option in enumerate(role):
            description += '\n {} {} '.format(reactions[x], option)
        embed = discord.Embed(title = "Select Your Roles!", description = "".join(description), colour = discord.Colour.blurple())



        channel = discord.utils.get(ctx.guild.text_channels, name="roles")
        rrm = await channel.send(embed = embed)
        for reaction in reactions[:len(role)]:
            await rrm.add_reaction(reaction)
            await rrm.clear_reaction("⚫")
            await rrm.clear_reaction("🎮")
            rmm_id = rrm.id
            rmm = await ctx.channel.fetch_message(rmm_id)
            utils.inforan(f"Command Ran ~ RRSetup ~ {utils.lg}Suceccful")
        
    @commands.has_any_role("admin", "Nigel", "Owner")
    @commands.command()
    async def RREdit(self, ctx):
        utils.inforan(f"Command Ran ~ RREdit")

        role = (f"{GetRole(ctx, 'Pink').mention}", f"{GetRole(ctx, 'Blue').mention}", f"{GetRole(ctx, 'Yellow').mention}", f"{GetRole(ctx, 'she/her').mention}", f"{GetRole(ctx, 'he/him').mention}", f"{GetRole(ctx, 'they/them').mention}\n", "**Select Your Games!**", f"{GetRole(ctx, 'Minecraft').mention}", f"{GetRole(ctx, 'ApexLegends').mention}", f"{GetRole(ctx, 'Phasmophobia').mention}", f"{GetRole(ctx, 'Overwatch').mention}")
        reactions = ["🍓", "🫐", "🍌", "♀️", "♂️", "👥", "🎮", "<:minecraft:902949359497396296>", "<:Apex:902970278139789423>", "👻", "<:Overwatch:903690256610635807>"]


        description = []
        for x, option in enumerate(role):
            description += '\n {} {} '.format(reactions[x], option)
        embed = discord.Embed(title = "Select Your Roles!", description = "".join(description), colour = discord.Colour.blurple())
        embed.set_footer(text="There are more to add just wait")

        channel = discord.utils.get(ctx.guild.text_channels, name="roles")
        rrm_message = await ctx.channel.fetch_message(902985201901273139)
        rrm = await rrm_message.edit(embed=embed)
        for reaction in reactions[:len(role)]:
            await rrm_message.add_reaction(reaction)
            await rrm_message.clear_reaction("🎮")      
            utils.inforan(f"Command Ran ~ RREdit ~ {utils.lg}Suceccful")
        