"""
Welcome to your brand new nest module!
Have fun and good luck :)
"""
class Cog:
    def __init__(self, bot, command_handler):
        self.bot = bot
        self.command_handler = command_handler
        pass
def setup(bot, command_handler):
    Cog(bot, command_handler)