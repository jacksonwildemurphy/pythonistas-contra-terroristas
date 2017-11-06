# Written by Jackson Murphy and Kelsey Heidarian. Last updated November 5, 2017.

#from numpy import dot
#from numpy.linalg import norm
import re
import spacy
nlp = spacy.load("en")
import sys

# Returns the number of times a variation of the word "arson" is found in the story
def count_arson_mentions(story):
	_story = story.lower()
	pattern = re.compile(r"(\bburn|\bset fire|\bon fire)")
	return len(re.findall(pattern, _story))

# Returns the number of times a variation of the word "bomb" is found in the story
def count_bombing_mentions(story):
	_story = story.lower()
	pattern = re.compile(r"(\bbomb)")
	return len(re.findall(pattern, _story))

# Returns the number of times a variation of the word "kidnap" or "abduct"
# is found in the story
def count_kidnapping_mentions(story):
	_story = story.lower()
	pattern = re.compile("(kidnap|abduct)")
	return len(re.findall(pattern, _story))

# Returns 0 for now because robbery never appears in the test data
def count_robbery_mentions(story):
	return 0

# Determines which type of incident is most likely, based on the
# words found in the story. Arson and kidnapping take precedence in cases
# where multiple types of incidents are mentioned, as words associated with
# "bombing" and "attack" are sometimes found in arson and kidnapping events
def determine_incident(arson_mentions, bombing_mentions, kidnapping_mentions):
	if bombing_mentions > 0 and kidnapping_mentions > 0:
		pass
		#print("story had references to both bombing and kidnapping!")
	if bombing_mentions > 0 and arson_mentions > 0:
		pass
		#print("story had references to both bombing and arson!")
	if arson_mentions > 0:
		#arson_stories[0] += 1
		return "ARSON"
	elif kidnapping_mentions > 0:
		#kidnapping_stories[0] += 1
		return "KIDNAPPING"
	elif bombing_mentions > 0:
		#bombing_stories[0] += 1
		return "BOMBING"
	else:	# "attack" seems a good catchall, according to the train data
		#attack_stories[0] += 1
		return "ATTACK"

# Returns the incident of the story. The 5 possible incidents are:
# "arson", "attack", "bombing", "kidnapping", or "robbery"
def extract_incident(story):
	arson_mentions = count_arson_mentions(story)
	bombing_mentions = count_bombing_mentions(story)
	kidnapping_mentions = count_kidnapping_mentions(story)
	incident = determine_incident(
		arson_mentions, bombing_mentions, kidnapping_mentions)
	return incident

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
	# weapon = extract_weapons(story)
	# perp_indiv = extract_perp_indiv(story)
	# perp_org = extract_perp_org(story)
	# target = extract_target(story)
	# victim = extract_victim(story)
	print("ID:", story_id)
	print("INCIDENT:", incident)
	print("WEAPON: -")
	print("PERP INDIV: -")
	print("PERP ORG: -")
	print("TARGET: -")
	print("VICTIM: -")
	print()


###### START OF PROGRAM ######

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
