import requests


# Get data from URL
response = requests.get("https://s3.amazonaws.com/tcmg476/http_access_log")
data = response.text

# Write data to file
filename = "log_data.txt"
file = open(filename, 'w')
file.write(data)
file.close()

total_requests = 0
past_sixmonths = 0

# Parse data
for line in open(filename):
    fileinfo = line.split()
    if (len(fileinfo) < 4):
        continue
    else:
        date = fileinfo[3].split('/')
        if ((date[0][1:] == '11') and (date[1] == 'Apr') and (date[2][:4] == '1995')):
            past_sixmonths += 1
    total_requests += 1

# Output data
print(f"Total requests: {total_requests}")
print(f"Total requests within the last 6 months: {past_sixmonths}")
