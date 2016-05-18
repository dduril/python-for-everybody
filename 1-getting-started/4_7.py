def computegrade(score):
  if score < 0.6:
    grade = 'F' 
  elif score < 0.7:
    grade = 'D'
  elif score < 0.8:
    grade = 'C'
  elif score < 0.9:
    grade = 'B'
  elif score <= 1.0:
    grade = 'A'
  else:
    grade = 'Bad score'
  return grade
  
try:
  s = raw_input('Enter score: ')
  score = float(s)
except:
  print('Bad score')
  quit()
   
print computegrade(score)
 