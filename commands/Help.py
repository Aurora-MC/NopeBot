import discord
from discord.ext import commands


class Help:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def help(self, ctx):

        help_embed = discord.Embed(
            color = 0x36393E
        )

        help_embed.set_author(name="{} | Server help page".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        help_embed.add_field(name=".ping", value="View Bots ping `ms`", inline=True)
        help_embed.add_field(name=".info", value="Shows info about this bot", inline=True)
        help_embed.set_footer(text="{} | {}".format(ctx.message.guild.name, ctx.message.created_at), icon_url=ctx.message.guild.icon_url)

        await ctx.message.channel.send(embed=help_embed)


def setup(client):
    client.add_cog(Help(client))


