'''
File to convert addresses in dataframe to coordinates using a Geocoder, so that we do not have to make repetitive API calls.
'''

import pandas as pd
from tqdm import tqdm
from pygeocoder import Geocoder

def main():
	BATCH_SIZE = 300
	
	df = pd.read_csv('Datasets/pd_collisions_datasd_v1.csv')
	addresses_we_have = pd.read_csv('Datasets/Locations.csv').drop('Unnamed: 0', axis = 1)
	
	print(f'Current Size : {addresses_we_have.shape[0]} locations')
	
	df = df[addresses_we_have.shape[0]: min(df.shape[0], addresses_we_have.shape[0] + BATCH_SIZE)] # We only want to geocode the positions we don't have
	
	# Extracting Addresses from df
	addresses = df.apply(lambda x : ' '.join(
		str(i).strip() for i in [x.address_number_primary, x.address_pd_primary, x.address_road_primary, x.address_sfx_primary] 
	) + ', SAN DIEGO', axis = 1)
	
	# Geocoder
	MAPS_API_KEY = 'AIzaSyD4ozPjvWdpbW8K3fiabpFwRNSTjITvim8'
	coder = Geocoder(MAPS_API_KEY)
	
	tqdm.pandas() # Progress Bar
	
	# Geocoding
	addresses = addresses.to_frame().rename({0: 'Address'}, axis = 1)
	addresses['Coordinates'] = addresses['Address'].progress_apply(lambda address : coder.geocode(address).coordinates)
	
	result = pd.concat([addresses_we_have, addresses])
	
	# Saving file
	result.to_csv('Datasets/locations.csv')
	
	print(f'Completed Batch, New Size : {result.shape[0]} locations')
		
if __name__ == '__main__':
	main()