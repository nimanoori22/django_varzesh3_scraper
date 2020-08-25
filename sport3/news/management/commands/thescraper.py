from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup as bs
import requests
from news.models import MyNewsFb

class Command(BaseCommand):
    help = 'collect football news'

    def handle(self, *args, **kwargs):
        with requests.session() as s:
            page = s.get('https://www.varzesh3.com/')
            soup = bs(page.content, 'html.parser')
            soup.find('ul', class_="news-list--listed-news").decompose()
            for ultag in soup.find_all('ul', {'class': 'news-list--listed-news'}):
                for litag in ultag.find_all('li'):
                    for a in litag.find_all('a'):
                        url = 'https://www.varzesh3.com/' + str(a['href'])
                        title = a.text

                    try:
                        MyNewsFb.objects.create(
                            url=url,
                            title=title,
                        )
                        print('%s added' % (title,))
                    except:
                        print('%s already exists' % (title,))
        self.stdout.write( 'football news completed' )