from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Кнопка приветствия
inline_start_button = InlineKeyboardButton("Начнём!", callback_data='start_button')
inline_start_kb = InlineKeyboardMarkup().add(inline_start_button)

# Кнопка ответа
inline_answer_button = InlineKeyboardButton("Ответить", callback_data='answer_button')
inline_answer_kb = InlineKeyboardMarkup().add(*[inline_answer_button])

# Кнопка следющего вопроса
inline_next_question_button = InlineKeyboardButton("Следующий вопрос", callback_data='next_question')
inline_next_question_kb = InlineKeyboardMarkup().add(inline_next_question_button)

# Кнопка просмотра результатов теста
inline_check_answers_button = InlineKeyboardButton("Посмотреть результаты", callback_data='check_answers')
inline_check_answers_kb = InlineKeyboardMarkup().add(inline_check_answers_button)
