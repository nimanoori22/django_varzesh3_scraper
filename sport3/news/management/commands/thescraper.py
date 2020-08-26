from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup as bs
import requests
from news.models import MyNewsFb

links = []


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
                        links.append('https://www.varzesh3.com/' + str(a['href']))

            mylinks = list(dict.fromkeys(links))
            print(mylinks)
            for link in mylinks:
                page1 = s.get(link)
                soup1 = bs(page1.content, 'html.parser')
                news_lead = soup1.select('.news-page--news-lead')
                news_title = soup1.select('.news-page--news-title')
                news_text = soup1.select('.news-page--news-text')

                for n, t, mt, in zip(news_lead, news_title, news_text):
                    lead = n.text
                    title = t.text
                    content = mt.text
                    

                    try:
                        MyNewsFb.objects.create(
                            url=link,
                            title=title,
                            lead=lead,
                            content=content,
                        )
                        print('%s added' % (title,))
                    except:
                        print('%s already exists' % (title,))
        self.stdout.write( 'football news completed' )