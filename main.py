# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot
from discord.ext import commands
import discord
import os
import random
import aiohttp
from dotenv import load_dotenv
load_dotenv()
import requests
import asyncio

from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  activity = discord.Activity(type=discord.ActivityType.watching, name = 'Interstellar')
  await client.change_presence(status=discord.Status.idle, activity=activity)
  print('We have logged in as {0.user}'.format(client))

  channel_id = 1269234641789915137
  channel = client.get_channel(channel_id)
  if channel:
     await channel.send("The bot is now online!")



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('/hello'):
        await message.channel.send('Hello sir!')

    if message.content.startswith('/taas-links'):
        # Embed setup
        embedVar = discord.Embed(
            title="ACCESS ALL OUR SOCIAL MEDIA LINKS DOWN BELOW!",
            color=discord.Color.dark_orange()
        )
        embedVar.add_field(name="Instagram", value="https://www.instagram.com/taas.astronomers/", inline=False)
        embedVar.add_field(name="TAAS Family WhatsApp Group", value="https://chat.whatsapp.com/FOXGNvfjZFR6LtUVENzSL0", inline=False)
        embedVar.add_field(name="TAAS Website", value="https://sites.google.com/thapar.edu/taas", inline=False)

        # File path
        file_path = 'C:\\Users\\spars\\Downloads\\UqKrHFjGaYQ3Fi9rACt6S9.jpg'
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                discord_file = discord.File(file, filename='UqKrHFjGaYQ3Fi9rACt6S9.jpg')
                embedVar.set_image(url=f'attachment://UqKrHFjGaYQ3Fi9rACt6S9.jpg')
                await message.channel.send(embed=embedVar, file=discord_file)
        else:
            await message.channel.send(embed=embedVar)

    if message.content.startswith('/image'):
        embed = discord.Embed(title='test', colour=discord.Colour.dark_orange())
        # Provide the full path to the image
        file_path = 'S:\\Programming Stuff\\TAAS\\bot\\IMG-20240524-WA0018.jpg'
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                discord_file = discord.File(file, filename='IMG-20240524-WA0018.jpg')
                embed.set_image(url=f'attachment://IMG-20240524-WA0018.jpg')
                await message.channel.send(embed=embed, file=discord_file)
        else:
            await message.channel.send('Image file not found.')

    if message.content.startswith('/rules'):
        embedVar = discord.Embed(title = 'RULES!', description = 'We have a small but strict set of rules on our server. Please read them and follow them strictly.', color = discord.Color.dark_orange())
        embed = discord.Embed(title='TAAS🚀', colour=discord.Colour.dark_orange())
        file_path = 'S:\\Programming Stuff\\TAAS\\bot\\images.jpeg'
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                discord_file = discord.File(file, filename='images.jpeg')
                embed.set_image(url=f'attachment://images.jpeg')
                await message.channel.send(embed=embed, file=discord_file)
        else:
            await message.channel.send('Image file not found.')
        embedVar.add_field(name = '1. Be respectful', value = 'You must respect all users, regardless of your liking towards them. Treat others the way you want to be treated.', inline = False)
        embedVar.add_field(name = '2. No Inappropriate Language ', value = 'Any derogatory language towards any user is prohibited. This is an English speaking server, so please speak English to the best of your ability', inline = False)
        embedVar.add_field(name = '3. No spamming', value = "Don't send a lot of small messages right after each other. Do not disrupt chat by spamming. Keep discussions relevant to channel topics and guidelines", inline = False)
        embedVar.add_field(name = '4. No pornographic/adult/other NSFW material', value = 'This is a community server and not meant to share this kind of material.', inline = False)
        embedVar.add_field(name = '5. No advertisements', value = 'We do not tolerate any kind of advertisements, whether it be for other communities or streams. Ask <@admin> before promoting your content in this server', inline = False)
        embedVar.add_field(name = '6. Project Privacy ', value = 'Do not provide or request help on projects that may break laws, breach terms of services, be considered malicious/inappropriate or be for graded coursework/exams.', inline = False)
        embedVar.add_field(name = '7. No offensive names and profile pictures', value = 'You will be asked to change your name or picture if the staff deems them inappropriate.', inline = False)
        embedVar.add_field(name = '8. Direct & Indirect Threats ', value = "Threats to other users of DDoS, Death, DoX, abuse, and other malicious threats are absolutely prohibited and disallowed.", inline = False)
        embedVar.add_field(name = '9. Follow the Discord Community Guidelines', value = 'You can find them here: https://discordapp.com/guidelines', inline = False)
        r = await message.channel.send(embed = embedVar)
    
        await r.add_reaction("👍🏻")
        await r.add_reaction("👎🏻")

    if message.content.startswith('/random-image'):

        image_directory = "S:\\Programming Stuff\\TAAS\\folder"
        all_files = os.listdir(image_directory)
        image_files = [file for file in all_files if file.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp','mp4'))]
        random_image_file = random.choice(image_files)
        random_image_path = os.path.join(image_directory, random_image_file)

        embed = discord.Embed(title = 'Random Image', colour = discord.Colour.dark_blue())

        file_path = random_image_path
        if os.path.isfile(file_path):
           with open(file_path, 'rb') as file:
              discord_file = discord.File(file, filename = random_image_file)
              embed.set_image(url = f'attachment://{random_image_file}')
              await message.channel.send(embed = embed, file = discord_file)

    if message.content.startswith('/roles'):
       embedVar = discord.Embed(title = 'Roles', description = 'Select your roles', color = discord.Colour.dark_orange())
       embedVar.add_field(name = 'Male : @Male', value = "React with ♂️", inline=False)
       embedVar.add_field(name = 'Female : @Female', value = "React with ♀️", inline=False)
       
       r = await message.channel.send(embed = embedVar)
       await r.add_reaction("♂️")
       await r.add_reaction("♀️")
    
    if message.content.startswith('/apod'):

        NASA_API_KEY = 'Mr5ooLbGFiNdG3BpJTnlHLnXkwl9n50KSW6bdrMP'
        NASA_APOD_URL = 'https://api.nasa.gov/planetary/apod'

        async with aiohttp.ClientSession() as session:
            async with session.get(NASA_APOD_URL, params={'api_key': NASA_API_KEY}) as response:
                if response.status == 200:
                    data = await response.json()
                    title = data.get('title', 'No Title')
                    explanation = data.get('explanation', 'No Explanation')
                    image_url = data.get('url', '')

                    embed = discord.Embed(title=title, description=explanation, color=discord.Colour.dark_blue())
                    embed.set_image(url=image_url)
                    await message.channel.send(embed = embed)

                else:
                    await message.channel.send('Failed to retrieve APOD. Please try again later.')

    
    if message.content.startswith('/picture'):
       
        NASA_API_KEY = 'Mr5ooLbGFiNdG3BpJTnlHLnXkwl9n50KSW6bdrMP'
        NASA_IMAGES_URL = 'https://images-api.nasa.gov/search'

        query = message.content[len('/picture '):].strip()
            
        if not query:
            await message.channel.send('Please provide a search query.')
            return

        async with aiohttp.ClientSession() as session:
            try:
                params = {'q': query, 'media_type': 'image'}
                headers = {'User-Agent': 'DiscordBot (your-email@example.com)'}
                async with session.get(NASA_IMAGES_URL, params=params, headers=headers) as response:
                    if response.status == 200:
                        data = await response.json()
                        items = data.get('collection', {}).get('items', [])

                        if items:
                            # Randomly select an image result
                            item = random.choice(items)
                            image_url = item.get('links', [])[0].get('href', '')
                            title = item.get('data', [])[0].get('title', 'No Title')
                            description = item.get('data', [])[0].get('description', 'No Description')

                            embed = discord.Embed(title=title, description=description, color=discord.Colour.dark_gold())
                            embed.set_image(url=image_url)
                            await message.channel.send(embed=embed)
                        else:
                            await message.channel.send('No images found for the given query.')
                    else:
                        await message.channel.send(f'Failed to retrieve images. Status code: {response.status}')
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send('An error occurred while retrieving images. Please try again later.')



keep_alive()

try:
  token = os.getenv('TOKEN')
  if token == "":
    raise Exception("Please add your token to the Secrets pane.")
  client.run(token)
except discord.HTTPException as e:
  if e.status == 429:
    print(
        "The Discord servers denied the connection for making too many requests"
    )
    print(
        "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
    )
  else:
    raise e
  
