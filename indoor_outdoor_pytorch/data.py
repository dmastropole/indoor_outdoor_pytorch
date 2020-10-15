import os
from shutil import copyfile
import json
import pandas as pd


INDOOR_CATS = {
    'Wall',
    'Bathroom',
    'Bedroom',
    'Living room',
    'Classroom',
    'Shower',
    'Basement',
    'Loft',
    'Floor',
    'Carpet',
    'Gym',
    'Room',
    'Elevator',
    'Dining room',
    'Ceiling',
    'Kitchen',
    'Nursery (room)',
    'Wallpaper',
    'Picture frame',
    'Wardrobe',
    'Dishwasher',
    'Plumbing',
    'Closet',
    'Ceiling fan',
    'Couch',
    'Home appliance',
    'Furniture'
}

OUTDOOR_CATS = {
    'Outdoor recreation',
    'Sunset',
    'Snow',
    'Lake',
    'Mountain',
    'Volcano',
    'Underwater',
    'River',
    'Dune',
    'Beach',
    'Wildlife',
    'Forest',
    'Desert',
    'Sky',
    'Garden',
    'Military parade',
    'Skiing',
    'Marching band',
    'Carnival',
    'Gardening',
    'Nature',
    'Off-road vehicle',
    'Graffiti',
    'Trail',
    'Camping',
    'Hiking',
    'Lawn',
    'Roof',
    'Thunderstorm',
    'Traffic',
    'Rafting',
    'Campsite',
    'Cave'
}

def name_to_idx(name_str, df):
    return df['Index'][df['Name']==name_str].to_numpy()[0]

def is_indoor(labels, indoor_ids, outdoor_ids):
    labels = set(labels)
    if labels.isdisjoint(outdoor_ids) and not labels.isdisjoint(indoor_ids):
        return True
    return False

def is_outdoor(labels, indoor_ids, outdoor_ids):
    labels = set(labels)
    if labels.isdisjoint(indoor_ids) and not labels.isdisjoint(outdoor_ids):
        return True
    return False

def make_dirs(data_dir):
    dataset_paths = {}

    def check_make(dataset_dir):
        dataset_path = os.path.join(data_dir, dataset_dir)
        if not os.path.exists(dataset_path):
            os.makedirs(dataset_path)
            dataset_paths[dataset_dir] = dataset_path
        else:
            print(f'{dataset_dir} already exists')

    check_make('train/indoor')
    check_make('train/outdoor')
    check_make('val/indoor')
    check_make('val/outdoor')
    return dataset_paths

def copy_files(fids, data_dir, dataset_paths, class_name, n_train, n_val):

    if dataset_paths:
        for idx, fid in enumerate(fids):
            filename = f'{fid}.jpg'
            if idx < n_train:
                copyfile(
                    os.path.join(data_dir, 'indoor_outdoor', 'images', filename),
                    os.path.join(dataset_paths[f'train/{class_name}'], filename)
                )
            elif idx < n_train + n_val:
                copyfile(
                    os.path.join(data_dir, 'indoor_outdoor', 'images', filename),
                    os.path.join(dataset_paths[f'val/{class_name}'], filename)
                )
            else:
                break
