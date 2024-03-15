from aiogram import executor,Bot,types,Dispatcher
from req import response

token = '6315632036:AAEZOxbUN5lPVP_rVGYGA3IfUq0OQ6nwRSo'
bot =  Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_hi(message:types.Message):
    await message.answer(text=f'''Salem {message.from_user.first_name}.
ChatGPT botimizga xosh keldiniz.
Ozinizge kerekli sorawlardi jollan''')

@dp.message_handler()
async def send_responce(message:types.Message):
    res = await response(message.text)
    await message.answer(text=res)




if __name__=="__main__":
    executor.start_polling(dispatcher=dp,skip_updates=True)