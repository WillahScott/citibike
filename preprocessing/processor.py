## PROCESSING of the Citi-Bike datasets
#      April, 2016

## Usage (from preprocessing/ folder) :
# $ python -W ignore processor.py
#


import glob
import datetime
import numpy as np
import pandas as pd

DATA_PATH = '../data/'

def data_munger(df):
	''' Preprocesses dataframe, outputs processed dataframe '''
	# Initial FILTER: duration, start_time, start_location, end_location, usertype
	pre_filter = ['tripduration', 'starttime', 'usertype',
	              'start station latitude', 'start station longitude',
	              'end station latitude', 'end station longitude' ]
	predata = df[ pre_filter ]

	# Trip to minutes -> Intervals
	trip_cuts = [5,10,30,60]
	predata['duration'] = np.digitize( predata['tripduration'] / 60, trip_cuts )

	# Hour of day (floor)
	get_hour = lambda x: int( x.split()[1].split(':')[0] )
	predata['time'] = predata['starttime'].apply(get_hour)

	# Weekday
	get_weekday = lambda x: datetime.datetime(*map(int, x.split()[0].split('-'))).weekday()
	predata['weekday'] = df['starttime'].apply(get_weekday)

	# Rename columns
	renamer = {'start station latitude': 'start_lat',
	           'start station longitude': 'start_lon',
	           'end station latitude': 'end_lat',
	           'end station longitude': 'end_lon'}
	predata.rename(columns=renamer, inplace=True)

	# Final filter
	final_filter = ['weekday', 'time', 'duration', 'usertype',
	                'start_lat', 'start_lon', 'end_lat', 'end_lon']
	return predata[ final_filter ]


def process_files(in_files, out_files=None, verbose=False):
	''' Pipelines the data munging for a set of files '''

	in_out = zip(in_files, out_files if out_files is not None else in_files)

	for in_, out_ in in_out:

		if verbose:
			print('Processing {}  ...'.format(in_) )

		in_data = pd.read_csv(in_)
		out_data = data_munger(in_data)
		out_data.to_csv(out_)

		if verbose:
			print('   DONE -> {}\n'.format(out_))


# If executed all csv's on DATA_PATH/raw/ will get processed and saved into
#  DATA_PATH/processed with the same name (with whitespace stripped)

def main():
	# get list of all csv's in DATA_PATH/raw
	in_csv = glob.glob(DATA_PATH + 'raw/*.csv')
	out_csv = map( lambda x: x.replace('raw/','processed/').replace(' ',''), in_csv )

	print( '\nProcessing {} files:\n'.format(len(in_csv)) )

	process_files(in_csv, out_csv, verbose=True)


if __name__ == '__main__':
	main()
