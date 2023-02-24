"""
Productivity Bot for Discord
"""
# import required dependencies
import discord
from discord.ext import commands
from discord import app_commands
import string

# import bot token
from keys import *

intents = discord.Intents.all()
client = commands.Bot(command_prefix='-', intents=intents)
CHARACTERS = list(string.printable)

study_list = []


@client.event
async def on_ready():
    """ bot startup"""
    try:
        synced = await client.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(e)

    print('Bot is ready')
    print('--------------------------------------')


@client.tree.command(name='call_timmy', description='Call Timothy Zhang')
async def call_timmy(interaction: discord.Interaction):
    """ Call Timmy"""
    await interaction.response.send_message('<@426866069735473174>')


@client.tree.command(name='spam_timmy', description='Annoy Timothy Zhang')
async def call_timmy(interaction: discord.Interaction, level: int):
    """ Spam Timmy """
    if level <= 0:
        pass

    await interaction.response.send_message('<@426866069735473174>')
    channel = client.get_channel(interaction.channel_id)
    for _ in range(level - 1):
        await channel.send('<@426866069735473174>')


@client.tree.command(name='focus', description='Use this command to focus')
async def focus(interaction: discord.Interaction, time: int):
    """ Focus """
    study_list.append(interaction.user)
    await interaction.response.send_message(f'You have been put into focus mode for {time} minutes :)')


@client.event
async def on_member_join(member):
    """ new joins """
    print(f'{member} has joined a server')


@client.event
async def on_member_remove(member):
    """ new departures """
    print(f'{member} has left the server')


@client.event
async def on_message(message):
    """ Detects channel activity """
    if message.content != '' and message.author in study_list:
        await message.delete()
        await message.channel.send(f'Get back to work {message.author}')

# async def on_message(message):
#     """ Detects channel activity """
#     if message.content in CHARACTERS:
#         await message.delete()


client.run(BOTTOKEN)
