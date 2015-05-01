# coding = utf-8

import re
import codecs
# from datetime import datetime

"""
Kindle Note Formate:
Book title
Position, Datetime
Content of note
"""

def processMetaLine(meta):
	lst = meta.split('|')
	posPattern = r'#\d+-\d+'
	pos = re.search(posPattern,lst[0])
	#print "position: "+pos.group()

	dateList = lst[-1].split()
	datePatten = r'(\d+).*(\d+).*(\d+)'
	dt = re.search(datePatten, dateList[-2])
	#print "date: " + dt.group()
	tm = re.search(datePatten, dateList[-1])
	#print "time: " + tm.group()

# load file
file_handler = codecs.open('TestClippings.txt', 'r', 'utf-8')

# text = file_handler.read()
# text = text.encode('utf-8')
# print text

kStartPatten = r"=========="

blockNum = 0
note_dict = {}
while True:
	title = file_handler.readline().encode('utf-8')
	if not title:
		break
	blockNum += 1
	print "note ", blockNum
	title = title.strip()
	print "book title: ", title
	meta = file_handler.readline().encode('utf-8').strip()
	processMetaLine(meta)
	# print "meta infor: ", meta
	# blank line
	file_handler.readline()
	note = file_handler.readline().encode('utf-8').strip()
	if note:
		if title in note_dict.keys():
			note_dict[title].append(note)
		else:
			note_dict[title] = [note]
	else:
		print "blank note"
	# print "note content: ", note
	file_handler.readline()

# for k in note_dict.keys():
# 	print k
# 	print note_dict[k]
# print note_dict
for k in note_dict.keys():
	filename = unicode(k,'utf-8')+".txt"
	while True:
		write_flag = raw_input("Would you like to save notes of book?[y/n]")
		if write_flag.lower() == 'y':
			out_file_handler = codecs.open(filename,'w','utf-8')
			for n in note_dict[k]:
				print n
				out_file_handler.write('- '+unicode(n,'utf-8'))
				out_file_handler.write('\n')
			out_file_handler.close()
			break
		elif write_flag.lower() == 'n':
			print 'skip notes of book'
			break
		else:
			print 'invalid input'

file_handler.close()