from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
import app.keyboards as skb
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

COMMAND_BOT_TELEGRAM = "\n/start - Для начала работы с ботом \n/register - Для регистрации"

router = Router()

class Register(StatesGroup):
    name = State()
    age = State()
    phone = State()

@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer(f"Привет!\n {COMMAND_BOT_TELEGRAM}")
    await message.reply("Выберите что вас интересует:\n", reply_markup=skb.main)


@router.message(Command("help"))
async def get_help(message:Message):
    await message.answer("Вы нажали на кнопку помощи!")

@router.message(F.text == "Супер")
async def nice(message:Message):
    await message.answer("Я очень рад!")

@router.message(F.text == "Каталог")
async def get_catalog(message:Message):
    await message.answer("Выберите вашу услугу...", reply_markup=skb.catalog)

@router.callback_query(F.data == "t_books")
async def get_books(callback:CallbackQuery):
    await callback.answer("Вы выбрали категорию книги!")
    await callback.message.answer("Вы выбрали книги!")

@router.message(Command('register'))
async def registration(message:Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer("Введите ваше имя: ")

@router.message(Register.name)
async def catch_name(message:Message, state:FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer("Введите ваш возраст: ")

@router.message(Register.age)
async def catch_age(message:Message, state:FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.phone)
    await message.answer("Введите ваш телефон: ", reply_markup=skb.send_phone)


@router.message(Register.phone, F.contact)   
async def catch_phone(message:Message, state:FSMContext):
    await state.update_data(phone=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f"Ваше имя: {data["name"]}\n Ваш возраст: {data["age"]}\n Ваш телефон:+{data["phone"]}")
    await state.clear()

