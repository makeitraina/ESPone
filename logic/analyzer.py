import re

from static.grammar import score_words

def is_score_related(words):
	key_word_count = 0
	extra_word_count = 0
	for word in words:
		if word in score_words['key_words']:
			key_word_count += 1
		elif word in score_words['extra_words']:
			extra_word_count += 1
	matching_words = [1 for word in words if word in score_words]
	return (key_word_count > 1) or (key_word_count > 0 and (extra_word_count > 1))

def lexify_string(str):
	str = str.strip().lower()
	str = str.translate(None, '.,?!#~`@$%^&*()_=+/;:|]}{[><\\\"')
	str = re.sub('er$', '', str)
	str = re.sub('ing$', '', str)
	str = re.sub('([0-9]+)-([0-9]+)$', '_-_', str)
	return str

def should_add_article(data):
	words_in_description = data.split()
	lexified_words = [lexify_string(word) for word in words_in_description]
	return is_score_related(lexified_words)

def process(articles):
	return {article_name: article_data for article_name, article_data in articles.iteritems() \
		if should_add_article(article_data['description'])}
