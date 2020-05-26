

class MySpider(Spider):
    # ...
    async def parse_with_deferred(self, response):
        additional_response = await treq.get('https://additional.url')
        additional_data = await treq.content(additional_response)
        # ... use response and additional_data to yield items and requests

    async def parse_with_asyncio(self, response):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://additional.url') as additional_response:
                additional_data = await r.text()
        # ... use response and additional_data to yield items and requests


