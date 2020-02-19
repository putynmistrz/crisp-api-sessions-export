from crisp_api import Crisp
from time import sleep
from random import *
import json
import jsonpickle
from datetime import datetime
# api credentials stored in another file for security reasons - have to have those two variables defined in another file
from crisp_info import api_key, api_token,website_id
import csv


MILLISECONDS = 1000

client=Crisp()

client.authenticate(api_key,api_token)

print('I should be authenticated to the CRISP API')

## TO DO: do ... while dictionary isnt empty


conversation_data=[]
messages_data=[]
i==1


#max-iterations => limit
#max_iterations = 2
#while i<=max_iterations:


      
def print_menu():       
    print (30 * "-" , "MENU" , 30 * "-")
    print ("1. Gather ALL session IDs + compile them into 1 big JSON file")
    print ("2. Load existing JSON file and store filtered data in .CSV")
    print ("3. Do the first and second option at the same time (generate JSON -> store important data in CSV")
    print ("4. Exit")
    print (67 * "-")

def sessions_into_json():
    global i
    i==1
    while bool(client.website.list_conversations(website_id,i)):
    
        current_batch_of_conversations=client.website.list_conversations(website_id,i)
        print(i)
        #bypass API limit
        sleep(uniform(1,3))
        conversation_data += current_batch_of_conversations
        i+=1
print('Out of the loop')
json.dump(conversation_data, open('conversations.json','w'), indent=4)

def load_json():
    conversation_data=[]
    conversation_data=json.load(open('conversations.json','r'))

def filter_data_import_csv():
    outputFile=open('sessions.csv','w',newline='', encoding='utf-8')
    outputWriter=csv.writer(outputFile)
    outputWriter.writerow(['SESSION ID:', 'CREATED AT:', 'UPDATED AT:', 'SEGMENTS', 'COUNTRY:'])
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
    outputFile.close()
                  
loop=True

while loop:
    print_menu()
    choice=input()

    if choice=="1":
        print ("1st option has been selected :  ALL Session IDs -> 1 JSON file")
        sessions_into_json()
    elif choice=="2":
        print("2nd option has been selected : LOAD conversations.json -> filter -> CSV")
        load_json()
        filter_data_import_csv()
    elif choice=="3":
        print("3rd option has been selected : all of the above at once")
        sessions_into_json()
        load_json()
        filter_data_import_csv()                        
    elif choice=="4":
        print("4th option has been selected : Exit")
        loop=False
    else:
        print("Wrong option has been selected. Press any key to try again...")
            
                          



