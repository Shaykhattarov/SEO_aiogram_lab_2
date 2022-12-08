import keyboards as kb

from config import token
from tests import read_file
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    global question_amount
    await message.answer(text='Привет!', reply_markup=kb.inline_start_kb)
    if question_amount == 0:
        await message.answer(text='У нас пока нет тестов для тебя :(')


@dp.callback_query_handler(lambda c: c.data == "start_button" or c.data == "next_question")
async def send_question(call: types.CallbackQuery):
    global question_counter
    await bot.answer_callback_query(call.id)
    if question_counter <= len(data):
        question = f"Вопрос №{question_counter + 1}: \n{data[question_counter]['question']}"
        await bot.send_message(call.from_user.id, text=question)
        question_counter += 1
    return


@dp.message_handler()
async def get_answer_from_user(message: types.Message):
    global user_answers
    global question_counter, question_amount
    user_answers.append(message.text)
    answer = f"Ваш ответ: \n{message.text}"
    if question_counter != question_amount:
        await message.answer(text=answer, reply_markup=kb.inline_next_question_kb)
    else:
        await message.answer(text=answer, reply_markup=kb.inline_check_answers_kb)


@dp.callback_query_handler(lambda c: c.data == 'check_answers')
async def check_answers(call: types.CallbackQuery):
    global question_amount, user_answers
    await bot.answer_callback_query(call.id)
    true_answers = 0
    results = "Вот твои ответы: \n"
    for num, answer in enumerate(user_answers):
        if answer == data[num]['answer']:
            results += f"  {num + 1}: {answer} ✅ \n"
            true_answers += 1
        else:
            results += f"  {num + 1}: {answer} ❌ \n"
    hundred_scale = int((true_answers / question_amount) * 100)
    if hundred_scale <= 40:
        complement = 'Ты большой молодец! Но попробуй еще раз :)'
    elif hundred_scale <= 70:
        complement = "Ты добился хорошего результата. Так держать!"
    else:
        complement = "Ты уминчка! Продолжай в том же духе😉"
    results += f"Общий результат: {hundred_scale} из 100.\n{complement}"
    await bot.send_message(call.from_user.id, text=results)


if __name__ == "__main__":
    print("[INFO] Старт")
    data = read_file()  # список вопросов и ответов
    question_amount = len(data)
    question_counter = 0  # счетчик вопросов
    user_answers = []
    print("[INFO] Начало работы executor")
    executor.start_polling(dp, skip_updates=True)
