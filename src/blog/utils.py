import datetime
import re


from django.utils.html import strip_tags


def count_word():
	# html_string = """"<h1>Wat was that's</h1>"""
	word_string = strip_tags(html_string)
	match_word = re.findall(r'\w+', word_string)
	count = len(match_word)
	return count

def read_time(html_string):
	count = count_word(html_string)
	time_min = (count/200.0)
	time_sec = time_min * 60
	time = str(datetime.timedelta(seconds=time_sec))
	return time
