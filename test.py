import spacer 
import random
import colorama

def get_random_message(state):
	happy_choices = ["niceeeee!", "good job!!", "yassssssssssss!", "LETS GOOOOO!", "whoop whoop!"]
	sad_choices = ["oooops,","arghh oh well,","something's not quite right","uhhhhhh","ummmmmmm","hmmmmm..","uhh... sure?"]
	if state == "pass":
		choice = random.choice(happy_choices)
	elif state == "fail":
		choice = random.choice(sad_choices)
	else:
		raise Exception("????????")
	return choice

def get_colour(state):
	if state == "fail":
		colour = colorama.Fore.RED
	elif state == "pass":
		colour = colorama.Fore.GREEN
	return colour
	
def display_message(state, actual, expected):
	random_celebration = get_random_message(state)
	colour = get_colour(state)
	print(f"{colour}{random_celebration} \nresult: {actual}\nexpected: {expected}")

def assert_equals(actual,expected):
	if actual != expected:
		display_message("fail", actual, expected)
		exit()
	else:
		display_message("pass",actual, expected)
	return

def test_standard():
	string_list = ["green","orange","purple"]
	new_string_list = spacer.remove_new_lines(string_list)
	assert_equals(new_string_list,["green","orange","purple"])
test_standard()


def test_new_lines():
	string_list = ["green\n","oran\nge","\npu\nrple"]
	new_string_list = spacer.remove_new_lines(string_list)
	assert_equals(new_string_list,["green","orange","purple"])
test_new_lines()


def test_get_from_file():
	file_content = spacer.get_iter_from_file("test data/test.txt")
	assert_equals(file_content,["a","b"])
test_get_from_file()

def file_new_lines():
	file_content = spacer.get_iter_from_file("test data/test new lines.txt")
	assert_equals(file_content,["a","b", "c"])
file_new_lines()