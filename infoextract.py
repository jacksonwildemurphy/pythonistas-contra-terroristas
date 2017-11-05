import sys
#from numpy import dot
#from numpy.linalg import norm
#from spacy.en import English
#parser = English()


def line_is_story_id(line):
	if "DEV-MUC3" in line or "TST1-MUC3" in line or "TST2-MUC4" in line:
		print("Hey Jackson, this line is a story id:", line)
		return True
	return False

def extract_info(story, story_id):
	print("----------------------------")
	print("ID:", story_id)
	print(story)
	print("----------------------------")


if len(sys.argv) != 2:
	print("Please specifiy a file.")
	sys.exit(2)

file_name = sys.argv[1]
file = open(file_name, 'r')
line = file.readline()
while line:
	while not line_is_story_id(line):
		line = file.readline()
	if line_is_story_id(line):
		story_id = line.split()[0]
		story = ""
		line = file.readline()
		'''while line and not line_is_story_id(line):
			story += line'''

		extract_info(story, story_id)



file.close()

