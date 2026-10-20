from exif import Image
import pandas as pd


def get_metadata_single(img_path):
    with open(img_path, 'rb') as img_file:
        img = Image(img_file)
        if not img.has_exif:
            print('Image does not have EXIF metadata')
        else:
            df = pd.DataFrame(columns=['attribute', 'value'])
            attr_list = img.list_all()

            # Add image file name
            df = df.append({'attribute': 'image_path',
                           'value': img_path},
                           ignore_index=True)

            for attr in attr_list:
                value = img.get(attr)
                dict_i = {'attribute': attr,
                          'value': value}
                df = df.append(dict_i, ignore_index=True)

            df.sort_values(by='attribute', inplace=True)
            df.set_index('attribute', inplace=True)
            return df


data = get_metadata_single('./1.png')
for key in data:
    print(f"{key}: {data[key]}")
