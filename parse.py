total_requests = 0
past_sixmonths = 0

for line in open(filename):
    fileinfo = line.split()
    
    if(len(fileinfo) < 4):
        continue
    else:
        date = fileinfo[3].split('/')
        if((date[0][1:] == '11') and (date[1] == 'Apr') and (date[2][:4] == '1995')):
            past_sixmonths += 1
    
    total_requests += 1


