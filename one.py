# Python code to learn and build simple asyncio functions

import asyncio

async def func() :
    print('Inside an async function.')

    print('Before calling awaitable.....')
    
    await asyncio.sleep(3) # This line pauses the execution flow for the amount of seconds given as argument to the sleep() function.
    
    print('After calling awaitable.....')

asyncio.run(func()) # all async functions are called by passing them as arguments inside the asyncio.run() function.


""" 
func()

--> If we directly call func(), we will get 'RuntimeWarning: coroutine 'func' was never awaited'.
This is because the async functions are needed to be handled differently.
"""
