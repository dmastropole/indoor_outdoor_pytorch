import pytest
import pandas as pd
import numpy as np

import indoor_outdoor_pytorch.data as iop_data


def test_name_to_idx():
    df = pd.DataFrame({
        'Index': [0, 1],
        'Name': ['kitchen', 'mountain']
    })

    idx = iop_data.name_to_idx('kitchen', df)
    assert idx == 0

@pytest.mark.parametrize('labels, truth', [
	([1], True),
	([1, 2, 7], True),
	([1, 4], False),
	([4, 7], False),
	([7], False)
])
def test_is_indoor(labels, truth):
	indoor_ids = {1, 2, 3}
	outdoor_ids = {4, 5, 6}
	res = iop_data.is_indoor(labels, indoor_ids, outdoor_ids)
	assert res == truth

@pytest.mark.parametrize('labels, truth', [
	([1], True),
	([1, 2, 7], True),
	([1, 4], False),
	([4, 7], False),
	([7], False)
])
def test_is_outdoor(labels, truth):
	outdoor_ids = {1, 2, 3}
	indoor_ids = {4, 5, 6}
	res = iop_data.is_outdoor(labels, indoor_ids, outdoor_ids)
	assert res == truth
