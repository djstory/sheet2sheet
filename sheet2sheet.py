#!/usr/bin/env python

'''
    File name: sheet2sheet.py
    Author: Daniel Story
    Date created: 3/7/2019
    Date last modified: 4/2/2019
    Python Version: 2.7, 3
'''

import sys, pandas
from datetime import datetime
from dateutil.relativedelta import relativedelta

filename=str(sys.argv[1])
rows = []

def main():
	with open(filename, "r") as file:

		# read in data from CSV
		df = pandas.read_csv(filename, index_col=None, header=0, sep=",")
		
		# iterate rows and perform some computation
		for index, row in df.iterrows():
			# if row qualifies, perform computation
			if row['Duration'] > 1:
				duration = row['Duration']
				for d in range(1, int(duration)+1):
					newdict = dict()
					newdict.update(row)
					newdict['Duration'] = 1
					try:
						newdict['Gross'] = '[' + str(round(float(row['Gross'])/duration, 2)) + ']'
					except:
						print("Error")
					try:
						newdict['Co.'] = '[' + str(round(float(row['Co.'])/duration, 2)) + ']'
					except:
						print("Error")
					try:
						newdict['Exhibition Returns B'] = '[' + str(round(float(row['Exhibition Returns B'])/duration, 2)) + ']'
					except:
						print("Error")
					try:
						datetime_obj =datetime.strptime(row['Date'], "%m/%d/%Y")
						daysToAdd = d - 1
						dateNext = datetime_obj + relativedelta(days=+daysToAdd)
						dateNextSave = dateNext.strftime("%m/%d/%Y")
						newdict['Date'] = dateNextSave
						newdict['Enddate'] = dateNextSave
					except:
						print("Couldn't save date.")
					rows.append(newdict)
			# else save row as-is to new dataset
			else:
				rows.append(row)

	# save new dataset to file
	newdf = pandas.DataFrame(rows)
	with open('output.csv', 'w') as f:
		newdf.to_csv(f, index=False, mode='a', header=True, encoding='utf-8')
		print("Done.")

if __name__ == '__main__':
  main()