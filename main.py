import os
import sys

import discord
import requests

import api

client = discord.Client()


help_message = discord.Embed(
    title="List of commands",
    description="`!pcats random` -> shows a random cat picture",
)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user or not message.content.startswith("!pcats"):
        return

    try:
        print(
            "command [%s] sent by user %s in channel %s from guild %s"
            % (message.content, message.author, message.channel, message.guild)
        )

        command = message.content.split()
        if len(command) == 1:
            await message.channel.send(embed=help_message)
        else:
            if command[1] == "random":
                cat_image_url = api.get_random_photo_url()
                await message.channel.send(
                    cat_image_url,
                    reference=message,
                )
            else:
                await message.channel.send(embed=help_message)

    except requests.exceptions.HTTPError:
        await message.channel.send(
            "An error has ocurred with our cat images provider. Please try again later"
        )

    except Exception as exception:
        await message.channel.send("An unknown error has ocurred.")
        print(exception, file=sys.stderr)


token = os.getenv("DISCORD_TOKEN")
if not token:
    raise SystemExit("No valid token provided")

client.run(token)
