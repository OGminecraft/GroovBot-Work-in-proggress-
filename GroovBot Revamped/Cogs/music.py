import asyncio
#from asyncio.windows_events import NULL
import youtube_dl
import pafy
import discord
from discord.ext import commands
from Utils import utils
from utilsx.console import Colors
from config.config import YT_AUDIO_DOWNLOAD, YT_SEARCH_RETURN_AMOUNT, YT_AUDIO_PLAYBACK_VOLUME, NULL, MEMBER_SKIP_PERCENTAGE

class Player(commands.Cog):
    """Handles All of the Music Stuff"""
    def __init__(self, bot):
        self.bot = bot
        self.song_queue = {}
        utils.info(f"{utils.y}Cog Loaded ~ {utils.lm}Player")
        self.setup()

    def setup(self):
        for guild in self.bot.guilds:
            self.song_queue[guild.id] = []

    async def check_queue(self, ctx, cskip1):
        if len(self.song_queue[ctx.guild.id]) > 0:
           # ctx.voice_client.stop()
            await self.play_song(ctx, self.song_queue[ctx.guild.id][0], cskip1)
            self.song_queue[ctx.guild.id].pop(0)
        elif discon:
            print("Null")
            return NULL
        else:
            print("stop")
            ctx.voice_client.stop()

    async def search_song(self, amount, song, get_url=False):
        info = await self.bot.loop.run_in_executor(None, lambda: youtube_dl.YoutubeDL({"format" : "bestaudio", "quiet" : True}).extract_info(f"ytsearch{amount}:{song}",download=YT_AUDIO_DOWNLOAD, ie_key="YoutubeSearch"))
        if len(info["entries"]) == 0: return None
        return [entry["webpage_url"] for entry in info["entries"]] if get_url else info

    async def ifskip(self, ctx, cskip):
        if cskip:
            return NULL
        else:
            await self.check_queue(ctx, False)


    async def play_song(self, ctx, song, cskip1):
        FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn',
        }
    
        url = pafy.new(song).getbestaudio().url
        #ctx.voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url, **FFMPEG_OPTIONS)), after=lambda error: self.bot.loop.create_task(self.check_queue(ctx)))
        ctx.voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url, **FFMPEG_OPTIONS)), after=lambda error: self.bot.loop.create_task(self.ifskip(ctx, cskip1)))
        ctx.voice_client.source.volume = YT_AUDIO_PLAYBACK_VOLUME
    


#Commands

    @commands.command()
    @commands.has_any_role("admin", "Owner", "Nigel")
    async def debug(self, ctx):
        utils.inforan(f"Command Ran ~ Debug")
        await ctx.send('Active Voice Client Source: ' + str(ctx.voice_client.source))
        await ctx.send("Queue: " + str(self.song_queue[ctx.guild.id]))
        
    @commands.command(help="lets you join the bot to your voice channel")
    async def join(self, ctx):
        utils.inforan(f"Command Ran ~ Join")
        if ctx.author.voice is None:
            return await ctx.send("You are not connected to a voice channel, please connect to a voice channel.")

        if ctx.voice_client is not None:
            await ctx.voice_client.disconnect()

        await ctx.author.voice.channel.connect()

    @commands.command(help="Makes the bot leave the call")
    async def stop(self, ctx):
            utils.inforan(f"Command Ran ~ Stop")
            if ctx.voice_client is not None:
                self.song_queue[ctx.guild.id] = []
                global discon
                discon = True
                return await ctx.voice_client.disconnect()
            else:
                await ctx.send("I am not connected to a voice channel.")

    @commands.command(help="Plays a Song of your choice")
    async def play(self, ctx, *, song=None):
            utils.inforan(f"Command Ran ~ Play")
            queue_len = len(self.song_queue[ctx.guild.id])

            if ctx.voice_client is None:
                await ctx.author.voice.channel.connect()
            if song is None:
                return await ctx.send("You must include a song to play.")

            if ctx.voice_client is None:
                return await ctx.send("I must be in a voice channel to play a song. Client: " + str(ctx.voice_client))

        # handle song where song isn't url
            if not ("youtube.com/watch?" in song or "https://youtu.be/" in song):
                await ctx.send("Searching for song, this may take a few seconds.")

                result = await self.search_song(1, song, get_url=True)

                if result is None:
                    return await ctx.send("Sorry, I could not find the given song, try using my search command.")

                song = result[0]

            if ctx.voice_client.source is not None:
                
                

                if queue_len < 10:
                    self.song_queue[ctx.guild.id].append(song)
                    print()
                    print('Song Added to Queue: ' + str(song))
                    print('Queue Length: ' + str(queue_len + 1))
                    return await ctx.send(f"I am currently playing a song, this song has been added to the queue at position: {queue_len+1}.")

                else:
                    return await ctx.send("Sorry, I can only queue up to 10 songs, please wait for the current song to finish.")
            global discon
            discon = False
            await self.play_song(ctx, song, False)
            await ctx.send(f"Now playing: {song}")
            print('Song Added: ' + str(song))


    @commands.command(help="searches for a song")
    async def search(self, ctx, *, song=None):
        utils.inforan(f"Command Ran ~ Search")
        if song is None: return await ctx.send("You forgot to include a song to search for.")

        await ctx.send("Searching for song, this may take a few seconds.")

        info = await self.search_song(YT_SEARCH_RETURN_AMOUNT, song)

        embed = discord.Embed(title=f"Results for '{song}':", description="*You can use these URL's to play an exact song if the one you want isn't the first result.*\n", colour=discord.Colour.red())
        
        amount = 0
        for entry in info["entries"]:
            embed.description += f"[{entry['title']}]({entry['webpage_url']})\n"
            amount += 1

        embed.set_footer(text=f"Displaying the first {amount} results.")
        await ctx.send(embed=embed)

    @commands.command(help="Shows The Current Queue")
    async def queue(self, ctx): # display the current guilds queue
            if len(self.song_queue[ctx.guild.id]) == 0:
                return await ctx.send("There are currently no songs in the queue.")

            embed = discord.Embed(title="Song Queue", description="", colour=discord.Colour.dark_gold())
            i = 1
            for url in self.song_queue[ctx.guild.id]:
                embed.description += f"{i}) {url}\n"
                i += 1

            embed.set_footer(text="Thanks for using me!")
            await ctx.send(embed=embed)

#skip
    @commands.command(help="Puts up a Poll To Skip The Current Song")
    async def skip(self, ctx):
        utils.inforan(f"Command Ran ~ Skip")
        if ctx.voice_client is None:
            return await ctx.send("I am not playing any song.")

        if ctx.author.voice is None:
            return await ctx.send("You are not connected to any voice channel.")

        if ctx.author.voice.channel.id != ctx.voice_client.channel.id:
            return await ctx.send("I am not currently playing any songs for you.")

        poll = discord.Embed(title=f"Vote to Skip Song by - {ctx.author.name}#{ctx.author.discriminator}", description="**80% of the voice channel must vote to skip for it to pass.**", colour=discord.Colour.blue())
        poll.add_field(name="Skip", value=":white_check_mark:")
        poll.add_field(name="Stay", value=":no_entry_sign:")
        poll.set_footer(text="Voting ends in 15 seconds.")

        poll_msg = await ctx.send(embed=poll) # only returns temporary message, we need to get the cached message to get the reactions
        poll_id = poll_msg.id

        await poll_msg.add_reaction(u"\u2705") # yes
        await poll_msg.add_reaction(u"\U0001F6AB") # no
        
        await asyncio.sleep(15) # 15 seconds to vote

        poll_msg = await ctx.channel.fetch_message(poll_id)
        
        votes = {u"\u2705": 0, u"\U0001F6AB": 0}
        reacted = []

        for reaction in poll_msg.reactions:
            if reaction.emoji in [u"\u2705", u"\U0001F6AB"]:
                async for user in reaction.users():
                    if user.voice.channel.id == ctx.voice_client.channel.id and user.id not in reacted and not user.bot:
                        votes[reaction.emoji] += 1

                        reacted.append(user.id)
        
        skip = False

        if votes[u"\u2705"] > 0:
            if votes[u"\U0001F6AB"] == 0 or votes[u"\u2705"] / (votes[u"\u2705"] + votes[u"\U0001F6AB"]) > MEMBER_SKIP_PERCENTAGE: # 80% or higher
                skip = True
                embed = discord.Embed(title="Skip Successful", description="***Voting to skip the current song was succesful, skipping now.***", colour=discord.Colour.green())

        if not skip:
            utils.inforan(f"Command Ran ~ Skip ~ {utils.lg}Succecful ~ Skiped = False")
            embed = discord.Embed(title="Skip Failed", description="*Voting to skip the current song has failed.*\n\n**Voting failed, the vote requires at least 80% of the members to skip.**", colour=discord.Colour.red())

        embed.set_footer(text="Voting has ended.")

        await poll_msg.clear_reactions()
        await poll_msg.edit(embed=embed)

        #global cskip
        #cskip = False
        if skip:
            utils.inforan(f"Command Ran ~ Skip ~ {utils.lg}Succecful ~ Skiped = True")
            ctx.voice_client.stop()
            await self.ifskip(ctx, True)


    @commands.command(help="Pauses The Current Song Playing")
    async def pause(self, ctx):
            utils.inforan(f"Command Ran ~ Pause")
            if ctx.voice_client.is_paused():
                return await ctx.send("I am already paused.")

            ctx.voice_client.pause()
            await ctx.send("The current song has been paused.")


    @commands.command(help="Unpauses The Current Song Playing")
    async def unpause(self, ctx):
            utils.inforan(f"Command Ran ~ Unpause")
            if ctx.voice_client is None:
                return await ctx.send("I am not connected to a voice channel.")

            if not ctx.voice_client.is_paused():
                return await ctx.send("I am already playing a song.")
        
            ctx.voice_client.resume()
            await ctx.send("The current song has been resumed.")

    @commands.is_owner()
    @commands.command()
    async def oskip(self, ctx):
        utils.inforan(f"Command Ran ~ OSkip")
        ctx.voice_client.stop()
        await self.ifskip(ctx, True)