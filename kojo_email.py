import os
from datetime import date
from pyquery import PyQuery as pq
import json
import smtplib

todaydate = date.today().isoformat()

# Initialize the Email

fromaddr = os.environ.get('SENDTOADDR')
toaddrs  = fromaddr
msg = "Subject: Today's Kojo Show -- " + todaydate + '\n'
server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
user = os.environ.get('GMAILUSER')
pwd = os.environ.get('GMAILPWD')
server.login(user,pwd)


# Open up the existing Kojo Show details
f = open('./blob.json','r+')
ex_data = json.load(f)
f.seek(0)
data = []

# Get today's list of shows
url = "http://thekojonnamdishow.org/shows/" + todaydate
s = pq(url)

# For each day, go to each show
for e in s('div').filter('.event-permalink'):
	s_url = pq(e).text()
	d = pq(s_url)
	guests = d('div').filter(".content-multigroup-wrapper")
	gdata = []

	# Get the guest data
	for guest in guests:
		g = pq(guest)
		gdata.append({
			"guest":g('div').filter(".field-field-guest").text(),
				"credentials":g('div').filter(".field-field-guest-credentials").text()
			})

	# Append the guest data and other metadata into data object
	dataobj = {
		"date": d('span').filter(".date-display-single").text(),
		"title": d('h2').filter(".page-title").text(),
		"url":  s_url,
		"summary":d('div').filter(".segment-node-body").text(),
		"guests": gdata
		}
	data.append(dataobj);
	ex_data.append(dataobj);

# Send the email with the new data
msg = msg + json.dumps(data, indent=2)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()

# Dump the complete data set to the blob file
f.write(json.dumps(ex_data, indent=2))
f.close()