#!usr/bin/env python3

import os

def parse_csv(file):
	table = []
	for line in file:
		record = line.replace(", ", ",")
		record = record.strip()
		record = record.split(",")
		table.append(record)
	
	return table

#Check every cell in a column to determine the length of the column
def find_max_column_length(table):
	maxRecordLength = len(table[0])
	maxColumnLength = [0] * maxRecordLength
	
	for record in table:
		for i,cell in enumerate(record):
			if len(cell) > maxColumnLength[i]:
				maxColumnLength[i] = len(cell)	
				
	return maxColumnLength
	
def create_horizontal_border_line(maxColumnLength):
	horizontalBorderLine = "|"
	for number in maxColumnLength:
		horizontalBorderLine += ("-" * number)
		horizontalBorderLine += ("|")
		
	return horizontalBorderLine
	
def create_border_lines(horizontalBorderLine):
	bottomBorderLine = horizontalBorderLine.replace("-", "_")
	topBorderLine = bottomBorderLine.replace("|", "_")
	
	#Editing the first and last characters as a list since strings are immutable in Python
	topBorderLine = list(topBorderLine)
	topBorderLine[0] = " "
	topBorderLine[-1] = " "
	
	#Joining them to create a new string
	topBorderLine = "".join(topBorderLine)
	
	return (topBorderLine,bottomBorderLine)
	
def print_record(record, maxColumnLength):
	line = "|"
	for i,cell in enumerate(record):
		spacing = 0
		if len(cell) < maxColumnLength[i]:
			spacing = maxColumnLength[i] - len(cell)
		line += cell + (" " * spacing) + "|"
	print(line)

def print_2d_table(table):
	maxColumnLength = find_max_column_length(table)
	horizontalBorderLine = create_horizontal_border_line(maxColumnLength)
	
	(topBorderLine,bottomBorderLine) = create_border_lines(horizontalBorderLine)
	print(topBorderLine)
	
	#Print out all the lines but the last since the bottom line needs to be different
	for record in table[:-1]:
		print_record(record, maxColumnLength)
		
		print(horizontalBorderLine)
	else:
		print_record(table[-1], maxColumnLength)
		print(bottomBorderLine)

def main():
	with open("csv.txt") as file:
		table = parse_csv(file)
		print_2d_table(table)

if __name__ == "__main__":
	main()
