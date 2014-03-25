import os
from pyquery import PyQuery as pq
import re
import json

f = open('../blob.json','r')
shows = json.load(f)

o = open('./transcript.txt','r+')

for show in shows:
	url = "http://thekojonnamdishow.org" + show["url"] + "/transcript"
	s = pq(url)
	event = s('div').filter('.trans-event')
	for e in event:
		o.write(pq(e).text().encode('utf8'))

o.close()