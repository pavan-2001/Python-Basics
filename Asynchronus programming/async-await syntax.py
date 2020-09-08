import time
def count():
    print('one')
    time.sleep(1)
    print('two')
def main():
    for i in range(0,3):
        count()
s=time.perf_counter()
main()
elapsed=time.perf_counter()-s
print(f"{__file__} executed in {elapsed:0.2f} seconds")

import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())


s = time.perf_counter()
asyncio.run(main())
elapsed = time.perf_counter() - s
print(f"using asyncio {__file__} executed in {elapsed:0.2f} seconds.")

"""
one
two
one
two
one
two
test.py executed in 3.01 seconds
One
One
One
Two
Two
Two
using asyncio test.py executed in 1.01 seconds.
"""
