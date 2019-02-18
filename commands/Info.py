import discord
from discord.ext import commands


class Info:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def info(self, ctx):
        info_embed = discord.Embed(
            color=0x36393E
        )

        info_embed.set_author(name="Bot Info", icon_url=ctx.message.author.avatar_url)
        info_embed.add_field(name="Bot Developer", value="<@287682736104275968>", inline=True)
        info_embed.add_field(name="Support Server", value="[Click here](https://discord.gg/wD6BuEn)", inline=True)
        info_embed.add_field(name="Invite Me", value="[Click here](https://discordapp.com/oauth2/authorize?client_id=546120797266116620&permissions=10240&scope=bot)", inline=True)
        info_embed.add_field(name="About me:", value="`I am a simple chat filter to keep the server clean and friendly!`")
        info_embed.set_footer(text="{} | {}".format(ctx.message.guild.name, ctx.message.created_at), icon_url=ctx.message.guild.icon_url)

        await ctx.message.channel.send(embed=info_embed)


def setup(client):
    client.add_cog(Info(client))
