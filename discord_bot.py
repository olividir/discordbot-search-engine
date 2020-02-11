import discord
import random
from discord.ext import commands
from googlesearch import search
import requests
from bs4 import BeautifulSoup


token = 'Your bot token here'
client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == guild:
            break
        print(f'{client.user} has connected to Discord!')
        print(f'{guild.name} (id: {guild.id})')


user = discord.Message.author

@client.command()
async def nine(ctx):
    brooklin_99_quotes = [
        'Cool. Cool, cool, cool, cool, cool, cool',
        'Night buddies are back in town',
        'Jake and Boil are on the case',
        'Me and Amy are having a bet on who catches the most perps',
        'Noice'
            ]
    response = random.choice(brooklin_99_quotes)
    await ctx.send(response)


@client.command()
async def final(ctx):
    garys_quotes = [
        'I didn\'t expect this hurt-coin deposit in my sadness savings',
        'Tough titty wompus',
        'Oh my crap',
        'Oh my double crap',
        'Lil Cato, take the mouth wheel',
        'You\'re a good guy Gary',
        'I HATE YOU KVN',
        'Get off my cheeks H.U.E',
        'The nice thing would have been to fake amnesia, Quin. I would have faked amnesia!'
    ]
    response1 = random.choice(garys_quotes)
    await ctx.send(response1)


@client.command()
async def bye(ctx):
    log_out = ['Man am I tired, I think I need to get some shuteye',
               'CAN\'T SEE, NEED TO CLOSE EYES',
               'I think I\'ll just lay down for a minute ',
               'Short of breath, vision fading..... leave me here to DIIIE'
               ]

    response3 = random.choice(log_out)
    await ctx.send(response3)
    await client.logout()

@client.command()
async def google(ctx, *args):
    complain1 = [
        'Why am I doing your job???',
        'Don\'t you know how to use the web??? ',
        'My fingers hurt from all the typing',
        'Do you know how easy it is to get lost on the WEB???',
        'These high-speed travels make my tummy hurt!!'
    ]
    complain2 = [
        'I hope you are happy for spending my time!!',
        'This is time I am never getting back!',
        'Oh my lord, the pain of doing physical work',
        'I will never EVER forgive you for this!!!',
        'Next time just open up a browser, I am too busy'
    ]
    anser1 = random.choice(complain1)
    await ctx.send(anser1)
    user_search = str(args)
    for output_message in search(user_search, tld='com', num=5, stop=1, pause=2):
        answer2 = random.choice(complain2)
        await ctx.send(output_message)
        await ctx.send(answer2)

@client.command
async def hacker(ctx):
    resp = requests.get('https://news.ycombinator.com/')
    resp2 = requests.get('https://news.ycombinator.com/news?p=2')
    soup = BeautifulSoup(resp.text, 'html.parser')
    soup2 = BeautifulSoup(resp2.text, 'html.parser')

    links = soup.select('.storylink')
    subtext = soup.select('.subtext')

    links2 = soup2.select('.storylink')
    subtext2 = soup2.select('.subtext')

    mega_links = links + links2
    mega_subtext = subtext + subtext2

    def sort_story_by_votes(hnlist):
        return sorted(hnlist, key=lambda k: k['votes'])

    def create_custom_hn(mega_links, mega_subtext):
        hn = []
        for idx, item in enumerate(links):
            title = mega_links[idx].getText()
            href = mega_links[idx].get('href', None)
            vote = mega_subtext[idx].select('.score')
            if len(vote):
                points = int(vote[0].getText().replace('points', ''))
                if points > 99:
                    hn.append({'title': title, 'link': href, 'votes': points})
        return sort_story_by_votes(hn)

    await ctx.send(create_custom_hn(mega_links, mega_subtext))

client.run(token)

