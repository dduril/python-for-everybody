# -------------------------------------
# Python for Informatics
# -------------------------------------
# Course Three
# Using Python to Access Web Data
#
# Assignment 11.2
#
# -------------------------------------
fname = raw_input('Enter file: ')
try:
  fhand = open(fname)
except:
  print 'File cannot be opened:', fname 
  exit()
  
