import asyncio
import aiohttp
import json
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv
import os

load_dotenv()

API_TOKEN = "8461170461:AAHkHDiK8x7FKtPnbyyycN2ZqYfu9UowGZg" # 🔑 положи токен в .env
API_URL = "http://127.0.0.1:8000/chat"  # адрес FastAPI сервера

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот 🤖 Пиши что-нибудь, и я задам это GigaChat 🚀")


@dp.message()
async def handle_message(message: types.Message):
    user_id = str(message.from_user.id)
    user_msg = message.text
    chat_id = message.chat.id

    await bot.send_chat_action(chat_id, "typing")

    async with aiohttp.ClientSession() as session:
        payload = {"user_id": user_id, "message": user_msg}
        print(f"[BOT] Отправляю запрос на: {API_URL} с сообщением: {user_msg}")

        async with session.post(API_URL, json=payload) as resp:
            print(f"[BOT] Получен статус: {resp.status}")
            if resp.status != 200:
                await message.answer(f"⚠️ Ошибка: {resp.status}")
                return

            answer = ""
            sent_message = None
            last_edit_time = asyncio.get_event_loop().time()

            try:
                async for line_bytes in resp.content:
                    line = line_bytes.decode("utf-8").strip()
                    if not line:
                        continue

                    if not line.startswith("data:"):
                        continue

                    data = line[len("data:"):].strip()
                    if data == "[DONE]":
                        break

                    try:
                        delta_json = json.loads(data)
                        delta = delta_json.get("delta", "")
                    except Exception:
                        delta = data

                    if not delta:
                        continue

                    answer += delta

                    # Первое сообщение — отправляем
                    if sent_message is None:
                        sent_message = await message.answer(answer)
                    else:
                        now = asyncio.get_event_loop().time()
                        if now - last_edit_time > 0.5:  # обновление каждые 0.5 сек
                            try:
                                await bot.edit_message_text(
                                    chat_id=chat_id,
                                    message_id=sent_message.message_id,
                                    text=answer,
                                )
                                last_edit_time = now
                            except Exception:
                                pass

                # После окончания стрима обновляем финальный текст
                if sent_message:
                    try:
                        await bot.edit_message_text(
                            chat_id=chat_id,
                            message_id=sent_message.message_id,
                            text=answer,
                        )
                    except Exception:
                        pass
                else:
                    await message.answer(answer or "⚠️ Пустой ответ")

            except Exception as e:
                print(f"Ошибка при чтении потока: {e}")
                await message.answer("⚠️ Ошибка при получении ответа")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
