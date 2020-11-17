from bs4 import BeautifulSoup
import requests
import random
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.types import InputFile

key = '1312468545:AAFdSsAauFxUoIA0BG7xh6bIIMU5i0DWahk'

bot = Bot(token=key, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

url = 'https://www.akchabar.kg/ru/exchange-rates/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
text = []

for i in soup.select('td'):
    text.append(i.get_text())

button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='РСК'),
            KeyboardButton(text='FINCA'),
            KeyboardButton(text='Бай-Тушум')
        ],
        [
            KeyboardButton(text='KICB'),
            KeyboardButton(text='Моссовет'),
            KeyboardButton(text='Оптима')
        ],
        [
            KeyboardButton(text='Азии'),
            KeyboardButton(text='КЫРГЫЗСТАН'),
            KeyboardButton(text='Демир')
        ],
        [
            KeyboardButton(text='Кыргызкоммерцбанк'),
            KeyboardButton(text='Керемет')
        ]
    ], resize_keyboard=True
)

optima = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='USD', callback_data='optima_usd'),
            InlineKeyboardButton(text='EUR', callback_data='optima_eur')
        ], [
            InlineKeyboardButton(text='RUB', callback_data='optima_rub'),
            InlineKeyboardButton(text='KZT', callback_data='optima_kzt')
        ]
    ]
)

rsk = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='USD', callback_data='rsk_usd'),
            InlineKeyboardButton(text='EUR', callback_data='rsk_eur')
        ], [
            InlineKeyboardButton(text='RUB', callback_data='rsk_rub'),
            InlineKeyboardButton(text='KZT', callback_data='rsk_kzt')
        ]
    ]
)

finca = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='USD', callback_data='finca_usd'),
            InlineKeyboardButton(text='EUR', callback_data='finca_eur')
        ], [
            InlineKeyboardButton(text='RUB', callback_data='finca_rub'),
            InlineKeyboardButton(text='KZT', callback_data='finca_kzt')
        ]
    ]
)

bai = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='USD', callback_data='bai_usd'),
            InlineKeyboardButton(text='EUR', callback_data='bai_eur')
        ], [
            InlineKeyboardButton(text='RUB', callback_data='bai_rub'),
            InlineKeyboardButton(text='KZT', callback_data='bai_kzt')
        ]
    ]
)

kicb = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='USD', callback_data='kicb_usd'),
            InlineKeyboardButton(text='EUR', callback_data='kicb_eur')
        ], [
            InlineKeyboardButton(text='RUB', callback_data='kicb_rub'),
            InlineKeyboardButton(text='KZT', callback_data='kicb_kzt')
        ]
    ]
)

kkb = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='USD', callback_data='kkb_usd'),
            InlineKeyboardButton(text='EUR', callback_data='kkb_eur')
        ], [
            InlineKeyboardButton(text='RUB', callback_data='kkb_rub'),
            InlineKeyboardButton(text='KZT', callback_data='kkb_kzt')
        ]
    ]
)

mossovet = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='USD', callback_data='mossovet_usd'),
            InlineKeyboardButton(text='EUR', callback_data='mossovet_eur')
        ], [
            InlineKeyboardButton(text='RUB', callback_data='mossovet_rub'),
            InlineKeyboardButton(text='KZT', callback_data='mossovet_kzt')
        ]
    ]
)

asia = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='USD', callback_data='asia_usd'),
            InlineKeyboardButton(text='EUR', callback_data='asia_eur')
        ], [
            InlineKeyboardButton(text='RUB', callback_data='asia_rub'),
            InlineKeyboardButton(text='KZT', callback_data='asia_kzt')
        ]
    ]
)

kg = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='USD', callback_data='kg_usd'),
            InlineKeyboardButton(text='EUR', callback_data='kg_eur')
        ], [
            InlineKeyboardButton(text='RUB', callback_data='kg_rub'),
            InlineKeyboardButton(text='KZT', callback_data='kg_kzt')
        ]
    ]
)

demir = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='USD', callback_data='demir_usd'),
            InlineKeyboardButton(text='EUR', callback_data='demir_eur')
        ], [
            InlineKeyboardButton(text='RUB', callback_data='demir_rub'),
            InlineKeyboardButton(text='KZT', callback_data='demir_kzt')
        ]
    ]
)

keremet = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='USD', callback_data='keremet_usd'),
            InlineKeyboardButton(text='EUR', callback_data='keremet_eur')
        ], [
            InlineKeyboardButton(text='RUB', callback_data='keremet_rub'),
            InlineKeyboardButton(text='KZT', callback_data='keremet_kzt')
        ]
    ]
)


@dp.message_handler(text='/start')
async def get_about(message: types.Message):
    await message.answer('Выберите любой Банк', reply_markup=button)


@dp.message_handler(text='РСК')
async def get_rsk(message: types.Message):
    await message.answer(text='Выбрали РСК банк', reply_markup=ReplyKeyboardRemove())
    await message.answer(text='Tеперь выберите желаемую валюту', reply_markup=rsk)


@dp.message_handler(text='FINCA')
async def get_finca(message: types.Message):
    await message.answer(text='Выбрали FINCA банк', reply_markup=ReplyKeyboardRemove())
    await message.answer(text='Tеперь выберите желаемую валюту', reply_markup=finca)


@dp.message_handler(text='Кыргызкоммерцбанк')
async def get_kkb(message: types.Message):
    await message.answer(text='Выбрали Кыргызкоммерцбанк банк', reply_markup=ReplyKeyboardRemove())
    await message.answer(text='Tеперь выберите желаемую валюту', reply_markup=kkb)


@dp.message_handler(text='KICB')
async def get_kicb(message: types.Message):
    await message.answer(text='Выбрали KICB банк', reply_markup=ReplyKeyboardRemove())
    await message.answer(text='Tеперь выберите желаемую валюту', reply_markup=kicb)


@dp.message_handler(text='Моссовет')
async def get_mossovet(message: types.Message):
    await message.answer(text='Выбрали Моссовет банк', reply_markup=ReplyKeyboardRemove())
    await message.answer(text='Tеперь выберите желаемую валюту', reply_markup=mossovet)


@dp.message_handler(text='Оптима')
async def get_optima(message: types.Message):
    await message.answer(text='Выбрали Оптима банк', reply_markup=ReplyKeyboardRemove())
    await message.answer(text='Tеперь выберите желаемую валюту', reply_markup=optima)


@dp.message_handler(text='Азия')
async def get_asia(message: types.Message):
    await message.answer(text='Выбрали Азия банк', reply_markup=ReplyKeyboardRemove())
    await message.answer(text='Tеперь выберите желаемую валюту', reply_markup=asia)


@dp.message_handler(text='КЫРГЫЗСТАН')
async def get_kg(message: types.Message):
    await message.answer(text='Выбрали КЫРГЫЗСТАН банк', reply_markup=ReplyKeyboardRemove())
    await message.answer(text='Tеперь выберите желаемую валюту', reply_markup=kg)


@dp.message_handler(text='Демир')
async def get_demir(message: types.Message):
    await message.answer(text='Выбрали Демир банк', reply_markup=ReplyKeyboardRemove())
    await message.answer(text='Tеперь выберите желаемую валюту', reply_markup=demir)


@dp.message_handler(text='Бай-Тушум')
async def get_bai(message: types.Message):
    await message.answer(text='Выбрали Бай-Тушум банк', reply_markup=ReplyKeyboardRemove())
    await message.answer(text='Tеперь выберите желаемую валюту', reply_markup=bai)


@dp.message_handler(text='Керемет')
async def get_keremet(message: types.Message):
    await message.answer(text='Выбрали Керемет банк', reply_markup=ReplyKeyboardRemove())
    await message.answer(text='Tеперь выберите желаемую валюту', reply_markup=keremet)

# 
#  USD
# 


@dp.callback_query_handler(text='rsk_usd')
async def rsk_usd(call: CallbackQuery):
    await call.message.answer('Курс USD \n Покупка {} \n Продажа {}'.format(text[7], text[8]))

@dp.callback_query_handler(text='finca_usd')
async def finca_usd(call: CallbackQuery):
    await call.message.answer('Курс USD \n Покупка {} \n Продажа {}'.format(text[31], text[32]))

@dp.callback_query_handler(text='kkb_usd')
async def kkb_usd(call: CallbackQuery):
    await call.message.answer('Курс USD \n Покупка {} \n Продажа {}'.format(text[34], text[35]))

@dp.callback_query_handler(text='kicb_usd')
async def kicb_usd(call: CallbackQuery):
    await call.message.answer('Курс USD \n Покупка {} \n Продажа {}'.format(text[16], text[17]))

@dp.callback_query_handler(text='mossovet_usd')
async def mossovet_usd(call: CallbackQuery):
    await call.message.answer('Курс USD \n Покупка {} \n Продажа {}'.format(text[13], text[14]))

@dp.callback_query_handler(text='optima_usd')
async def optima_usd(call: CallbackQuery):
    await call.message.answer('Курс USD \n Покупка {} \n Продажа {}'.format(text[4], text[5]))

@dp.callback_query_handler(text='asia_usd')
async def asia_usd(call: CallbackQuery):
    await call.message.answer('Курс USD \n Покупка {} \n Продажа {}'.format(text[19], text[20]))

@dp.callback_query_handler(text='kg_usd')
async def kg_usd(call: CallbackQuery):
    await call.message.answer('Курс USD \n Покупка {} \n Продажа {}'.format(text[10], text[11]))

@dp.callback_query_handler(text='demir_usd')
async def demir_usd(call: CallbackQuery):
    await call.message.answer('Курс USD \n Покупка {} \n Продажа {}'.format(text[22], text[23]))

@dp.callback_query_handler(text='bai_usd')
async def bai_usd(call: CallbackQuery):
    await call.message.answer('Курс USD \n Покупка {} \n Продажа {}'.format(text[25], text[26]))

@dp.callback_query_handler(text='keremet_usd')
async def keremet_usd(call: CallbackQuery):
    await call.message.answer('Курс USD \n Покупка {} \n Продажа {}'.format(text[7], text[8]))

# 
#  EURO
# 


@dp.callback_query_handler(text='rsk_eur')
async def rsk_eur(call: CallbackQuery):
    await call.message.answer('Курс EURO \n Покупка {} \n Продажа {}'.format(text[43], text[44]))

@dp.callback_query_handler(text='finca_eur')
async def finca_eur(call: CallbackQuery):
    await call.message.answer('Курс EURO \n Покупка {} \n Продажа {}'.format(text[67], text[68]))

@dp.callback_query_handler(text='kkb_eur')
async def kkb_eur(call: CallbackQuery):
    await call.message.answer('Курс EURO \n Покупка {} \n Продажа {}'.format(text[70], text[71]))

@dp.callback_query_handler(text='kicb_eur')
async def kicb_eur(call: CallbackQuery):
    await call.message.answer('Курс EURO \n Покупка {} \n Продажа {}'.format(text[52], text[53]))

@dp.callback_query_handler(text='mossovet_eur')
async def mossovet_eur(call: CallbackQuery):
    await call.message.answer('Курс EURO \n Покупка {} \n Продажа {}'.format(text[49], text[50]))

@dp.callback_query_handler(text='optima_eur')
async def optima_eur(call: CallbackQuery):
    await call.message.answer('Курс EURO \n Покупка {} \n Продажа {}'.format(text[40], text[41]))

@dp.callback_query_handler(text='asia_eur')
async def asia_eur(call: CallbackQuery):
    await call.message.answer('Курс EURO \n Покупка {} \n Продажа {}'.format(text[55], text[56]))

@dp.callback_query_handler(text='kg_eur')
async def kg_eur(call: CallbackQuery):
    await call.message.answer('Курс EURO \n Покупка {} \n Продажа {}'.format(text[46], text[47]))

@dp.callback_query_handler(text='demir_eur')
async def demir_eur(call: CallbackQuery):
    await call.message.answer('Курс EURO \n Покупка {} \n Продажа {}'.format(text[58], text[59]))

@dp.callback_query_handler(text='bai_eur')
async def bai_eur(call: CallbackQuery):
    await call.message.answer('Курс EURO \n Покупка {} \n Продажа {}'.format(text[61], text[62]))

@dp.callback_query_handler(text='keremet_eur')
async def keremet_eur(call: CallbackQuery):
    await call.message.answer('Курс EURO \n Покупка {} \n Продажа {}'.format(text[64], text[65]))

# 
#  RUB
# 

@dp.callback_query_handler(text='rsk_rub')
async def rsk_rub(call: CallbackQuery):
    await call.message.answer('Курс RUB \n Покупка {} \n Продажа {}'.format(text[79], text[80]))

@dp.callback_query_handler(text='finca_rub')
async def finca_rub(call: CallbackQuery):
    await call.message.answer('Курс RUB \n Покупка {} \n Продажа {}'.format(text[103], text[104]))

@dp.callback_query_handler(text='kkb_rub')
async def kkb_rub(call: CallbackQuery):
    await call.message.answer('Курс RUB \n Покупка {} \n Продажа {}'.format(text[106], text[107]))

@dp.callback_query_handler(text='kicb_rub')
async def kicb_rub(call: CallbackQuery):
    await call.message.answer('Курс RUB \n Покупка {} \n Продажа {}'.format(text[88], text[89]))

@dp.callback_query_handler(text='mossovet_rub')
async def mossovet_rub(call: CallbackQuery):
    await call.message.answer('Курс RUB \n Покупка {} \n Продажа {}'.format(text[85], text[86]))

@dp.callback_query_handler(text='optima_rub')
async def optima_rub(call: CallbackQuery):
    await call.message.answer('Курс RUB \n Покупка {} \n Продажа {}'.format(text[76], text[77]))

@dp.callback_query_handler(text='asia_rub')
async def asia_rub(call: CallbackQuery):
    await call.message.answer('Курс RUB \n Покупка {} \n Продажа {}'.format(text[91], text[92]))

@dp.callback_query_handler(text='kg_rub')
async def kg_rub(call: CallbackQuery):
    await call.message.answer('Курс RUB \n Покупка {} \n Продажа {}'.format(text[82], text[83]))

@dp.callback_query_handler(text='demir_rub')
async def demir_rub(call: CallbackQuery):
    await call.message.answer('Курс RUB \n Покупка {} \n Продажа {}'.format(text[94], text[95]))

@dp.callback_query_handler(text='bai_rub')
async def bai_rub(call: CallbackQuery):
    await call.message.answer('Курс RUB \n Покупка {} \n Продажа {}'.format(text[97], text[98]))

@dp.callback_query_handler(text='keremet_rub')
async def keremet_rub(call: CallbackQuery):
    await call.message.answer('Курс RUB \n Покупка {} \n Продажа {}'.format(text[100], text[101]))

# 
#  KZT
# 

@dp.callback_query_handler(text='rsk_kzt')
async def rsk_kzt(call: CallbackQuery):
    await call.message.answer('Курс KZT \n Покупка {} \n Продажа {}'.format(text[64], text[65]))

@dp.callback_query_handler(text='finca_kzt')
async def finca_kzt(call: CallbackQuery):
    await call.message.answer('Курс KZT \n Покупка {} \n Продажа {}'.format(text[64], text[65]))

@dp.callback_query_handler(text='kkb_kzt')
async def kkb_kzt(call: CallbackQuery):
    await call.message.answer('Курс KZT \n Покупка {} \n Продажа {}'.format(text[64], text[65]))

@dp.callback_query_handler(text='kicb_kzt')
async def kicb_kzt(call: CallbackQuery):
    await call.message.answer('Курс KZT \n Покупка {} \n Продажа {}'.format(text[64], text[65]))

@dp.callback_query_handler(text='mossovet_kzt')
async def mossovet_kzt(call: CallbackQuery):
    await call.message.answer('Курс KZT \n Покупка {} \n Продажа {}'.format(text[64], text[65]))

@dp.callback_query_handler(text='optima_kzt')
async def optima_kzt(call: CallbackQuery):
    await call.message.answer('Курс KZT \n Покупка {} \n Продажа {}'.format(text[64], text[65]))

@dp.callback_query_handler(text='asia_kzt')
async def asia_kzt(call: CallbackQuery):
    await call.message.answer('Курс KZT \n Покупка {} \n Продажа {}'.format(text[64], text[65]))

@dp.callback_query_handler(text='kg_kzt')
async def kg_kzt(call: CallbackQuery):
    await call.message.answer('Курс KZT \n Покупка {} \n Продажа {}'.format(text[64], text[65]))

@dp.callback_query_handler(text='demir_kzt')
async def demir_kzt(call: CallbackQuery):
    await call.message.answer('Курс KZT \n Покупка {} \n Продажа {}'.format(text[64], text[65]))

@dp.callback_query_handler(text='bai_kzt')
async def bai_kzt(call: CallbackQuery):
    await call.message.answer('Курс KZT \n Покупка {} \n Продажа {}'.format(text[64], text[65]))

@dp.callback_query_handler(text='keremet_kzt')
async def keremet_kzt(call: CallbackQuery):
    await call.message.answer('Курс KZT \n Покупка {} \n Продажа {}'.format(text[64], text[65]))

@dp.message_handler(text='/photo')
async def photo(message: types.Message):
    index = random.randint(1, 10)
    photo_path = InputFile(
        path_or_bytesio='photos/image' + str(index) + '.jpg')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_path, caption='Vot te photo')

executor.start_polling(dp)