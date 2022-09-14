from vkbottle.bot import Bot
from vkbottle import load_blueprints_from_package
from config import token
from Pars import Pars

bot = Bot(token=token)

for bp in load_blueprints_from_package("blueprints"):
    bp.load(bot)
pars=Pars()
pars.today()
pars.pars_num_current_week()


bot.run_forever()