import discord
from discord.ext import commands, tasks

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        ids = [1515823264104976534, 1380330926881636372, 1178421286985289778]
        for guild_ids in ids:
            try:
                guild = discord.Object(id=guild_ids)
                synced = await self.tree.sync(guild=guild)
                print(f'Synced {len(synced)} commands to guild {guild.id}')
            except Exception as e:
                print(f'{len(synced)} commands to guild {guild.id} has failed to sync')
                print(f'Error: {e}')

    async def on_message(self, message):
        content = message.content
        channel = message.channel
        msg = content.split(' ')
        content_lower = f'{message.content}'.lower()
        if message.author == self.user:
            return
        if "https://youtu.be/" in content_lower or "https://youtube.com/" in content_lower: 
           if "?si=" in content_lower or "?is=" in content_lower:
                await channel.send(f"Your YouTube link is not sanitized, please sanitize your YouTube link.\n-# ||<@{message.author.id}>||")

intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)

with open('discord_token.txt') as dt:
    token = dt.read()

client.run(token)
