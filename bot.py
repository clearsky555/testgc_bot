from aiogram import executor

from router import dp


if __name__ == '__main__':
    print('бот запустился')
    executor.start_polling(dp, skip_updates=False)