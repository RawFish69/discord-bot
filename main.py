# bot

import hikari
import lightbulb
import randomhttps://github.com/RawFish69/discord-bot/blob/main/main.py

bot = lightbulb.BotApp(
    token='',
    default_enabled_guilds=(996653472575397918, 434168318128160768)
)

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_event(event):
    print(event.content)

@bot.listen(hikari.StartedEvent)
async def bot_start(event):
    print('I pull up.')

@bot.command
@lightbulb.command('hi', 'say hello back')
@lightbulb.implements(lightbulb.SlashCommand)
async def print_hello(ctx):
    await ctx.respond('hello')

@bot.command
@lightbulb.command('facts', 'a random based fact')
@lightbulb.implements(lightbulb.SlashCommand)
async def print_facts(ctx):
    based_facts = ['The based department is the global organization for all the based individuals on this planet. It is based on the Two-things theory, the head of the department is the CBO. The CBO is straight and based, which means he is straight-up based, CBO stays flexing at all times.',
                   'Treat a bitch like a celebrity, and she’ll treat you like a fan, treat a bitch like a dog, she’ll treat you like an owner and always stay loyal',
                   'The first CBO was named after Sir. Yahoo 69 MD (*where MD stands for Massive Dick)',
                   'If there are a million people saying hello unique sora, then I am one of them. If there are ten people saying hello unique sora , then I am one of them. If there is only one person saying hello unique sora, that is me. If no one is saying hello unique sora, then that means I am no longer on earth. If the world is against unique sora, then I am against the world.',
                   'From the streets did she emerge, and to the streets she will return. And I say unto you, she is for the streets. So be not weary, when she must return from whence she came',
                   'It\'s hard for me to take you seriously when I know what\'s been in that mouth of yours',
                   'There are no chicks with dicks, only guys with tits'
                   ]
    await ctx.respond(based_facts[random.randint(0, 6)])

@bot.command
@lightbulb.command('start', 'Based Activities')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def start(ctx):
    pass

@start.child()
@lightbulb.command('roll', 'Roll a dice')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def roll_dice(ctx):
    dice_num = random.randint(1,6)
    await ctx.respond('The number you rolled is **{}**!'.format(dice_num))

@start.child()
@lightbulb.option('number', 'Numbers of dice you are rolling (0-30)', type=int)
@lightbulb.command('rolls', 'Roll multiple dices')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def rolls(ctx):
    roll_count = ctx.options.number
    roll_sum = 0
    for i in range(roll_count):
        random_roll = random.randint(1,6)
        await ctx.respond('You rolled **{}**!'.format(random_roll))
        roll_sum += random_roll
        i += 1
    await ctx.respond('Dice rolled: **{}** \nThe Sum: **{}**'.format(roll_count, roll_sum))


@bot.command
@lightbulb.command('dps', 'damage calculations')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def dps(ctx):
    pass

@dps.child()
@lightbulb.command('armor', 'calculates armor dps with crazy math')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def armor(ctx):
    await ctx.respond('armor dps does not exist you tard')

@dps.child()
@lightbulb.option('tier', 'Attack Speed multiplier', type=float)
@lightbulb.option('base', 'Base of the weapon', type=int)
@lightbulb.command('weapon', 'Calculates the DPS')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def weap_dps(ctx):
    average_dps = ctx.options.base * ctx.options.tier
    await ctx.respond('Effective DPS: {}'.format(average_dps))
    return average_dps

bot.run()

