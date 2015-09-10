#!/usr/bin/python
#-*- coding:utf-8 -*-

import json
import urllib
import time
import random

def showsome(searchfor):
	check_result = True
	while check_result:
  		query = urllib.urlencode({'q': searchfor})
  		url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
	 	search_response = urllib.urlopen(url)
		# while (check_result == True):
		search_results = search_response.read()
		results = json.loads(search_results)
	  	data = results['responseData']
		if not data: 
			print 'something else wait a time'
			time.sleep(random.randrange(3, 8))
			check_result = True
			continue
  		print 'Total results: %s' % data['cursor']['estimatedResultCount']
  		hits = data['results']
  		print 'Top %d hits:' % len(hits)
	  	for h in hits: print ' ', h['url']
  		print 'For more results, see %s' % data['cursor']['moreResultsUrl']
  		check_result = False

##以唯讀方式讀取
File_csv = open('TwEduUniversityList.csv','r')
while 1:
	Rows = File_csv.readline()
	if not Rows: break
	Name_Host = Rows.split(',')
	Name = Name_Host[0]
	Host = Name_Host[1]
	print '學校名稱:\t%s' % Name
	print '----------------------------------'
	time.sleep(random.randrange(0, 3, 2))
	showsome(Host)
