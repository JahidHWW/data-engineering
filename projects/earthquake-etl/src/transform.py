def transform_earthquake(row):
    row_id = row.get('id')
    mag = row.get('mag')
    depth = row.get('depth')
    row_place = row.get('place')

    if row_id is None or mag is None or depth is None or row_place is None:
        return None
    
    if row_id == '' or mag == '' or depth == '' or row_place == '':
        return None
    
    try:
        row_mag = float(mag)
        row_depth = float(depth)
    except ValueError:
        return None

    transformed_row = {
        'id' : row_id,
        'mag' : row_mag,
        'depth' : row_depth,
        'place' : row_place
        }
    
    return transformed_row

if __name__ == '__main__':
    sample = {
    'id': 'us12345',
    'mag': '4.5',
    'depth': '',
    'place': 'Alaska'
    }
    result = transform_earthquake(sample)
    if result is None:
        print('Record rejected: invalid or missing data')
    else:
        print(result)
        print(type(result['mag']))
        print(type(result['depth']))