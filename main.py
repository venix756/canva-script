import asyncio
import re
from os import name
from curl_cffi.requests import AsyncSession

# Set event loop policy for Windows
if name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

print("""
___.                                                     
\_ |__ ___.__. ____     ____ _____    _______  _______   
 | __ <   |  |/ __ \  _/ ___\\__  \  /    \  \/ /\__  \  
 | \_\ \___  \  ___/  \  \___ / __ \|   |  \   /  / __ \_
 |___  / ____|\___  >  \___  >____  /___|  /\_/  (____  /
     \/\/         \/       \/     \/     \/           \/ 
                                                    v 0.0.1
""")

# Headers
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

# Regex patterns
url_pattern = r'^https://www\.canva\.com/design/[^/]+/[^/]+/edit.*$'
int_pattern = r'^\d+$'

url = input('Paste URL: ')

# Validate the URL using regex
if not re.match(url_pattern, url):
    print("Invalid URL. Please provide a valid Canva design URL.")
    exit()

count = input('Type number of requests: ')

# Validate the count using regex
if not re.match(int_pattern, count):
    print("Invalid count. Please provide a valid integer value.")
    exit()

async def main():
    async with AsyncSession() as s:
        print('Processing...')
        tasks = [s.get(url, headers=headers) for _ in range(int(count))]
        await asyncio.gather(*tasks)
        print('Success')

asyncio.run(main())
