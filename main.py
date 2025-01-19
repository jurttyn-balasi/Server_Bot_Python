from aiogram import Dispatcher,Bot,executor,types
from btn import main_menu
api='8137152663:AAG6SMemEAzEQMsvXRFl4S1cYChRya21u9Y'
PROXY_URL = "http://proxy.server:3128/"

bot=Bot(api,proxy=PROXY_URL)
dp=Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_hi(sms:types.Message):
    await sms.answer(text=f'Assalawma aleykum {sms.from_user.username}',
                     reply_markup=main_menu)

@dp.message_handler(commands=['photo'])
async def foto(sms:types.Message):
    image=open(file='pyt.png',mode='rb')
    await sms.answer_photo(photo=image,
                           caption='Python Logo!')
    
if __name__=='__main__':
    executor.start_polling(skip_updates=True,dispatcher=dp)


    
