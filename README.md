# sentimentANALYSIS_twitter
sentiment analysis on twitter dataset
Here is the list which the extraction code needs to implement: according to JIRA user stories.
It is still not decided whether JAVA or Python will be used for this.

If anyone has any logic of extracting any of this in a structured manner, please reply to this email, so that the logic is documented.

Single Cheque/ Multiple Cheques
•	Mentioned in range Eg: please stop cheques between 001 to 0934 or listing multiple cheques listed vertically, horizontally, with commas, with hyphen, with spaces, any different way
•	In attachments,  .CSV, Excel format (xls, xlsx, xlsm, 2007 xls etc), .DAT, .txt

1.	Account number – with modulus11 check and can have only 8 digits Eg: 12345678
2.	Sort code – with validation of range Natwest Brand and RBS Brand range has combinations such as 12-34-56 OR 2-34-56 OR 12-4-56 OR 12-34-6 with hyphen-, spaces, without spaces
3.	Cheque number – between 1 to 6 digits with OR without leading zeros Eg: 1 OR 01 OR 001 OR 0001 OR 00001 OR 000001 OR 1 OR 12 OR 123 OR 1234 OR 1234 OR 12345 OR 123456
4.	Cheque Date/ Date of Cheque – “Any format of date which can be conceived by a human”
5.	Out of Date(OOD) - More than 6 months old – Cheque date validation
6.	Payee Name – Eg: payee name, payee , cheque issued to, cheque issued for, Please stop cheque for or any other thing
7.	Amount of cheque “Any amount mentioned anywhere with or without the tag “Amount or Amt or £” Eg: Please stop cheque for 34.09 , stop cheque for amt 34.09 stop cheque £ 34.09
8.	Alternative Charging Account : Eg: “Please stop the cheques below – do not charge account 44555555 charge on 67886666”

Using word search engine on email content:
•	Lost, Stolen, Astray, Mislaid, Stale, Fraud, Not received,  Non receipt
(If above information is not included then the stop should be considered chargeable)


# - *- coding: utf- 8 - *-

from flask import Flask
from flask import request
from flask_cors import CORS

import os
import re
app = Flask(__name__)
CORS(app)

# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("PORT", 9099))

@app.route('/')
def hello_world():
    return 'Hello World! I am PCF instance ' + str(os.getenv("CF_INSTANCE_INDEX", 0)) + ' . \nThis output is from Python code running in PCF.'

@app.route('/test',methods=['GET'])
def getTest():
    return 'This is a test'

@app.route('/test/<strInput>',methods=['GET'])
def getTestParam(strInput):
    return 'Welcome ' +strInput
	
@app.route('/topic',methods=['POST'])
def postTestParam():
	try:
		inData = request.get_json()
		#return 'Received following param in POST : ' + inData['id']
		import re
		import os
		import numpy as np
		import pandas as pd
		import sklearn
		import pickle
		import configparser
		import cx_Oracle
		import traceback
		import sys
		import logging
		
		config = configparser.ConfigParser()
		config.sections()
		config.read('config/default_config.ini')
		config.sections()

		# here we call all environment variables
		name = config['env_var']['name']
		print(name)
		print("09-11-2018 - V1.1")
		
		logging.basicConfig(filename='config/' + name + '.log',level=logging.DEBUG)
		logging.debug('Problem with Python code')
		
		logging.warning('And this, too')
		
		# here we call all database connection variables
		#password = config['database_var']['dbpassword']
		#print(password)
		

		#This is where database is connected
		print("DB CONNECTION WITH cx_0racle")
		#connection = cx_Oracle.connect('USP_REQHANDLER_OWNER/OWNER321as_$@devecpvm005143.server.rbsgrp.net:1564/DOGB0336_APP')
		connection = cx_Oracle.connect('RBS_DEVELOPER/Sc0tl4nd#!@devecpvm003497.server.rbsgrp.net:1678/DOGB0382_APP')
		cursor = connection.cursor ()
		cursor.execute ('Select COUNT(*)from CUST_SRVC_STATUS')
		count = cursor.fetchone ()[0]
		print('Count from CUST_SRVC_STATUS =')
		print(count)
		cursor.close ()
		connection.close () 
		print("DB CONNECTION WITH cx_0racle ENDED")

		#This is where the input of email goes in
		print(inData)
		print("Printed just indata")
		emailcontent = inData['id']
		print("email content assigned")
		
		emailcontent = emailcontent.encode('ascii','ignore').decode('ascii')
		print(emailcontent)
		
		out1 = emailcontent.decode('utf-8')
		out1= out1.replace(u'£',' ')
		out1 = out1.replace('\r', ' ')
		out1 = out1.replace('\n', ' ') 
		print(out1)
		#print("decodecoded string printed as out1")
		
		
		# This is where the body of email is read
		#out1 = emailcontent
		out1 = out1.lower()
		out1 = "".join(c for c in out1 if c not in ('+', '%', '!', '.', ':', '#'))
		
		# Predictive Model starts here
		emailcontent1 = [out1]
		filename = "config/finalized_model.sav"
		loaded_model = pickle.load(open(filename, 'rb'))
		count_vect = pickle.load(open("config/finalized_vector", "rb"))
		print("0.0 ARTIFICIAL INTELLIGENCE IS DETECTING THE TOPIC")
		logging.info('0.0 ARTIFICIAL INTELLIGENCE IS DETECTING THE TOPIC')
		abc = str(loaded_model.predict(count_vect.transform(emailcontent1)))
		print("0.1 ARTIFICIAL INTELLIGENCE HAS DETECTED THE TOPIC - " + abc)
		logging.info('0.1 ARTIFICIAL INTELLIGENCE HAS DETECTED THE TOPIC - ' + abc)
		
		# Predictive Model ends here
		
		#this is just dummy code
		file_object  = open("config/test.txt", "r") 
		var = file_object.read()
		print(var)
		
		# The extraction code starts here
		
		if abc == "[1]":
			
			#definition to find needle in a haystack
			def findnth(haystack, needle, n):
				parts= haystack.split(needle, n+1)
				if len(parts)<=n+1:
					return -1
				return len(haystack)-len(parts[-1])-len(needle)
			
			# Clean spaces between words
			out1 = out1.replace('account', ' acc ')
			out1 = out1.replace('acct', ' acc ')
			out1 = out1.replace('act', ' acc ')
			out1 = out1.replace('acc', ' acc ')
			out1 = out1.replace('cheques', ' cheq ')
			out1 = out1.replace('cheque', ' cheq ')
			out1 = out1.replace('cheq', ' cheq ')
			out1 = out1.replace('chq', ' cheq ')
			out1 = out1.replace('dated', ' date ')
			out1 = out1.replace('date', ' ')
			out1 = out1.replace('sort', ' sort ')
			out1 = out1.replace('code', '  ')
			out1 = out1.replace('stopped', ' stop ')
			out1 = out1.replace('stops', 'stop')
			out1 = out1.replace('numbers', ' number ')
			out1 = out1.replace('number', ' number ')
			out1 = out1.replace('no', ' number ')
			out1 = out1.replace('number', ' ')
			out1 = out1.replace('cancellation', ' cancel ')
			out1 = out1.replace('cancelled', ' cancel ')
			out1 = out1.replace('cancel', ' cheq ')
			out1 = out1.replace('amount', ' amt ')
			out1 = out1.replace('thanks', ' thanks ')
			out1 = out1.replace(',', ' ')
			out1 = out1.replace('.', ' ')
			# removing double spaces between words
			print('STEP 1.0 - REMOVED SPACES ' + out1)
			logging.info('STEP 1.0 - REMOVED SPACES ' + out1)

			# remove dates from the string
			expr = re.compile('\d{2}/\d{2}/\d{4}')
			out1 = re.sub(expr, '', out1)  # replace all dates with ''

			# remove dates from the string
			expr = re.compile('\d{2}/\d{2}')
			out1 = re.sub(expr, '', out1)  # replace all dates with ''
			
			# removing amount next to pound sign
			if "date" in out1:
				list_of_words = out1.split()
				next_word = list_of_words[list_of_words.index("c2a3") + 1]
				out1 = out1.replace(next_word, ' ')
				print('STEP 2.0 - REMOVED NUMBER NEXT TO POUND SIGN ' + out1)
			
			# removing amount next to pound sign
			if "c2a3" in out1:
				list_of_words = out1.split()
				next_word = list_of_words[list_of_words.index("date") + 1]
				out1 = out1.replace(next_word, ' ')
				print('STEP 2.1 - REMOVED NUMBER NEXT TO DATE ' + out1)

			# removing amt
			if 'amt' in out1:
				list_of_words = out1.split()
				next_word = list_of_words[list_of_words.index('amt') + 1]
				out1 = out1.replace(next_word, ' ')
				print('STEP 3.0 - REMOVED NUMBER NEXT TO AMT ' + out1)
				logging.info('STEP 3.0 - REMOVED NUMBER NEXT TO AMT ' + out1)
				
			s1 = "acc"
			USP_ACC = ""
			USP_ACC_ERROR = ""
			'''Account_number Identification'''
			if s1 in out1:
				count_of_word1 = out1.count(s1)
				c = 0
				for y in range(0, count_of_word1):
					c = findnth(out1, s1, y)
					wtf3 = out1[c:c+20]
					print(wtf3)
					if re.findall(r'(\d{8})', wtf3):
						account_number = re.findall(r'(\d{8})', wtf3)
						print(account_number)
						account_1 = ''.join(account_number)
						USP_ACC = account_number[0]
						print("STEP 4.0 - FOUND ACCOUNT NUMBER " + USP_ACC)
						logging.info("STEP 4.0 - FOUND ACCOUNT NUMBER " + USP_ACC)
						USP_ACC_ERROR = ""
						# This code removes account numbers from email
						list_of_words = out1.split()
						resultwords = [word for word in list_of_words if word not in account_number]
						out1 = ' '.join(resultwords)
						print('STEP 4.0 - REMOVAL OF ACCOUNT NUMBER ' + out1)
						logging.info('STEP 4.0 - REMOVAL OF ACCOUNT NUMBER ' + out1)
			if USP_ACC == "":
				USP_ACC = "NA"
				USP_ACC_ERROR = "ACCOUNT NUMBER NOT FOUND "
				logging.info(USP_ACC_ERROR)
				print('STEP 4.1 - ACCOUNT NUMBER NOT FOUND')
				logging.info('STEP 4.1 - ACCOUNT NUMBER NOT FOUND')
			
			s2 = "sort"
			USP_SORTCODE = ""
			USP_SORTCODE_ERROR = ""
			'''Sort Code Identification'''
			if s2 in out1:
				count_of_word2 = out1.count(s2)
				d = 0
				for z in range(0, count_of_word2):
					d = findnth(out1, s2, z)
					wtf4 = out1[d:d+20]
					print(wtf4)
					if re.findall(r'(\d{2}-\d{2}-\d{2})', wtf4):
						sort_code_hyp = re.findall(r'(\d{2}-\d{2}-\d{2})', wtf4)
						print("STEP 5.0 - FOUND SORT CODE WITH HYPHEN " + sort_code_hyp[0])
						logging.info("STEP 5.0 - FOUND SORT CODE WITH HYPHEN " + sort_code_hyp[0])
						USP_SORTCODE_ERROR = ""
						USP_SORTCODE = sort_code_hyp[0]
						# This code removes sort codes from email
						out1 = out1.replace(sort_code_hyp[0], " ")
						USP_SORTCODE = USP_SORTCODE.replace('-', '')
						print('STEP 5.0 - REMOVAL OF SORT CODE ' + out1)
						logging.info('STEP 5.0 - REMOVAL OF SORT CODE ' + out1)
					elif re.findall(r'(\d{1}-\d{2}-\d{2})', wtf4):
						sort_code_hyp = re.findall(r'(\d{1}-\d{2}-\d{2})', wtf4)
						print("STEP 5.0 - FOUND SORT CODE WITH HYPHEN " + sort_code_hyp[0])
						logging.info("STEP 5.0 - FOUND SORT CODE WITH HYPHEN " + sort_code_hyp[0])
						USP_SORTCODE_ERROR = ""
						USP_SORTCODE = sort_code_hyp[0]
						# This code removes sort codes from email
						out1 = out1.replace(sort_code_hyp[0], " ")
						USP_SORTCODE = USP_SORTCODE.replace('-', '')
						print('STEP 5.0 - REMOVAL OF SORT CODE ' + out1)
						logging.info('STEP 5.0 - REMOVAL OF SORT CODE ' + out1)
					elif re.findall(r'(\d{2}-\d{1}-\d{2})', wtf4):
						sort_code_hyp = re.findall(r'(\d{2}-\d{1}-\d{2})', wtf4)
						print("STEP 5.0 - FOUND SORT CODE WITH HYPHEN " + sort_code_hyp[0])
						logging.info("STEP 5.0 - FOUND SORT CODE WITH HYPHEN " + sort_code_hyp[0])
						USP_SORTCODE_ERROR = ""
						USP_SORTCODE = sort_code_hyp[0]
						# This code removes sort codes from email
						out1 = out1.replace(sort_code_hyp[0], " ")
						USP_SORTCODE = USP_SORTCODE.replace('-', '')
						print('STEP 5.0 - REMOVAL OF SORT CODE ' + out1)
						logging.info('STEP 5.0 - REMOVAL OF SORT CODE ' + out1)
					elif re.findall(r'(\d{2}-\d{2}-\d{1})', wtf4):
						sort_code_hyp = re.findall(r'(\d{2}-\d{2}-\d{1})', wtf4)
						print("STEP 5.0 - FOUND SORT CODE WITH HYPHEN " + sort_code_hyp[0])
						logging.info("STEP 5.0 - FOUND SORT CODE WITH HYPHEN " + sort_code_hyp[0])
						USP_SORTCODE_ERROR = ""
						USP_SORTCODE = sort_code_hyp[0]
						# This code removes sort codes from email
						out1 = out1.replace(sort_code_hyp[0], " ")
						USP_SORTCODE = USP_SORTCODE.replace('-', '')
						print('STEP 5.0 - REMOVAL OF SORT CODE ' + out1)
						logging.info('STEP 5.0 - REMOVAL OF SORT CODE ' + out1)
					elif re.findall(r'(\d{6})', wtf4):
						sort_code = re.findall(r'(\d{6})', wtf4)
						print("STEP 5.1 - FOUND SORT CODE WITHOUT HYPHEN " + sort_code[0])
						logging.info("STEP 5.1 - FOUND SORT CODE WITHOUT HYPHEN " + sort_code[0])
						USP_SORTCODE = sort_code[0]
						USP_SORTCODE_ERROR = ""
						# This code removes sort codes from email
						out1 = out1.replace(sort_code[0], " ")
						print('STEP 5.2 - REMOVAL OF SORT CODE ' + out1)
						logging.info('STEP 5.2 - REMOVAL OF SORT CODE ' + out1)
			if USP_SORTCODE == "":
				USP_SORTCODE = "NA"
				USP_SORTCODE_ERROR = "SORT CODE NOT FOUND "
				logging.info('STEP 5.3 - SORT CODE NOT FOUND ')
					
			s3 = "cheq"
			USP_CHEQUE_NUM = ""
			USP_CHEQUE_ERROR = ""
			'''Cheque_number Identification'''
			if s3 in out1:
				count_of_word = out1.count(s3)
				a = 0
				for x in range(0, count_of_word):
					a = findnth(out1, s3, x) 
					wtf2 = out1[a:a+15]
					if re.findall(r'(\d{6})', wtf2):
						cheq_number = re.findall(r'(\d{6})', wtf2)
						print(cheq_number)
						print("STEP 6.0 - FOUND 6 DIGITS CHEQUE NUMBER " + cheq_number[0])
						USP_CHEQUE_NUM = cheq_number[0]
						USP_CHEQUE_ERROR = ""
						# This code removes cheque numbers from email
						out1 = out1.replace(cheq_number[0], " ")
						print('STEP 6.1 - REMOVAL OF 6 DIGITS CHEQUE NUMBER ' + out1)
					elif re.findall(r'(\d{5})', wtf2):
						cheq_number = re.findall(r'(\d{5})', wtf2)
						USP_CHEQUE_NUM = cheq_number[0]
						USP_CHEQUE_ERROR = ""
						print(cheq_number)
						print("STEP 6.1 - FOUND 5 DIGIT CHEQUE NUMBER " + cheq_number[0])
					elif re.findall(r'(\d{4})', wtf2):
						cheq_number = re.findall(r'(\d{4})', wtf2)
						USP_CHEQUE_NUM = cheq_number[0]
						USP_CHEQUE_ERROR = ""
						print(cheq_number)
						print("STEP 6.1 - FOUND 4 DIGIT CHEQUE NUMBER " + cheq_number[0])
					elif re.findall(r'(\d{3})', wtf2):
						cheq_number = re.findall(r'(\d{3})', wtf2)
						USP_CHEQUE_NUM = cheq_number[0]
						USP_CHEQUE_ERROR = ""
						print(cheq_number)
						print("STEP 6.1 - FOUND 3 DIGIT CHEQUE NUMBER " + cheq_number[0])
					elif re.findall(r'(\d{2})', wtf2):
						cheq_number = re.findall(r'(\d{2})', wtf2)
						USP_CHEQUE_NUM = cheq_number[0]
						USP_CHEQUE_ERROR = ""
						print(cheq_number)
						print("STEP 6.1 - FOUND 2 DIGIT CHEQUE NUMBER " + cheq_number[0])
			if USP_CHEQUE_NUM == "":
				USP_CHEQUE_NUM = "NA"
				USP_CHEQUE_ERROR = "CHEQUE NUMBER NOT FOUND"
				print(USP_CHEQUE_ERROR)
	 
			if (USP_CHEQUE_NUM == "NA" or USP_ACC == "NA" or USP_SORTCODE == "NA"):  # CORRECT!
				json1 = '{"data": [{"requestTopic":"stopcheque","requestSubType":"single","payload":[{"chequeNumber":"' + USP_CHEQUE_NUM + '","accountNumber":"' + USP_ACC + '","sortCode":"' + USP_SORTCODE + '"}],"error":"720 ' + USP_CHEQUE_ERROR + USP_ACC_ERROR + USP_SORTCODE_ERROR + '"}], }'
				print(json1)
			else:
				json1 = '{"data": [{"requestTopic":"stopcheque","requestSubType":"single","payload":[{"chequeNumber":"' + USP_CHEQUE_NUM + '","accountNumber":"' + USP_ACC + '","sortCode":"' + USP_SORTCODE + '"}]}] }'
				print(json1)
		else:
			json1 = ('{"data": [{"requestTopic": "UNKNOWN"}]}')
	except Exception as error:
		json1 = ('{"error":"500 - Python failed to execute"}')
		print(error)
	return json1;
	
if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)
