from crisp_api import Crisp
from time import sleep
from random import *
import json
from datetime import datetime
# api credentials stored in another file for security reasons - have to have those two variables defined in another file
from crisp_info import api_key, api_token,website_id
import csv

outputFile=open('sessions.csv','w',newline='', encoding='utf-8')
outputWriter=csv.writer(outputFile)
outputWriter.writerow(['SESSION ID:', 'CREATED AT:', 'UPDATED AT:', 'SEGMENTS', 'COUNTRY:'])

client=Crisp()
client.authenticate(api_key,api_token)
print('I should be authenticated to the CRISP API')

MILLISECONDS = 1000
conversation_data=[]
i=1
                                  
while bool(client.website.list_conversations(website_id,i)):
    
    current_batch_of_conversations=client.website.list_conversations(website_id,i)
    print(i)
    #sleep - avoid CRISP API limitation
    sleep(uniform(1,3))
    conversation_data += current_batch_of_conversations
    i+=1
print('Out of the loop')
json.dump(conversation_data, open('conversations.json','w'), indent=4)
        
for i in conversation_data:
    current_session_id = str(i['session_id'])
    timestamp_create=str(datetime.fromtimestamp(i['created_at']/ MILLISECONDS))
    timestamp_update=str(datetime.fromtimestamp(i['updated_at']/ MILLISECONDS))
    current_segment = str(i['meta']['segments'])
    try:
        current_location = str(i['meta']['device']['geolocation']['country'])
    except:
        current_location="N/A - COUNTRY NOT FOUND"
    
    outputWriter.writerow([current_session_id,timestamp_create,timestamp_update,current_segment,current_location])
print('After the loop, everything should be done')
outputFile.close()
                          



