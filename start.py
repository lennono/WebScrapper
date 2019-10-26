import bs4
import asyncio
from time import time
from aiohttp import ClientSession


async def fetch_html(url: str, session: ClientSession, **kwargs) -> str:
    """GET request wrapper to fetch page HTML.

    kwargs are passed to `session.request()`.
    """
    print(url)
    resp = await session.request(method="GET", url=url, **kwargs)
    resp.raise_for_status()
    html = await resp.text()
    head = await parse(html)
    return head


async def parse(body):
    page = bs4.BeautifulSoup(body, 'html.parser')
    for link in page.find_all('a'):
        if 'href' in link.attrs:
            print(link.attrs['href']) #


async def main(rate):
    async with ClientSession() as session:
        top = await asyncio.gather(fetch_html(rate, session))
        return top

if __name__ == "__main__":
    start = time()
    loop = asyncio.get_event_loop()
    Page = loop.run_until_complete(main('https://jigglypuffsdiary.com/'))
    print(f'What up. Exec time: {time() - start}')
