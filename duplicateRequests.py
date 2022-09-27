url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")

print('Check to see log already exists:')

if  not path.exists('log'):
	print('Log did not exist, downloading: ')
	print(url)
	urllib.request.urlretrieve(url, 'log')
	print('Finished Downloading')
else:
	print("Log existed, skipping .\n")

file = open('log', 'r')

logfile =[]
    