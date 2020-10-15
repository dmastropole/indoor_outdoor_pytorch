import os
import json
import pandas as pd

import indoor_outdoor_pytorch.data as iop_data


THIS_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(THIS_DIR, '..', 'data')


def check_cats(cat_list, df):
	df_cats = set(df['Name'].to_list())
	cat_set = set(cat_list)
	return cat_set.issubset(df_cats)

def main():

	# Create labels
	vocab = pd.read_csv(os.path.join(DATA_DIR, 'indoor_outdoor/vocabulary.csv'))

	assert check_cats(iop_data.INDOOR_CATS, vocab)
	assert check_cats(iop_data.OUTDOOR_CATS, vocab)

	with open(os.path.join(DATA_DIR, 'indoor_outdoor/video_category_data.json'), 'r') as f:
		vcd = json.load(f)

	indoor_ids = {iop_data.name_to_idx(name, vocab) for name in iop_data.INDOOR_CATS}
	outdoor_ids = {iop_data.name_to_idx(name, vocab) for name in iop_data.OUTDOOR_CATS}

	# Get corresponding picture ids
	indoor_pics = {data['long_id'] for data in vcd if iop_data.is_indoor(data['labels'], indoor_ids, outdoor_ids)}
	outdoor_pics = {data['long_id'] for data in vcd if iop_data.is_outdoor(data['labels'], indoor_ids, outdoor_ids)}

	# Copy files
	dataset_paths = iop_data.make_dirs(DATA_DIR)

	iop_data.copy_files(
		indoor_pics,
		DATA_DIR,
		dataset_paths,
		class_name='indoor',
		n_train=200,
		n_val=93
	)
	iop_data.copy_files(
		outdoor_pics,
		DATA_DIR,
		dataset_paths,
		class_name='outdoor',
		n_train=200,
		n_val=93
	)


if __name__ == '__main__':
	main()
