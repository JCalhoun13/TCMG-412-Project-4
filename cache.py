from urllib.request import urlopen
response = urlopen(https://s3.amazonaws.com/tcmg476/http_access_log) 
data = response.read()

# Write data to file
filename = "test.txt"
file_ = open(filename, 'w')
file_.write(data)
file_.close()