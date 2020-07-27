import os

for filename in os.listdir('./cmds'):
    print("1")
    if filename.endswith('.py'):
        print("2")
        bot.load_extension(f'cmds.{filename[:-3]}')
        print("3")