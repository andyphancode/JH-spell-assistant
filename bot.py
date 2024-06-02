import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import jamspell

# Load environment variables from .env file
load_dotenv()
# Get the bot token from the environment variables
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Initialize jamspell
corrector = jamspell.TSpellCorrector()
corrector.LoadLangModel('en.bin')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)



@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def commands(ctx):
    await ctx.send("""This is JH bot at your service, ready to figure out whatever your friend typed.\nHere are my available commands:\n```!commands: Get a list of commands\n\n!fix: Use this command and follow it up with any text to autocorrect it. For example sending [!fix helol eveyrone] without the brackets would result in me sending a message with the autocorrected response: hello everyone\n\n!re: Reply to a message with this command to autocorrect the message you replied to. For example, replying to a message that says [helol eveyrone] with !re would result in me sending a message with the autocorrected response: hello everyone\n\n!secret: Reply to a message with this command and see what happens! ```""")

@bot.command()
async def fix(ctx, *, sentence: str):
    # Correct the sentence using JamSpell
    corrected_sentence = corrector.FixFragment(sentence)
    await ctx.send(f"The message you are correcting is:\n ```{sentence}```\n This is what I think it is:\n```{corrected_sentence}```")

@bot.command()
async def re(ctx):
    # Check if the message is a reply
    if ctx.message.reference is None:
        await ctx.send("Please reply to a message you want to correct. This command only works with replies.")
        return

    # Fetch the referenced message
    referenced_message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
    sentence = referenced_message.content

    # Correct the sentence using JamSpell
    corrected_sentence = corrector.FixFragment(sentence)

    # Send the corrected sentence
    await ctx.send(f"The user you are correcting sent:\n```{sentence}```\nThis is what I think it means:\n```{corrected_sentence}```")



bot.run(TOKEN)
