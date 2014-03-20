import os
from sys import argv
import sys
import requests
from datetime import time, date, timedelta

def command_line():
	if len(argv) == 8:
		script, username, password, vendor_id, report_type, date_type, report_subtype, report_date = argv
	
	elif len(argv) == 7:
		script, username, password, vendor_id, report_type, date_type, report_subtype = argv
		yesterday = date.today() - timedelta(days=1)
		report_date = yesterday.strftime('%Y%m%d')
	else:
		this_script =  str(os.path.basename(__file__))
		print "Usage is: %s <email> <password> <vendor ID> <Sales OR Newsstand> <Daily OR Weekly> <Summary OR Detailed OR Opt-In>" % this_script
		return

	fetch(username, password, vendor_id, report_type, date_type, report_subtype, report_date)
	

def fetch(username, password, vendor_id, report_type, date_type, report_subtype, report_date):
	params = ({
	"USERNAME" : username,
	"PASSWORD" : password,
	"VNDNUMBER" : vendor_id,
	"TYPEOFREPORT" : report_type,
	"DATETYPE" : date_type,
	"REPORTTYPE" : report_subtype,
	"REPORTDATE" : report_date
	})
	
	url_base = "https://reportingitc.apple.com/autoingestion.tft?"
	
	headers ={"Content-Type" : "application/x-www-form-urlencoded"}
	
	r = requests.post(url_base, headers = headers, params = params)
	
	if r.headers['errormsg']:
		print r.headers['errormsg']
	elif r.headers['filename']:
		fname = r.headers['filename'].split(".")[0]
		f = open(fname+".txt", 'w')
		f.write(r.content)
		f.close()
		
	else:
		print "Something unexpected happened."
		
if __name__ == '__main__':
	command_line()