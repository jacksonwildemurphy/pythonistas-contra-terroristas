# Written by Jackson Murphy and Kelsey Heidarian. Last updated November 5, 2017.

#from numpy import dot
#from numpy.linalg import norm
import re
import spacy
nlp = spacy.load("en")
import sys
import operator

# constants for proper print spacing
ID_SPACING = "\t" * 7
INCIDENT_SPACING = "\t" * 4
WEAPON_SPACING = "\t" * 5
PERP_INDIV_SPACING = "\t" * 3
PERP_ORG_SPACING = "\t" * 4
TARGET_SPACING = "\t" * 5
VICTIM_SPACING = "\t" * 5


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

# Returns the first word in the story that matches a weapon associated with
# bombing, according to the training data
def get_bombing_weapon(story):
	pass

# Returns the weapons found in the story
def get_attack_or_bombing_weapon(story):
	weapon_strings = ['BOMB', 'BOMBS', 'ROCKET', 'ROCKETS', 'MACHINE GUN', 'MACHINEGUNS',
	'MACHINEGUN', 'SUBMACHINEGUN', 'DYNAMITE', 'GRENADE', 'GRENADES', 'AK 47S', 'BULLET',
	'BULLETS',  'MORTAR']
	weapon_count = {w: 0 for w in weapon_strings}
	story_list = story.split()
	for word in story_list:
		if word in weapon_strings:
			weapon_count[word] += 1
	sorted_weapons = sorted(weapon_count.items(), key=operator.itemgetter(1))
	if sorted_weapons[-1][1] != 0:
		return sorted_weapons[-1][0]
	else:
		return '-'

# Returns the incident of the story. The 5 possible incidents are:
# "arson", "attack", "bombing", "kidnapping", or "robbery"
def extract_incident(story):
	arson_mentions = count_arson_mentions(story)
	bombing_mentions = count_bombing_mentions(story)
	kidnapping_mentions = count_kidnapping_mentions(story)
	incident = determine_incident(
		arson_mentions, bombing_mentions, kidnapping_mentions)
	return incident

# Returns the weapons used in the terrorist incident, or "-"
# if no weapons were found.
def extract_weapon(story, incident):
	if incident == "ARSON" or incident == "KIDNAPPING":
		return "-" # no training samples had a weapon for these incident types
	else:
		return get_attack_or_bombing_weapon(story)

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

def extract_info(story, story_id, output_file):
	incident = extract_incident(story)
	weapon = extract_weapon(story, incident)

	# perp_indiv = extract_perp_indiv(story)
	# perp_org = extract_perp_org(story)
	# target = extract_target(story)
	# victim = extract_victim(story)
	output_file.write("ID:" + ID_SPACING + story_id + "\n")
	output_file.write("INCIDENT:" + INCIDENT_SPACING + incident + "\n")
	output_file.write("WEAPON:" + WEAPON_SPACING + weapon + "\n")
	output_file.write("PERP INDIV:" + PERP_INDIV_SPACING + "-" + "\n")
	output_file.write("PERP ORG:" + PERP_ORG_SPACING + "-" + "\n")
	output_file.write("TARGET:" + TARGET_SPACING + "-" + "\n")
	output_file.write("VICTIM:" + VICTIM_SPACING + "-" + "\n")
	output_file.write("\n")


###### START OF PROGRAM ######

if len(sys.argv) != 2:
	print("Please specifiy a file.")
	sys.exit(2)

input_file_name = sys.argv[1]
input_file = open(input_file_name, 'r')
line = input_file.readline()
output_file = open(input_file_name + ".templates", "w+")

while line:
	while not line_is_story_id(line):
		line = input_file.readline()
	if line_is_story_id(line):
		story_id = line.split()[0]
		story = ""
		line = input_file.readline()
		while line and not line_is_story_id(line):
			story += line
			line = input_file.readline()

		extract_info(story, story_id, output_file)

input_file.close()
output_file.close()
