import discord
from discord.ext import commands
from discord.ext.commands import bot
import requests


class Pterodactyl(commands.Cog):
    def __init__(self, bot):
        Useless = True
    
    @commands.command
    async def veiwserverstats(ctx, self):
        url = 'https://pterodactyl.file.properties/api/client'
        headers = {
            "Authorization": "Ajl4pe14d8d7QuYyJtgFGQr6diLo4VSybRvttjpyqlAilg5E",
            "Accept": "application/json",
            "cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
        }

        response = requests.request('GET', url, data=payload, headers=headers)
        print(response.text) 

def setup(bot):
    bot.add_cog(Pterodactyl(bot))