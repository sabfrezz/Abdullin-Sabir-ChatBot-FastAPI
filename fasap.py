from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from openai import AsyncOpenAI
import os
import json
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Используем новый клиент
client ="e5a53e72-b609-4c71-8ce1-ba6bcaa565cb"

# Простое хранилище контекста для каждого пользователя
user_sessions = {}


def get_context(user_id: str):
    if user_id not in user_sessions:
        user_sessions[user_id] = []
    return user_sessions[user_id]


@app.post("/chat")
async def chat_endpoint(request: Request):
    data = await request.json()
    user_id = data.get("user_id")
    message = data.get("message")

    if not user_id or not message:
        return {"error": "user_id и message обязательны"}

    user_context = get_context(user_id)
    user_context.append(f"User: {message}")

    async def generate():
        # Новый вызов API
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты добрый помощник по ИТ."},
                *[
                    {
                        "role": "user" if idx % 2 == 0 else "assistant",
                        "content": msg,
                    }
                    for idx, msg in enumerate(user_context)
                ],
            ],
            stream=True,
        )

        answer = ""
        async for chunk in response:
            delta = chunk.choices[0].delta
            content = delta.get("content")
            if content:
                answer += content
                # SSE-формат: data: {json}
                yield f"data: {json.dumps({'delta': content}, ensure_ascii=False)}\n\n"

        user_context.append(f"AI: {answer}")
        yield "data: [DONE]\n\n"

    return StreamingResponse(generate(), media_type="text/event-stream")
