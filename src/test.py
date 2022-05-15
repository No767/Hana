from hana_core import getResources
import asyncio
from rich import print

mainObj = getResources()

async def main():
    print(await mainObj.get_post("udknkd"))
    
asyncio.run(main())
