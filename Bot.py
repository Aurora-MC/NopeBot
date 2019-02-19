import discord
from discord.ext import commands
import asyncio
import json
import time
from itertools import cycle

client = commands.Bot(command_prefix=".")
client.remove_command("help")

token = " "
invite_Link = "https://discordapp.com/api/oauth2/authorize?client_id=546120797266116620&permissions=10240&scope=bot"

server_count = []
member_count = []

info = "[Server thread/INFO]:"
notice = "[Server thread/NOTICE]:"
warning = "[Server thread/WARNING]:"

extensions = [
    "commands.Help",
    "commands.Info",
    "commands.Ping"
]

with open('config/blacklist_words.json', 'r') as f:
    blacklist_words = json.load(f)


@client.event
async def on_ready():
    print(info + " Preparing Bot Extensions!\n")

    if __name__ == "__main__":
        for extension in extensions:
            try:
                client.load_extension(extension)
                print(notice + " Loaded {} Sucsessfully".format(extension))
            except Exception as error:
                print(warning + " {} Could not be loaded: [{}]".format(extension, error))

    for server in client.guilds:
        server_count.append(server)

        for member in server.members:
            member_count.append(member)

    print("\n" + info + " Bot is online in {} Server(s)".format(len(server_count)))
    print(info + " Serving {} members across Discord".format(len(member_count)))
    await change_status()


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return


@client.event
async def on_message(message):
    try:
        await client.process_commands(message)
    except discord.ext.commands.errors.CommandNotFound:
        return

    user_message = message.content.split(" ")
    for word in user_message:
        if word.lower() in blacklist_words["words"]:
            await message.delete()
            await message.channel.send("**__Please watch your language!__**")


# Changes the bots profile status

async def change_status():
    status_messages = [
        "{} members".format(len(member_count)),
        ".help -> for commands! <3"
    ]

    messages = cycle(status_messages)

    while not client.is_closed():
        msg = next(messages)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=msg), status=discord.Status.dnd, afk=False)
        await asyncio.sleep(5)


while True:
    try:
        client.loop.run_until_complete(client.start(token))
    except BaseException:
        time.sleep(5)
