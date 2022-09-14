from vkbottle.bot import Message, Blueprint
from vkbottle import Keyboard, KeyboardButtonColor, \
                        Text
from Pars import Pars

bp = Blueprint("For chat commands")

@bp.on.message(text="меню")
async def answer(message: Message):
    await message.answer("Для отображения кнопок введите /меню")

@bp.on.message(text="/меню")
@bp.on.message(payload={"cmd": "back"})
async def handler(message: Message):
    keyboard = Keyboard(one_time=True)
    keyboard.add(Text("Полезные ссылки",{"cmd": "links"}), color=KeyboardButtonColor.POSITIVE)
    keyboard.row()
    keyboard.add(Text("Расписание", {"cmd": "timetable"}), color=KeyboardButtonColor.POSITIVE)
    keyboard.row()
    keyboard.add(Text("Скрыть кнопки", {"cmd": "hide"}), color=KeyboardButtonColor.NEGATIVE)
    await message.answer("menu", keyboard=keyboard)


@bp.on.message(payload={"cmd": "links"})
async def timetable_handler(message: Message):
    keyboard = Keyboard(one_time=True)
    keyboard.add(Text("Учебный план",{"cmd": "academic plan"}), color=KeyboardButtonColor.POSITIVE)
    keyboard.row()
    keyboard.add(Text("Расписание",{"cmd": "tt"}), color=KeyboardButtonColor.POSITIVE)
    keyboard.row()
    keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
    await message.answer("Расписание", keyboard=keyboard)

@bp.on.message(payload={"cmd": "hide"})
async def timetable_today(message: Message):
    await message.answer("Кнопки скрыты")

@bp.on.message(payload={"cmd": "academic plan"})
async def timetable_today(message: Message):
    await message.answer("https://up.tpu.ru/view/detali.html?id=24167")

@bp.on.message(payload={"cmd": "tt"})
async def timetable_today(message: Message):
    await message.answer("https://rasp.tpu.ru/site/department.html?id=7863")

@bp.on.message(payload={"cmd": "timetable"})
async def timetable_handler(message: Message):
    keyboard = Keyboard(one_time=True)
    keyboard.add(Text("Расписание на сегодня",{"cmd": "today"}), color=KeyboardButtonColor.POSITIVE)
    keyboard.row()
    keyboard.add(Text("Расписание на завтра",{"cmd": "tomorrow"}), color=KeyboardButtonColor.POSITIVE)
    keyboard.row()
    keyboard.add(Text("Расписание на эту неделю",{"cmd": "this week"}), color=KeyboardButtonColor.POSITIVE)
    keyboard.row()
    keyboard.add(Text("Расписание на следущую неделю",{"cmd": "next week"}), color=KeyboardButtonColor.POSITIVE)
    keyboard.row()
    keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
    await message.answer("f", keyboard=keyboard)


@bp.on.message(payload={"cmd": "today"})
async def timetable_today(message: Message):
    pars = Pars()
    L=pars.timetable_today()
    for i in L:
        await message.answer(i)

@bp.on.message(payload={"cmd": "tomorrow"})
async def timetable_tomorrow(message: Message):
    pars = Pars()
    L=pars.timetable_tommorow()
    for i in L:
        await message.answer(i)

@bp.on.message(payload={"cmd": "this week"})
async def timetable_thisweek(message: Message):
    pars = Pars()
    Listday=["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота"]
    for j in range(0,6):
        await message.answer(Listday[j])
        L=pars.thisweek(j)
        for i in L:
            await message.answer(i)

@bp.on.message(payload={"cmd": "next week"})
async def timetable_nextweek(message: Message):
    pars = Pars()
    Listday=["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота"]
    for j in range(0,6):
        await message.answer(Listday[j])
        L=pars.nextweek(j)
        for i in L:
            await message.answer(i)

