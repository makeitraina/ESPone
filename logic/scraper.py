import requests
from lxml import html

BASE_ESPN_URL = "http://espn.go.com"

def get_first_child_element(parent, element_selector):
	element = None
	element_array = parent.cssselect(element_selector)
	if len(element_array) > 0:
		element = element_array[0]

	return element

def get_first_child_element_attribute(parent, element_selector, attribute_selector):
	attribute_val = ""
	element = get_first_child_element(parent, element_selector)
	if element is not None:
		attribute_values = element.xpath(attribute_selector)
		if len(attribute_values) > 0:
			attribute_val = attribute_values[0]
			
	return attribute_val

def parse_html_page_by_team(league, team_key, team_name):
	team_template_url = '{0}/{1}/team/_/name/{2}/{3}'
	team_url = team_template_url.format(BASE_ESPN_URL,league,team_key,team_name)

	page = requests.get(team_url)
	page_html = html.fromstring(page.text)
	articles = page_html.cssselect('div#news-feed-content article')

	for article in articles:
		article_details = []

		# Get the main figure element and body element of article
		main_figure = get_first_child_element(article, 'figure')
		main_body = get_first_child_element(article, 'div.text-container')
		# If the figure or body is not present skip to next article
		if main_figure is None or main_body is None:
			continue
		# extract information from article
		article_details.append(get_first_child_element_attribute(main_body, 'h1 a', 'text()'))
		article_details.append(BASE_ESPN_URL +
			get_first_child_element_attribute(article, 'a.story-link', '@href'))
		article_details.append(get_first_child_element_attribute(main_figure, 'picture img', '@data-default-src'))
		article_details.append(get_first_child_element_attribute(main_body, 'p', 'text()'))
		if "" in article_details:
			continue
		print '--'.join(article_details) + '\n'
