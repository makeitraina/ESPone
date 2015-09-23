from http import get
from http import post

pinterest_api_url = 'https://api.pinterest.com/v1/'

def create_pin(board,note,link,image_url):
	url = pinterest_api_url + 'pins/'
	params = {
		'board': board,
		'note': note,
		'link': link,
		'image_url': image_url
	}
	response = post(url, params)

def pin_new_items(board, new_data):
	for key in new_data:
		pin_data = new_data[key]
		create_pin(board, key, pin_data.url, pin_data.image_url)

