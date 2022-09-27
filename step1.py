import requests
import re
# Get data from URL
response = requests.get("https://s3.amazonaws.com/tcmg476/http_access_log")
data1 = response.text

data1
x = re.search(".*\[([0-9]+/[Oct]+/[0-9]{4}):", data1)

if x:
  print("YES! We have a match!")
else:
  print("No match")
  
  
#pattern = '.*\[([24]+/[Oct]+/[0-9]{4}):'  
pattern = '.*\[([0-9]+/[Oct]+/[0-9]{4}):'
count = 0
for match in re.finditer(pattern, data1):
   count += 1

print(count)



#the two pattern versions count the days or months in the logfile.
#I haven't figured out how to make it count the days without manually telling it the days/months to count
