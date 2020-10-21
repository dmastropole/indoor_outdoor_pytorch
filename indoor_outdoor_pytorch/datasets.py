import os
import torch
import torchvision as tv


def get_datasets(data_dir):
	# Data augmentation and normalization
	data_transforms = {
		'train': tv.transforms.Compose([
			tv.transforms.Resize((90, 120)),
			tv.transforms.RandomHorizontalFlip(),
			tv.transforms.ToTensor(),
			tv.transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
		]),
		'val': tv.transforms.Compose([
			tv.transforms.Resize((90, 120)),
			tv.transforms.ToTensor(),
			tv.transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
		])
	}

	# Create datasets
	image_datasets = {
		'train': tv.datasets.ImageFolder(
			os.path.join(data_dir, 'train'), data_transforms['train']
		),
		'val': tv.datasets.ImageFolder(
			os.path.join(data_dir, 'val'), data_transforms['val']
		)
	}

	dataloaders = {
		'train': torch.utils.data.DataLoader(
			image_datasets['train'],
			batch_size=4,
			shuffle=True
		),
		'val': torch.utils.data.DataLoader(
			image_datasets['val'],
			batch_size=4,
			shuffle=False
		)
	}

	# Get dataset sizes
	dataset_sizes = {'train': 400, 'val': 186}

	# Get class names
	class_names = image_datasets['train'].classes

	return dataloaders, dataset_sizes, class_names
