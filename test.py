import spacer 
import test_backend as test


def test_standard():
	string_list = ["green","orange","purple"]
	new_string_list = spacer.remove_new_lines(string_list)
	test.assert_equals(new_string_list,["green","orange","purple"])
test_standard()


def test_new_lines():
	string_list = ["green\n","oran\nge","\npu\nrple"]
	new_string_list = spacer.remove_new_lines(string_list)
	test.assert_equals(new_string_list,["green","orange","purple"])
test_new_lines()


def test_get_from_file():
	file_content = spacer.get_iter_from_file("test data/test.txt")
	test.assert_equals(file_content,["a","b"])
test_get_from_file()

def file_new_lines():
	file_content = spacer.get_iter_from_file("test data/test new lines.txt")
	test.assert_equals(file_content,["a","b", "c"])
file_new_lines()


def test_separated_lists():
	list1 = ["a","bb","ccc","ddd"]
	list2 = [1,2,3,4]
	output_string = spacer.space(list1,list2)
	test.assert_equals(output_string,"a    1\nbb   2\nccc  3\nddd  4")
test_separated_lists()
