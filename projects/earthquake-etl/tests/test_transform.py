from src.transform import transform_earthquake

def test_valid_earthquake():
    # Create a valid earthquake dictionary
    valid_earthquake = {
    'id': 'us12345',
    'mag': '4.5',
    'depth': '12',
    'place': 'Alaska'
    }
    # Call transform_earthquake()
    result = transform_earthquake(valid_earthquake)

    # Verify the returned values
    assert result['mag'] == 4.5
    assert result['depth'] == 12.0

def test_missing_magnitude():
    invalid_earthquake = {
    'id': 'us12345',
    'mag': '',
    'depth': '12',
    'place': 'Alaska'
    }

    result = transform_earthquake(invalid_earthquake)

    assert result is None

def test_missing_depth():
    invalid_earthquake = {
    'id': 'us12345',
    'mag': '4.5',
    'depth': '',
    'place': 'Alaska'
    }

    result = transform_earthquake(invalid_earthquake)

    assert result is None

def test_invalid_magnitude():
    invalid_earthquake = {
    'id': 'us12345',
    'mag': 'unknown',
    'depth': '10.5',
    'place': 'Alaska'
    }

    result = transform_earthquake(invalid_earthquake)

    assert result is None

def test_invalid_magnitude():
    invalid_earthquake = {
    'id': 'us12345',
    'mag': '4.5',
    'depth': 'unkown',
    'place': 'Alaska'
    }

    result = transform_earthquake(invalid_earthquake)

    assert result is None

def test_invalid_depth():
    invalid_earthquake = {
        'id' : 'us12345',
        'mag' : '4.5',
        'depth' : 'unknown',
        'place' : 'Alaska'
    }
    
    result = transform_earthquake(invalid_earthquake)

    assert result is None

def test_missing_depth_key():
    invalid_earthquake = {
        "id": "us12345",
        "mag": "4.5",
        "place": "Alaska"
    }

    result = transform_earthquake(invalid_earthquake)

    assert result is None

def test_missing_id():
    invalid_earthquake = {
        'mag' : '4.5',
        'depth' : 'unknown',
        'place' : 'Alaska'
    }

    result = transform_earthquake(invalid_earthquake)

    assert result is None


def test_missing_place():
    invalid_earthquake = {
        'id' : 'us12345',
        'mag' : '4.5',
        'depth' : 'unknown'
    }

    result = transform_earthquake(invalid_earthquake)

    assert result is None