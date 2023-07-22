## 非同步
```python
>>> import asyncio
>>> async def wicked():
...     print("Surrender,")
...     await asyncio.sleep(2)
...     print("Dorothy!")
... 
>>> asyncio.run(wicked())
Surrender,
Dorothy!
>>> from timeit import timeit
>>> timeit("asyncio.run(wicked())", globals=globals(), number=1)
Surrender,
Dorothy!
2.004628206000234
>>>
```

- await類似yield，但不是回傳值，而是標記一個位置讓事件迴圈可以在必要時暫停
- https://github.com/timofurrer/awesome-asyncio/
- https://aosabook.org/en/500L/a-web-crawler-with-asyncio-coroutines.html

### 其他類似套件
- curio
- trio & ask
- https://anyio.readthedocs.io/en/latest/

### ASGI web伺服器
- hypercorn
- sanic
- uvicorn

### 非同步web框架
- aiohttp
- api_hour
- asks
- blacksheep
- bocadillo
- channels
- fastapi
- muffin
- quart
- responder
- sanic
- starlette
- tornado
- vibora

### 非同步資料庫介面
- aiomysql
- aioredis
- asyncpg
