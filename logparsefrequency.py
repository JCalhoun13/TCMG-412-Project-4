# writing one chunk at a time to pdf file
if chunk:
textfile.write(chunk)
result={
"total_requests":0,
"per_day_data":{},
"per_week_data":{},
"per_month_data":{},
"request_not_successful":0,
"requests_redirected_elsewhere":0,
"filewise_request_frequency":{},
"most_requested_file":[0,[]], #maximum request and list of all files with that number of request
"least_requested_file":[0,[]] #minimum request and list of all files with that number of request
}