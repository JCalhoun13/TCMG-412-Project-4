import re

def threexx(total_requests):							
	redirect_count = 0.0
	with open('./http_access_log.txt') as file:				
		for line in file:
			if re.search('\s*(3\d\d)\s\S+', line):
				redirect_count += 1
	print('The percentage of requests that were redirected elsewhere: {0:.2%}'.format(redirect_count / total_requests))		
	
def fourxx(total_requests):							
	error_count = 0.0
	with open('./http_access_log.txt') as file:				
		for line in file:
			if re.search('\s*(4\d\d)\s\S+', line):
				error_count += 1
	print('Percentage of client error (4xx) requests: {0:.2%}'.format(error_count / total_requests))	