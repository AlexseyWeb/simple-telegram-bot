from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Каталог")],
    [KeyboardButton(text="Погода")],
    [KeyboardButton(text="фирма")],
    [KeyboardButton(text="Контакты"),
    KeyboardButton(text="Купить бот"),]],resize_keyboard=True, input_field_placeholder="Выберите пункт меню...")

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Книги", callback_data="t_books")],
    [InlineKeyboardButton(text="Курсы", callback_data="t-courses")],
    [InlineKeyboardButton(text="Техническое собеседование", callback_data="t-profile")]], )

send_phone = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Отправить номер", request_contact=True)]], resize_keyboard=True)