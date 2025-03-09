import os
import discord
import random
from typing import Final
from discord.ext import commands
from discord import Intents, Message, app_commands
from dotenv import load_dotenv
from random import choice, randint

# Loads the token from somewhere and Guild ID
load_dotenv(override=True)
TOKEN: Final = os.getenv("DISCORD_TOKEN")

# bot setup, the basics
intents: Intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="m!", intents=intents)

# Main bosses with short responses
BOSS_RESPONSES = {
    "margit": "Fell Omen, vanquished.",
    "godrick": "The Grafted is no more.",
    "rennala": "Queen of the Full Moon fades.",
    "radahn": "Stars resume their course.",
    "morgott": "The Veiled Monarch falls.",
    "firegiant": "The flame awaits.",
    "godskinduo": "The duo falls silent.",
    "maliketh": "Destined Death returns.",
    "gideon": "All-Knowing, silenced.",
    "godfrey": "First Lord, bested.",
    "radabeast": "The hammer shatters. You are Elden Lord.",
    "DBDL": "The Divine Dancing Lion rests.",
    "rellana": "The protector returns to slumber.",
    "goldenhippo": "The Golden Hippopotamus sinks beneath the waters.",
    "messmer": "Messmer's light fades to darkness.",
    "gaius": "Gaius, the Golden Knight, falls.",
    "scadutree": "The Avatar withers and crumbles.",
    "putrescent": "The Putrescent Knight's corruption is cleansed.",
    "midra": "Midra's final flame extinguished.",
    "bayle": "Bayle's strength was not enough.",
    "metyr": "Metyr returns to the shadows.",
    "romina": "Romina's final song ends.",
    "leda": "The Needle Knight's precision falters.",
    "pcr": "The Promised Consort falls beneath your might."
}

# Giving credit or append
GIVING_CREDIT = [
    "Well done, Tarnished.",
    "You have my gratitude.",
    "A fine display of strength.",
    "You walk with purpose.",
    "May your path be ever guided.",
    "You are worthy.",
    "Your resolve is strong.",
    "Grace is with you.",
    "I acknowledge your strength.",
    "You have done well."
]


# TEST 
# Prefix command
@bot.command()
async def hello(ctx):
    await ctx.send("Hello, Fellow member")

# Slash command TEST
@bot.tree.command(
    name="hello", 
    description="melina greets you",
)
async def hello(interaction: discord.Interaction):
    user_name = interaction.user.mention
    await interaction.response.send_message(f"Greetings, {user_name} the Tarnished. ")

#1
@bot.tree.command(
    name="how are you", 
    description="ask melina how her day is",
)
async def hru(interaction: discord.Interaction):
    await interaction.response.send_message("I am doing good, thank you for asking Tarnished")

#2
@bot.tree.command(
    name="are you there", 
    description="is melina with you?",
)
async def are_you_there(interaction: discord.Interaction):
    await interaction.response.send_message("I am here and with you Tarnished")

# 3
@bot.tree.command(
    name="farewell", 
    description="say your goodbye to melina your maiden",
)
async def farewell(interaction: discord.Interaction):
    await interaction.response.send_message("May your path be clear and farewell.")

# 4
@bot.tree.command(
    name="tarnished arrived", 
    description="nice welcome message from melina your maiden",
)
async def tarnished_arrived(interaction: discord.Interaction):
    await interaction.response.send_message("Welcome Tarnished to the Lands between.")

# 5 - Enhanced boss command with credit system
@bot.tree.command(
    name="i have defeated",
    description="Tell melina which boss you have bested",
)
@app_commands.describe(
    bosses="Which boss is it that you have bested?"
)
@app_commands.choices(bosses=[
    app_commands.Choice(name="Margit", value="margit"),
    app_commands.Choice(name="Godrick", value="godrick"),
    app_commands.Choice(name="Rennala", value="rennala"),
    app_commands.Choice(name="Radahn", value="radahn"),
    app_commands.Choice(name="Morgott", value="morgott"),
    app_commands.Choice(name="Fire Giant", value="firegiant"),
    app_commands.Choice(name="God Skin Duo", value="godskinduo"),
    app_commands.Choice(name="Maliketh", value="maliketh"),
    app_commands.Choice(name="Gideon", value="gideon"),
    app_commands.Choice(name="Godfrey", value="godfrey"),
    app_commands.Choice(name="Radagon and Elden Beast", value="radabeast"),
    app_commands.Choice(name="Divine Beast Dancing Lion", value="DBDL"),
    app_commands.Choice(name="Rellana", value="rellana"),
    app_commands.Choice(name="Golden Hippopotamus", value="goldenhippo"),
    app_commands.Choice(name="Messmer", value="messmer"),
    app_commands.Choice(name="Gaius", value="gaius"),
    app_commands.Choice(name="Scadutree Avatar", value="scadutree"),
    app_commands.Choice(name="Putrescent knight", value="putrescent"),
    app_commands.Choice(name="Midra", value="midra"),
    app_commands.Choice(name="Bayle", value="bayle"),
    app_commands.Choice(name="Metyr", value="metyr"),
    app_commands.Choice(name="Romina", value="romina"),
    app_commands.Choice(name="Needle Knight Leda", value="leda"),
    app_commands.Choice(name="Promised Consort Radahn", value="pcr")
])
async def bosses_command(interaction: discord.Interaction, bosses: str):
    # Get the main response for the boss
    boss_response = BOSS_RESPONSES.get(bosses, "A worthy opponent has fallen.")
    
    # Add a random credit message
    credit = random.choice(GIVING_CREDIT)
    
    # Combine the messages
    full_response = f"{boss_response} {credit}"
    
    await interaction.response.send_message(full_response)

# 6 - Roll dice command
@bot.tree.command(
    name="roll_dice",
    description="Roll a dice and see your fortune",
)
async def roll_dice(interaction: discord.Interaction):
    dice_result = randint(1, 6)
    await interaction.response.send_message(f"You rolled a {dice_result}. Fortune favors you.")

# Event handlers
@bot.event
async def on_ready():
    try:
        # Sync commands only to the test server
        await bot.tree.sync()
        print(f"Logged in as {bot.user}")
        print(f"Connected to {len(bot.guilds)} guild(s)")
        for guild in bot.guilds:
            print(f"- {guild.name} (ID: {guild.id})")
        print("Bot is ready!")
    except Exception as e:
        print(f"Error syncing commands: {e}")

@bot.event
async def on_message(message: Message):
    if message.author == bot.user:
        return

    # Log messages
    print(f"[{message.channel}] {message.author}: {message.content}")
    
    # Process commands
    await bot.process_commands(message)

# Run the bot
if __name__ == "__main__":
    try:
        bot.run(TOKEN)
    except Exception as e:
        print(f"Error running bot: {e}")