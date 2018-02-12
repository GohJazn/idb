import flask
import json
import flickrapi
import sys
from photo import Photo

"""
secrets used in request
TODO: hide these
"""
api_key = '646861afb9b6bf211e4b286b447ad794'
api_secret = '1bb508d092416b93'


"""
Lat and long of Austin, TX
Radius in KM
"""
LATITUDE = '30.2672'
LONGITUDE = '97.7431'
RADIUS = '30'

photos = []
flickr = flickrapi.FlickrAPI(api_key, api_secret, format='json')

def search_photos_scenic() :
    TAGS = 'zilkerpark'
    raw_json = flickr.photos.search(tags=TAGS, media="photo", page=1, per_page=1)
    parsed_dict = json.loads(raw_json.decode('utf-8')) #puts all json into dictionary object
    parse_search(parsed_dict)

def search_photos_coffee() :
    TAGS = 'HoundStooth Coffee'
    raw_json = flickr.photos.search(tags=TAGS, media="photo", page=1, per_page=2)
    parsed_dict = json.loads(raw_json.decode('utf-8'))
    parse_search(parsed_dict)

def parse_search(parsed_dict) :
    for key, value in parsed_dict['photos'].items():
        if(type(value) is list) :
            for item in value:
                url = create_url(item)
                num_favorites = count_favorites(item['id'])
                photo_info = get_info(item['id'], item['secret'])
                photo = parse_info(photo_info, item['id'], item['secret'])
                photos.append(photo)

def parse_info(photo_item, photo_id, photo_secret) -> Photo :
    url = create_url(photo_item)
    num_favs = count_favorites(photo_id)
    date_taken = photo_item['dates'].get('taken')
    location = ''
    lat = ''
    lon = ''
    if 'location' in photo_item :
        location = photo_item['location']
        lat = location.get('latitude')
        lon = location.get('longitude')
    owner = photo_item['owner']
    name = owner.get('realname')
    username = owner.get('username')
    title = photo_item['title'].get('_content')
    tags  = photo_item['tags'].get('tag')
    all_tags = ''
    for t in tags :
        if t['raw'][0] is "#" :
            all_tags = all_tags + t['raw']
    photo = Photo(num_favs, name, username, lat, lon, title, url, tags, photo_id, photo_secret)
    return photo

def create_url(item) -> str :
    url = 'https://farm' + str(item['farm']) + '.staticflickr.com/' \
    + str(item['server']) + '/' + str(item['id']) + '_' + str(item['secret']) \
     + '.jpg'
    return url

def get_info(photo_id, photo_secret) -> dict :
   global api_key
   raw_json = flickr.photos.getInfo(api_key=api_key, photo_id=photo_id, secret=photo_secret)
   parsed_dict = json.loads(raw_json.decode('utf-8'))
   photo_info = parsed_dict['photo']
   return photo_info

def count_favorites(photo_id) :
    raw_json = flickr.photos.getFavorites(api_key=api_key, photo_id=photo_id)
    parsed_dict = json.loads(raw_json.decode('utf-8'))
    count = 0
    for person in parsed_dict['photo'].get('person') :
        count = count + 1
    return count

def start() -> list :
    search_photos_scenic()
    search_photos_coffee()
    return photos

start()