#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: David Pay
#date: 06-21-2018

import asyncio
from aiomysql import create_pool

loop = asyncio.get_event_loop()

async def go():
    async with create_pool(host="localhost",
    port=3306,
    user='localuser',
    password='local',
    db='awesome',
    loop=loop) as pool:

        async with pool.get() as conn:
            async with conn.cursor() as cur:
                await cur.execute("select 42;")
                value = await cur.fetchone()
                print(value)

loop.run_until_complete(go())