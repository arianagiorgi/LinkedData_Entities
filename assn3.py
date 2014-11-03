### Ariana Giorgi
### 10/31/2014
### Computational Journalism Assignment #3 - Open Calais
### https://code.google.com/p/python-calais/

from calais import Calais
import collections

#set Calais API Key and create new instance
API_KEY = "g8gnzpdz52gkwyduv75zecem"
calais = Calais(API_KEY, submitter = "python-calais demo")

#demo text
input_text = "George Bush was the President of the United States of America until 2009.  Barack Obama is the new President of the United States now."

with open('stdin_1.txt', 'r') as f:
  	input_text = f.read()
f.closed

result = calais.analyze(input_text)
#result.print_entities()

#initialize dictionary that will contain the linked data
link_list = {}
#initialize detected references count (collected for assignment)
detected_count = 0

#loop through each entity and assign a link
for i in range(len(result.entities)):
	if 'resolutions' in result.entities[i]:
		#if Calais has assigned an RDF value, use that as the link
		name = result.entities[i]['name']
		link = result.entities[i]['resolutions'][0]['id']
		link_list[name] = link

		detected_count = detected_count + 1
	else:
		#else, create wikipedia link
		name = result.entities[i]['name']
		newname = name.replace(' ','_') #create a new variable to add onto the wikipedia link
		link = 'http://en.wikipedia.org/wiki/' + newname
		link_list[name] = link

#order the list in alphabetical order - see report for explanation of why I did this
link_list = collections.OrderedDict(sorted(link_list.items()))

#initialize count for number of entity references (collected for assignment)
entity_count = 0

text = input_text
for key in link_list:
	entity_count = entity_count + text.count(key)
	text = text.replace(key, '<a href=' + link_list[key] + '>' + key + '</a>')


with open('stdout_1.html','w') as f:
	f.write('Entity References: ' + str(entity_count) + '</br>')
	f.write('Detected References: ' + str(detected_count) + '</br></br>')
	f.write(text)
f.closed


