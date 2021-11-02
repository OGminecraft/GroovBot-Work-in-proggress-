from discord.ext import commands
from Utils.utils import fatal, warn, info
from utilsx.console import Colors

r = Colors.red.value
lr = Colors.light_red.value   
y = Colors.yellow.value
lm = Colors.magenta.value
info(f"{y}Cog Loaded ~ {lm}Sar")

class ErrorCog(commands.Cog):
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("```Error! Missing One Or More Required Arguments```")
            fatal(f"{r}Too many Arguements are Missing")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.TooManyArguments):
            await ctx.send("```Error! Too Many Arguements are Present```")
            fatal(f"{r}Too many Arguements are Present")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("```Error! Bad Arguement```")
            fatal(f"{r}Bad Arguement ~ {error}")

