### LOAD TXT DATA ###

# read in the ratings
def read_ratings_txt(folder, file_name):
    data = []
    counter = 0

    with open(os.path.join(folder, file_name), 'rb') as file:
        rating_data = {}
        for line in file:
            line = line.strip()
            if line.startswith(b'beer_name:'):
                # check if dictionary is not empty
                if rating_data:
                    data.append(rating_data)
                rating_data = {'beer_name': line.split(b'beer_name:')[1].decode('utf-8')}
            elif line.startswith(b'beer_id:'):
                rating_data['beer_id'] = line.split(b'beer_id:')[1].decode('utf-8')
            elif line.startswith(b'brewery_name:'):
                rating_data['brewery_name'] = line.split(b'brewery_name:')[1].decode('utf-8')
            elif line.startswith(b'brewery_id:'):
                rating_data['brewery_id'] = line.split(b'brewery_id:')[1].decode('utf-8')
            elif line.startswith(b'style:'):
                rating_data['style'] = line.split(b'style:')[1].decode('utf-8')
            elif line.startswith(b'abv:'):
                rating_data['abv'] = line.split(b'abv:')[1].decode('utf-8')
            elif line.startswith(b'date:'):
                timestamp = float(line.split(b'date:')[1].decode('utf-8'))
                rating_data['date'] = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
            elif line.startswith(b'user_name:'):
                rating_data['user_name'] = line.split(b'user_name:')[1].decode('utf-8')
            elif line.startswith(b'user_id:'):
                rating_data['user_id'] = line.split(b'user_id:')[1].decode('utf-8')
            elif line.startswith(b'appearance:'):
                rating_data['appearance'] = line.split(b'appearance:')[1].decode('utf-8')
            elif line.startswith(b'aroma:'):
                rating_data['aroma'] = line.split(b'aroma:')[1].decode('utf-8')
            elif line.startswith(b'palate:'):
                rating_data['palate'] = line.split(b'palate:')[1].decode('utf-8')
            elif line.startswith(b'taste:'):
                rating_data['taste'] = line.split(b'taste:')[1].decode('utf-8')
            elif line.startswith(b'overall:'):
                rating_data['overall'] = line.split(b'overall:')[1].decode('utf-8')
            elif line.startswith(b'rating:'):
                rating_data['rating'] = line.split(b'rating:')[1].decode('utf-8')
            elif line.startswith(b'text:'):
                rating_data['text'] = line.split(b'text:')[1].decode('utf-8')
            elif line.startswith(b'review:'):
                rating_data['review'] = line.split(b'review:')[1].decode('utf-8')

            #counter += 1

            #if counter == 100000000:  # limit amount of lines to read in (17lines in the data are 1 row)
            #    break

    if rating_data:
        data.append(rating_data)

    ratings = pd.DataFrame(data)
    return ratings


# read in the reviews
def read_reviews_txt(folder, file_name):
    data = []
    counter = 0

    with open(os.path.join(folder, file_name), 'rb') as file:
        review_data = {}
        for line in file:
            line = line.strip()
            if line.startswith(b'beer_name:'):
                # check if dictionary is not empty
                if review_data:
                    data.append(review_data)
                review_data = {'beer_name': line.split(b'beer_name:')[1].decode('utf-8')}
            elif line.startswith(b'beer_id:'):
                review_data['beer_id'] = line.split(b'beer_id:')[1].decode('utf-8')
            elif line.startswith(b'brewery_name:'):
                review_data['brewery_name'] = line.split(b'brewery_name:')[1].decode('utf-8')
            elif line.startswith(b'brewery_id:'):
                review_data['brewery_id'] = line.split(b'brewery_id:')[1].decode('utf-8')
            elif line.startswith(b'style:'):
                review_data['style'] = line.split(b'style:')[1].decode('utf-8')
            elif line.startswith(b'abv:'):
                review_data['abv'] = line.split(b'abv:')[1].decode('utf-8')
            elif line.startswith(b'date:'):
                timestamp = float(line.split(b'date:')[1].decode('utf-8'))
                review_data['date'] = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
            elif line.startswith(b'user_name:'):
                review_data['user_name'] = line.split(b'user_name:')[1].decode('utf-8')
            elif line.startswith(b'user_id:'):
                review_data['user_id'] = line.split(b'user_id:')[1].decode('utf-8')
            elif line.startswith(b'appearance:'):
                review_data['appearance'] = line.split(b'appearance:')[1].decode('utf-8')
            elif line.startswith(b'aroma:'):
                review_data['aroma'] = line.split(b'aroma:')[1].decode('utf-8')
            elif line.startswith(b'palate:'):
                review_data['palate'] = line.split(b'palate:')[1].decode('utf-8')
            elif line.startswith(b'taste:'):
                review_data['taste'] = line.split(b'taste:')[1].decode('utf-8')
            elif line.startswith(b'overall:'):
                review_data['overall'] = line.split(b'overall:')[1].decode('utf-8')
            elif line.startswith(b'rating:'):
                review_data['rating'] = line.split(b'rating:')[1].decode('utf-8')
            elif line.startswith(b'text:'):
                review_data['text'] = line.split(b'text:')[1].decode('utf-8')

            #counter += 1

            #if counter == 100000000:  # limit amount of lines to read in
            #    break

    if review_data:
        data.append(review_data)

    reviews = pd.DataFrame(data)
    return reviews



### TIME CONVERSION ###

from datetime import datetime

# convert the joined (date) column
def convert_timestamp(timestamp):
    try:
        timestamp = float(timestamp)
        return datetime.fromtimestamp(timestamp)
    except (ValueError, TypeError):
        return None
    

### UNICODE CONVERSION

# convert all unicodes that are displayed wrongly
def unicode_conversion(df):
    replacements = {
        'Ã³': 'ó',
        'Ã¡': 'á',
        'Ã©': 'é',
        'Å‚': 'ł',
        "Ã¢Â€Â™": "’",
        'Ã±': 'ñ',
        'Ã\xad': 'í',
        'Ã¶': 'ö',
        "Ã¤": "ä",
        "Ã¥": "å",
        "Ã¶": "ö",
        "Ã¸": "ø",
        "Ã¦": "æ",
        'Ã\x9f': 'ß',
        "Ã¨": "è",
        'Â£': '£',
        'â\x80\x93': '-',
        "Ã´": "ô",
        "â\x80\x99": "’",
        "Ã¼": "ü",
        "Â\xa0": "",
        "\xa0": " ",
        "[email\xa0protected]/* */": "",
        "[email protected]/*  */": "",
        "Ã®": "î",
        "Ãª": "ê",
        "Ã»": "û",
        'Ã»': 'û',
        "Ã\x87": "Ç",
        'Ã§': 'ç',
        "Ã": "à",
        "Ã¢": "â",
        "Ã¯": "ï",
        "Ã\x89": "é",
        'Ã\x89': 'é',
        'Ã¨': 'è',
        "Ã©": 'é',
        "à\x89": "É",
        "à¹": "ù",
        "àº": "ú",
        "Â«": "«",
        "Â»": "»",
        "à¢": "â",
        "â\x80\x9c": "“",
        "â\x80\x9d": "”",
        "&quot;": "'",
        "à\x80": "À",
        "à\x88": "È",
        "Å\x93": "œ",
        "â\x80": "...",
        "\'": "'"
    }

    def replace_chars(text):
        if isinstance(text, str):  # Check if the value is a string
            for old, new in replacements.items():
                text = text.replace(old, new)
        return text

    return df.apply(replace_chars)

# source: https://www.i18nqa.com/debug/utf8-debug.html, and ChatGPT