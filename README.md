# Abdullin-Sabir-ChatBot-FastAPI
Этот проект представляет собой Telegram-бот, который взаимодействует с сервером FastAPI.  

Описание:
Бот позволяет пользователям отправлять запросы и получать ответы, взаимодействуя с API, реализованным на базе FastAPI.  


Особенности:
Обработка команд и сообщений пользователя
Взаимодействие с сервером FastAPI
Логирование запросов и ошибок


Внимание!!!
При вводе запросов у пользователя возникает ошибка. Точная причина не установлена.


!!Установка и запуск!!

Требования
1)Python
2)Установленные библиотеки: aiogram, fastapi, uvicorn, aiohttp, python-dotenv, openai

 Укажите ваши ключи внутри обоих кодов:

API_TOKEN = 'ваш_токен_телеграм'
API_URL = 'http://127.0.0.1:8000"

Запуск сервера FastAPI:
uvicorn main:app --reload

Запуск бота
python bot.py


Ошибка возникающая при запросе:
ERROR:    Exception in ASGI application
  + Exception Group Traceback (most recent call last):
  |   File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\_utils.py", line 79, in collapse_excgroups
  |     yield
  |   File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\responses.py", line 271, in __call__
  |     async with anyio.create_task_group() as task_group:
  |                ~~~~~~~~~~~~~~~~~~~~~~~^^
  |   File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\anyio\_backends\_asyncio.py", line 772, in __aexit__
  |     raise BaseExceptionGroup(
  |         "unhandled errors in a TaskGroup", self._exceptions
  |     ) from None
  | ExceptionGroup: unhandled errors in a TaskGroup (1 sub-exception)
  +-+---------------- 1 ----------------
    | Traceback (most recent call last):
    |   File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\uvicorn\protocols\http\h11_impl.py", line 403, in run_asgi
    |     result = await app(  # type: ignore[func-returns-value]
    |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    |         self.scope, self.receive, self.send
    |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    |     )
    |     ^
    |   File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\uvicorn\middleware\proxy_headers.py", line 60, in __call__
    |     return await self.app(scope, receive, send)
    |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    |   File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\fastapi\applications.py", line 1054, in __call__
    |     await super().__call__(scope, receive, send)
    |   File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\applications.py", line 113, in __call__
    |     await self.middleware_stack(scope, receive, send)
    |   File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\middleware\errors.py", line 186, in __call__
    |     raise exc
    |   File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\middleware\errors.py", line 164, in __call__
    |     await self.app(scope, receive, _send)
    |   File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\middleware\exceptions.py", line 63, in __call__
    |     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
    |   File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\_exception_handler.py", line 53, in wrapped_app
    |     raise exc
    |   File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\_exception_handler.py", line 42, in wrapped_app
    |     await app(scope, receive, sender)
    |   File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\routing.py", line 716, in __call__
    |     await self.middleware_stack(scope, receive, send)
    |   File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\routing.py", line 736, in app
    |     await route.handle(scope, receive, send)
    |   File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\routing.py", line 290, in handle
    |     await self.app(scope, receive, send)
    |   File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\routing.py", line 78, in app
    |     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
    |   File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\_exception_handler.py", line 53, in wrapped_app
    |     raise exc
    |   File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\_exception_handler.py", line 42, in wrapped_app
    |     await app(scope, receive, sender)
    |   File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\routing.py", line 76, in app
    |     await response(scope, receive, send)
    |   File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\responses.py", line 270, in __call__
    |     with collapse_excgroups():
    |          ~~~~~~~~~~~~~~~~~~^^
    |   File "C:\Users\rusha\AppData\Local\Programs\Python\Python313\Lib\contextlib.py", line 162, in __exit__
    |     self.gen.throw(value)
    |     ~~~~~~~~~~~~~~^^^^^^^
    |   File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\_utils.py", line 85, in collapse_excgroups
    |     raise exc
    |   File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\responses.py", line 274, in wrap
    |     await func()
    |   File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\responses.py", line 254, in stream_response
    |     async for chunk in self.body_iterator:
    |     ...<2 lines>...
    |         await send({"type": "http.response.body", "body": chunk, "more_body": True})
    |   File "C:\Users\rusha\PyCharmMiscProject\.venv\fasap.py", line 39, in generate
    |     response = await client.chat.completions.create(
    |                      ^^^^^^^^^^^
    | AttributeError: 'str' object has no attribute 'chat'
    +------------------------------------

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\uvicorn\protocols\http\h11_impl.py", line 403, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        self.scope, self.receive, self.send
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\uvicorn\middleware\proxy_headers.py", line 60, in __call__
    return await self.app(scope, receive, send)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\fastapi\applications.py", line 1054, in __call__
    await super().__call__(scope, receive, send)
  File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\applications.py", line 113, in __call__
    await self.middleware_stack(scope, receive, send)
  File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\middleware\errors.py", line 186, in __call__
    raise exc
  File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\middleware\errors.py", line 164, in __call__
    await self.app(scope, receive, _send)
  File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\middleware\exceptions.py", line 63, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
  File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\routing.py", line 716, in __call__
    await self.middleware_stack(scope, receive, send)
  File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\routing.py", line 736, in app
    await route.handle(scope, receive, send)
  File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\routing.py", line 290, in handle
    await self.app(scope, receive, send)
  File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\routing.py", line 78, in app
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
  File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\routing.py", line 76, in app
    await response(scope, receive, send)
  File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\responses.py", line 270, in __call__
    with collapse_excgroups():
         ~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\rusha\AppData\Local\Programs\Python\Python313\Lib\contextlib.py", line 162, in __exit__
    self.gen.throw(value)
    ~~~~~~~~~~~~~~^^^^^^^
  File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\_utils.py", line 85, in collapse_excgroups
    raise exc
  File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\responses.py", line 274, in wrap
    await func()
  File "C:\Users\rusha\PyCharmMiscProject\.venv\Lib\site-packages\starlette\responses.py", line 254, in stream_response
    async for chunk in self.body_iterator:
    ...<2 lines>...
        await send({"type": "http.response.body", "body": chunk, "more_body": True})
  File "C:\Users\rusha\PyCharmMiscProject\.venv\fasap.py", line 39, in generate
    response = await client.chat.completions.create(
                     ^^^^^^^^^^^
AttributeError: 'str' object has no attribute 'chat'

