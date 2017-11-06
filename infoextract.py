#from numpy import dot
#from numpy.linalg import norm
import re
import spacy
nlp = spacy.load("en")
import sys

# Returns the number of times a variation of the word "arson" is found in the story
def count_arson_mentions(story):
	_story = story.lower()
	pattern = re.compile(r"(\bburn|\bablaze|\bset fire|\bon fire\b)")
	return len(re.findall(pattern, _story))

# Returns the number of times a variation of the word "kidnap" or "abduct"
# is found in the story
def count_kidnapping_mentions(story):
	_story = story.lower()
	pattern = re.compile("(kidnap|abduct)")
	return len(re.findall(pattern, _story))


# Returns the incident of the story. The 5 possible incidents are:
# "arson", "attack", "bombing", "kidnapping", or "robbery"
def extract_incident(story):
	arson_mentions = count_arson_mentions(story)
	#attack_mentions = count_attack_mentions(story)
	#bombing_mentions = count_bombing_mentions(story)
	kidnapping_mentions = count_kidnapping_mentions(story)
	#robbery_mentions = count_robbery_mentions(story)
	if arson_mentions > 0 and kidnapping_mentions > 0:
		print("story had references to both arson and kidnapping!")
	elif arson_mentions > 0:
		arson_stories[0] += 1
		return "arson"
	elif kidnapping_mentions > 0:
		kidnapping_stories[0] += 1
		return "kidnapping"
	# incident = determine_incident(
	# 	arson_mentions, attack_mentions, bombing_mentions, kidnapping_mentions, robbery_mentions)


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
	# print("Finished story!\n")
	if incident == "arson":
		print(story_id, "was tagged as arson")
	elif incident == "kidnapping":
		print(story_id, "was tagged as kidnapping")	


###### START OF PROGRAM ######

arson_stories = [0]
kidnapping_stories = [0]

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

print("Identified arson as the incident for this many stories:", arson_stories[0])
print("Identified kidnapping as the incident for this many stories:", kidnapping_stories[0])

file.close()
