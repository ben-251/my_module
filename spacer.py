class Iter_item:
	string = ""
	spacing = 0
	spacing_character = " "

	def __init__(self,string):
		self.string = string
	
	def make_spaces(self):
		string = ""
		for i in range(self.spacing):
			string += self.spacing_character
		return string
		

class Iterable:
	iterable = []
	longest_string_length = 0
	margin = 8
	
	def __init__(self,iterable):
		self.iterable = iterable
		
	def set_spacings(self):
		# space out based on length of longest one,
		# making that one have a spacing of one to the next one
		#
		# then check the ends of the next iterable and repeat
		self.longest_string_length = max(map(len, self.iterable))
		for index,string in enumerate(self.iterable):
			string_object = Iter_item(string)
			string_object.spacing  = self.get_spacing(string_object)
			self.iterable[index] = string_object

	def get_spacing(self,string_object):
		max_spacing = self.longest_string_length + self.margin
		spacing = max_spacing - len(string_object.string)
		return spacing
		
def space(iterable1,iterable2):
	iter1 = Iterable(iterable1)
	iter2 = Iterable(iterable2)

	iter1.set_spacings()
	iter2.set_spacings()
	output = create_output_string(iter1,iter2)
	return output

def space_multiple(iterables):
	for iterable in iterables:
		pass


def create_output_string(iter1,iter2):
	output = ""
	for index, (item1,item2) in enumerate(zip(iter1.iterable,iter2.iterable)):
		if index != len(iter1.iterable)-1:
			output += item1.string + item1.make_spaces() + item2.string + "\n"
		else:
			output += item1.string + item1.make_spaces() + item2.string
			
	return output


def main():
	list1 = [
		"this",
		"that",
		"this and that and everything in between",
		"."
	]

	list2 = [
		"th",
		"are",
		"benji",
		".",
		"asd"
	]
	print(space(list1, list2))

if __name__ == "__main__":
	main()