import aiohttp
async def channel_add(telegram_id,username,title):
    async with aiohttp.ClientSession() as sesion:
        async with sesion.get(f'http://127.0.0.1:8000/api/channel_add/{telegram_id}/{username}/{title}') as res:
            return await res.text()

async def channel_edit(telegram_id1):
    async with aiohttp.ClientSession() as sesion:
        async with sesion.get(f'http://127.0.0.1:8000/api/channel_edit/{telegram_id1}/') as res:
            return await res.text()

async def give_add(give,channel_ids,admin):
    async with aiohttp.ClientSession() as sesion:
        async with sesion.get(f'http://127.0.0.1:8000/api/give_add/{give}/{channel_ids}/{admin}/') as res:
            return await res.text()

async def give_time(give,time,admin):
    async with aiohttp.ClientSession() as sesion:
        async with sesion.get(f'http://127.0.0.1:8000/api/give_time/{give}/{time}/{admin}/') as res:
            return await res.text()

async def give_get():
    async with aiohttp.ClientSession() as sesion:
        async with sesion.get(f'http://127.0.0.1:8000/api/give/') as res:
            return await res.json()

async def assosiy():
    async with aiohttp.ClientSession() as sesion:
        async with sesion.get(f'http://127.0.0.1:8000/api/asosiy/') as res:
            return await res.json()


async def users_get():
    async with aiohttp.ClientSession() as sesion:
        async with sesion.get(f'http://127.0.0.1:8000/api/users/') as res:
            return await res.json()

async def admins_get():
    async with aiohttp.ClientSession() as sesion:
        async with sesion.get(f'http://127.0.0.1:8000/api/admins/') as res:
            return await res.json()

async def channel_get(id):
    async with aiohttp.ClientSession() as sesion:
        async with sesion.get(f'http://127.0.0.1:8000/api/channel/{id}/') as res:
            return await res.json()

async def give_user(telegram_id,username,name,give):
    async with aiohttp.ClientSession() as sesion:
        async with sesion.get(f'http://127.0.0.1:8000/api/user_give/{telegram_id}/{username}/{name}/{give}/') as res:
            return await res.text()