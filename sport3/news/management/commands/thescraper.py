from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup as bs
import requests
from news.models import MyNewsFb

links = []


class Command(BaseCommand):
    help = 'collect football news'

    def jalali_to_gregorian(self, jy, jm, jd):
        jy += 1595
        days = -355668 + (365 * jy) + ((jy // 33) * 8) + (((jy % 33) + 3) // 4) + jd
        if (jm < 7):
            days += (jm - 1) * 31
        else:
            days += ((jm - 7) * 30) + 186
        gy = 400 * (days // 146097)
        days %= 146097
        if (days > 36524):
            days -= 1
            gy += 100 * (days // 36524)
            days %= 36524
            if (days >= 365):
                days += 1
        gy += 4 * (days // 1461)
        days %= 1461
        if (days > 365):
            gy += ((days - 1) // 365)
            days = (days - 1) % 365
        gd = days + 1
        if ((gy % 4 == 0 and gy % 100 != 0) or (gy % 400 == 0)):
            kab = 29
        else:
            kab = 28
        sal_a = [0, 31, kab, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        gm = 0
        while (gm < 13 and gd > sal_a[gm]):
            gd -= sal_a[gm]
            gm += 1
        return [gy, gm, gd]

    def time_maker(self, datee):
        mylist = (datee.split('/'))

        for item in mylist:
            if '0' in item:
                new = item.replace('0', '')
                mylist[mylist.index(item)] = new
        num_list = []
        for num in mylist:
            num_list.append(int(num))
        return num_list
    
    def time_format(self, engdate):
        temp = ''
        for myitem in engdate:
            temp = temp + str(myitem) + '-'
        return(temp[:-1])

    def date_format_created(self, endatelist, atime):
        timelist = atime.split(':')
        return [endatelist[0],endatelist[1], endatelist[2], timelist[0], timelist[1],]

    

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
            for link in mylinks:
                try:
                    page1 = s.get(link)
                    soup1 = bs(page1.content, 'html.parser')
                    date = soup1.select_one('.numeric-value:nth-child(3)').text
                    time = soup1.select_one('.numeric-value:nth-child(2)').text
                    news_lead = soup1.select('.news-page--news-lead')
                    news_title = soup1.select('.news-page--news-title')
                    news_text = soup1.select('.news-page--news-text')
                    print(date)
                except:
                    continue
                try:
                    mydate = self.time_maker(date)
                except:
                    print(link)

                myengdate = self.jalali_to_gregorian(mydate[0], mydate[1], mydate[2])

                thetime = self.time_format(myengdate)

                mytime = self.date_format_created(myengdate, time)

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
                            mydate=thetime,
                            mytime=time,
                        )
                        print('%s added' % (title,))
                    except:
                        print('%s already exists' % (title,))
        self.stdout.write( 'football news completed' )