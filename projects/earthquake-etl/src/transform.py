def transform_earthquake(row):
    if row['mag'] == "" or row['depth'] == "":
        return None
    row_id = row['id']
    row_mag = float(row['mag'])
    row_depth = float(row['depth'])
    row_place = row['place']

    transformed_row = {
        'id' : row_id,
        'mag' : row_mag,
        'depth' : row_depth,
        'place' : row_place
        }
    
    return transformed_row

sample = {
    'id': 'us12345',
    'mag': '4.5',
    'depth': '',
    'place': 'Alaska'
}

if __name__ == "__main__":
    result = transform_earthquake(sample)
    if result is None:
        print('Record rejected: invalid or missing data')
    else:
        print(result)
        print(type(result['mag']))
        print(type(result['depth']))