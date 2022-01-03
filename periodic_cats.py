import sys

import discord
from discord.ext import commands
import requests

import api


class PeriodicCats(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if not message.author == self.bot.user:
            print(
                "\ncommand [%s] sent by user %s in channel %s from guild %s"
                % (message.content, message.author, message.channel, message.guild)
            )

    @commands.Cog.listener()
    async def on_command_error(
        self, context: commands.Context, error: commands.CommandError
    ):
        if isinstance(error, commands.CommandNotFound):
            return
        if isinstance(error, commands.CommandInvokeError):
            print("exception: %s" % error.original, file=sys.stderr)
            if isinstance(error.original, requests.exceptions.HTTPError):
                message = "An error has ocurred with our cat images provider. Please try again later"
            else:
                message = "An unknown error has ocurred"
        else:
            message = "Something went wrong"

        await context.send(message, reference=context.message)

    @commands.command(name="random")
    async def random_cat_photo(self, context: commands.Context):
        """Shows a random cat picture"""
        cat_image_url = api.get_random_photo_url()
        await context.send(
            cat_image_url,
            reference=context.message,
        )


def setup(bot: commands.Bot):
    bot.add_cog(PeriodicCats(bot))
