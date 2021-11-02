from discord.ext import commands
import discord
import random
from datetime import datetime
from praw import reddit
from utilsx.console import Prettier, Colors

d = Colors.default.value
lm = Colors.light_magenta.value
m = Colors.magenta.value
r = Colors.red.value
lr = Colors.light_red.value
b = Colors.blue.value
lb = Colors.light_blue.value
y = Colors.yellow.value
ly = Colors.light_yellow.value
lg = Colors.light_green.value

info_prefix = f"\b{m}[{lm}INFO{m}]{d} "
warning_prefix = f"\b{y}[{ly}WARN{y}]{d} "
fatal_prefix = f"\b{r}[{lr}FATAL{r}]{d} "
cmdran_prefix = f"\b{m}[{lm}CMDRAN{m}]{b} "
event_prefix = f"\b{m}[{lm}EVENT{m}]{b} "

log = bool

async def notify_user(member, message):
    if member is not None:
        channel = member.dm_channel
        if channel is None:
            channel = await member.create_dm()
        await channel.send(message)

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def last_replace(s, old, new):
    li = s.rsplit(old, 1)
    return new.join(li)

def text_to_owo(text):
    """ Converts your text to OwO """
    smileys = [';;w;;', '^w^', '>w<', 'UwU', '(・`ω\´・)', '(´・ω・\`)']

    text = text.replace('L', 'W').replace('l', 'w')
    text = text.replace('R', 'W').replace('r', 'w')

    text = last_replace(text, '!', '! {}'.format(random.choice(smileys)))
    text = last_replace(text, '?', '? owo')
    text = last_replace(text, '.', '. {}'.format(random.choice(smileys)))

    for v in vowels:
        if 'n{}'.format(v) in text:
            text = text.replace('n{}'.format(v), 'ny{}'.format(v))
        if 'N{}'.format(v) in text:
            text = text.replace('N{}'.format(v), 'N{}{}'.format(
                'Y' if v.isupper() else 'y', v))
                
    return text

def GetRole(ctx, Rolename):
    getrole = discord.utils.get(ctx.guild.roles, name=Rolename)
    return getrole


def printf(message: str) -> None:
    """
    Format prints a message to the console.
    (date + message)
    :param message: The message that must be printed.
    """
    Prettier.print(message + d, datetime.now())

def info(message: str) -> None:
    """
    Sends a message with the INFO prefix.
    :param message: The message that must be printed.
    """
    if log:
        printf(info_prefix + message)

def warn(message: str) -> None:
        """
        Sends a message with the WARN prefix.
        :param message: The message that must be printed.
        """
        if log:
            printf(warning_prefix + message)

def fatal(message: str) -> None:
    """
    Sends a message with the FATAL prefix.
    :param message: The message that must be printed.
    """
    if log:
        printf(fatal_prefix + message)

def cmdran(message: str) -> None:
        """
        Sends a message with the WARN prefix.
        :param message: The message that must be printed.
        """
        if log:
            printf(cmdran_prefix + message)

def inforan(message: str) -> None:
    if log:
        printf(info_prefix + cmdran_prefix + message)

def event(message: str) -> None:
    if log:
        printf(info_prefix + event_prefix + message)

