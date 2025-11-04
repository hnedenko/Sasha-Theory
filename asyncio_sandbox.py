import time
import asyncio

async def f():
    print("Функция f начала выполняться")
    await asyncio.sleep(5)
    print("Функция f закончила выполняться")

async def g():
    print("Функция g выполнилась")

async def main():
    main_loop.create_task(f())
    main_loop.create_task(g())


if __name__ == '__main__':
    main_loop = asyncio.get_event_loop()

    main_loop.run_until_complete(main())

    main_loop.run_forever()
