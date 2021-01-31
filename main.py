import discord
import os
import requests
import json
from keep_alive import keep_alive

#from reprlib import db
# this to use replit dataBase but I didn't need it here


client = discord.Client()

#a function that returns quotes from "zenquotes" API
def get_quote():
  response=requests.get("https://zenquotes.io/api/random")
  # a variable to store the response in a json array
  json_data=json.loads(response.text)
  # a modifier to take the quote and its author only
  quote=json_data[0]['q']+" -"+json_data[0]['a']
  return(quote)


# event when the bot starts it prints its name on the server terminal
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# interacting with user's commands
@client.event
async def on_message(message):
  # to do nothing if the message is written by the bot itself
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$7bb'):
        await message.channel.send('2lbyyy!')

    if message.content.startswith('$inspire'):
        quote=get_quote()
        await message.channel.send(quote)

#to run the web server
keep_alive()

#to run our bot knowing its TOKEN from .env which refers to environment variables
client.run(os.getenv('TOKEN'))