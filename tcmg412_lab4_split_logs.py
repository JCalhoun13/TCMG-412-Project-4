import requests
import os

if not os.path.isdir("log_data"):
    os.mkdir("log_data")

# separate lines by month
months = {}
i = 0
# for each line
for line in open("log_data.txt", 'r'):
    print(i)
    i += 1
    fileinfo = line.split()
    if len(fileinfo) < 4:
        continue

    # if valid request
    else:
        date = fileinfo[3].split('/')

        # if valid date
        if len(date) > 1:

            # store line in dictionary
            if date[1] not in months.keys():
                months[date[1]] = line
            else:
                months[date[1]] += line

# for each month
for key in months:
    if "." not in str(key):

        # write to file
        with open(os.sep.join(["log_data", f"{key}.txt"]), 'w') as file:
            file.write(months[key])
            file.close()

