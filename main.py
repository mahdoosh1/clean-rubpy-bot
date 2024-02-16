from rubpy import Client, filters, utils;from rubpy.types import Updates;bot = Client(name='rubpy')
(@bot.on_message_updates(filters.text)
async def updates(update: Updates):print(update);await update.reply(utils.Code('hello') + utils.Underline('from') + utils.Bold('rubpy')));bot.run()
