import urllib
import urllib.request
from urllib.error import HTTPError

from bs4 import BeautifulSoup

class Investing():
	def __init__(self, uri='http://ru.investing.com/economic-calendar/'):
		self.uri = uri
		self.req = urllib.request.Request(uri)
		self.req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')
		self.list_news = []
		self.l_new = ["Non Form", "CPI", "GDP", "JOLTS", "RETAIL SALES", "HOUSING SALES", "DURABLE GOODS", "JOBLESS", "FOMC"]

	def news(self):
		try:
			response = urllib.request.urlopen(self.req)
			html = response.read()
			soup = BeautifulSoup(html, "html.parser")
			table = soup.find('table', {"id": "economicCalendarData"})
			tbody = table.find('tbody')
			rows = tbody.findAll('tr', {"class": "js-event-item"})

			for tr in rows:
				news = {
					'country': None,
					'impact': None,
					'name': None
					}
				cols = tr.find('td', {"class": "flagCur"})
				currency = [td.get_text(strip=True) for td in cols]
				
				if currency[-1] == "USD":
					news['country'] = currency[-1]

					impact = tr.find('td', {"class": "sentiment"})
					bull = impact.findAll('i', {"class": "grayFullBullishIcon"})
					news['impact'] = len(bull)
					event = tr.find('td', {"class": "event"})
					a = event.find('a')
					for l_n in self.l_new:
						if l_n in a.text.strip().upper():
							news['name'] = a.text.strip()
							return True
			
			return False
		except HTTPError as error:
			print("Oops... Get error HTTP {}".format(error.code))

		return 


