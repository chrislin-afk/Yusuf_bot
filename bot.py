# bot.py
import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    quotes = [
        'The jungle used to have integrity',
        '4 dozen? Thats like 36',
        'I feel like I have to put in 30 hours a day man',
        'nigha is so bored in class dam',
        'have you ever fucc a bitch ass so fat lose yo balance',
        'gon make plans wit ppls around then and hit ye up if ur intreseted in stuff',
        'demi fine ass bih off the H',
        'drake a yung king',
        'corey on these milfs',
        'fired ty lue no more memes, fired championship coach cleveland is a fucking shitter franchise and they are 0-6',
        'gavins dad can probably dm heron preston and get sent a nasa hoodie',
        'nigga..we on NAV',
        'u tryna chill today tho',
        'yall playin fortnite',
        'I worked so hard !!',
        'think critically',
        'crs to worlds',
        'could be the best album since mozart and beetoven',
        'yall rdy new nav tonight could b decade changing',
        'any1 wanna start a new oldschool rs acct',
        'some of us recognize the deals $1 for 10 nuggets at wendys',
        'im EATING',
        'havent tasted a league win in many yrs',
        'still thinking about my 2/16 game',
        'lord yoosy got alot o groupie',
        'impale indians on top of rod of ages',
        'game is shit',
        'delete this chat',
        'drake jumps around at his shows and runs everywere doesnt get tired',
        'smoke a cig then chill wit kids at the arena',
        'tsm is real trash',
        'dum niqqas',
        'u saying im brown?',
        'wat is green beer made out of',
        'dam they wont even let these prison nigs outside for st pattys',
        'i only love skipping the mosqe and drinking natty im sorry',
        'nah we about scoping niqqas down',
        'chineses r crazy',
        'red dot sight ar 15',
        'hey can i get upvotes plz im being bullied',
        'i will eat my cat',
        'i won an aram last night',
        'im gomna go call ppl niggers in aram until i get permd',
        'i called up the muslims',
        'were u be i need diablo boost',
        'u think ima ride a rollercoster and get my feet chopped off',
        'ye i need scar jo bath water',
        'https://i.imgur.com/SOIx5oO.gif',
        'wish i could eat a thicc bitch ass after 3 hrs on elliptical',
        'im a small nigga',
        'DAM thats alot of hot n spicys',
        'non binary what that mean',
        'killl whites',
        'hey this is too many msgs for our ded grp',
        'hang these nuts plz',
        'where th FUCK is yandhi',
        'bruh how joji be having mils of views on his music but they dont know this dude ate a hair cake',
        'there is a diablo season on friday',
        'chat dead as brix delete this server',
        'rly im tryna watch PORNO wit ppls'






























    ]

    if message.content == 'islam':
        response = random.choice(quotes)
        await message.channel.send(response)
    
    
    temp = []
    for i in range(len(quotes)):
        if message.content in quotes[i]:
            temp.append(quotes[i])
    response = random.choice(temp)
    await message.channel.send(response)
    temp = []




client.run(TOKEN)
