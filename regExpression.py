import re 

str = "xyz intensive.learnings@cigna.com purple monkey" 
result = re.search(r'[\w\.-]+@[\w\.-]+', str)

print result.group(0) 
