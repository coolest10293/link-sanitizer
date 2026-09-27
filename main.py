import discord, datetime
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
        sent = message.created_at

        import calendar 
        sent = calendar.timegm(sent.utctimetuple())
        msg = content.split(' ')

        if message.author == self.user:
            return
        for word in msg:
            if "https://youtu.be/" in word or "https://www.youtube.com/" in word or "https://youtube.com/" in word: 
                index = msg.index(word)
                msg.remove(word)
                try:
                    link = word.split("?")
                except Exception as e:
                    print(f"Error: {e}")
                else:
                    linkb = link[1]
                    linkb_parts = linkb.split("&")
                for part in linkb_parts:
                    if "si=" in part or "is=" in part:
                            sanitized = False
                            linkb_parts.remove(part)
                            try:
                                await message.delete()
                                sanitized = True
                            except Exception as e:
                                pass
                                # await channel.send(f"Your YouTube link is not sanitized, please sanitize your YouTube link.\n-# ||<@{message.author.id}>||")
        try:
            if sanitized:
                await channel.send(f"<@{message.author.id}>:\n{" ".join(msg[:index] + [link[0] + "?" + "&".join(linkb_parts)] + msg[index:])}\n-# <t:{sent}:s>")
        except:
            pass



intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)

with open('discord_token.txt') as dt:
    token = dt.read()

client.run(token)
