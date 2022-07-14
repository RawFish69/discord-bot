import hikari
import lightbulb

plugin = lightbulb.Plugin('Example')

@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_msg(event):
    print(event.content)

@plugin.command
@lightbulb.command('help', 'All the help you need')
@lightbulb.implements(lightbulb.SlashCommand)
async def help(ctx):
    await ctx.respond('Help page is currently empty')

@plugin.command
@lightbulb.command('save', 'Manage save files')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def log_group(ctx):
    pass

@log_group.child()
@lightbulb.option('name', 'Username')
@lightbulb.command('create', 'Create the log file')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def create(ctx):
    username = ctx.options.name
    level = 1
    BP = 0 #based power
    with open('log_file_{}.txt'.format(username), 'w') as log:
        log.write('Player ID: ' + username + '\n')
        log.write('Level: ' + str(level) + '\n')
        log.write('Based Power: ' + str(BP) + '\n')
    await ctx.respond('Log file successfully generated.')
    await ctx.respond('Player name: {}\n'.format(username) +
                      'Level: {}\n'.format(level) +
                      'Based Power: {}'.format(BP))

@log_group.child()
@lightbulb.option('name', 'Your username')
@lightbulb.command('load', 'Load your saved files with username')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def read(ctx):
    with open('log_file_{}.txt'.format(ctx.options.name), 'r') as reader:
        for line in reader:
            part = line.strip()
            part = line.split(': ')
            if part[0] == 'Player ID':
                saved_name = part[1]
            elif part[0] == 'Level':
                saved_level = part[1]
            elif part[0] == 'Based Power':
                saved_BP = part[1]

    await ctx.respond('Save filed loaded successfully.\n' +
                      'Username: {}'.format(saved_name) +
                      'Level: {}'.format(saved_level) +
                      'Based Power: {}'.format(saved_BP))
    return saved_name, saved_level, saved_BP




def load(bot):
    bot.add_plugin(plugin)


