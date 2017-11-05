import sys
#from numpy import dot
#from numpy.linalg import norm
#from spacy.en import English
#parser = English()

def extract_incident(story):
	pass

def extract_weapons(story):
	pass

def extract_perp_indiv(story):
	pass

def extract_perp_org(story):
	pass

def extract_target(story):
	pass

def extract_victim(story):
	pass

def line_is_story_id(line):
	if "DEV-MUC3" in line or "TST1-MUC3" in line or "TST2-MUC4" in line:
		return True
	return False

def extract_info(story, story_id):
	incident = extract_incident(story)
	weapon = extract_weapons(story)
	perp_indiv = extract_perp_indiv(story)
	perp_org = extract_perp_org(story)
	target = extract_target(story)
	victim = extract_victim(story)

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
		while line and not line_is_story_id(line):
			story += line
			line = file.readline()

		extract_info(story, story_id)



file.close()
