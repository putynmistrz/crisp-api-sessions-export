# crisp-api-sessions-export
A tool for the python API CRISP wrapper, that downloads all sessions IDs, merges them into 1 big JSON and exports important data to .csv

# What is CRISP?

Crisp is a Service Desk tool. Read more here:
https://crisp.chat/en/

It is a pretty good tool with a complex API, but it was lacking in some reporting/analitical functionality. That's why I have created this simple python app.

# How is session data stored in CRISP?

Session data is paginated. Other than using this app, it is really difficult to gather all of the pages and merge them into 1 file.

# How does this app work?

The main application code is in the "Gather Session IDs to CSV.py" file. It works like this:

1. Authorizes you to the CRISP API using data found in the "crisp_info.py" file.
2. Sets the output files as the "session.csv" and "conversations.json", both included in the repo
3. Uses the CRISP API method - Crisp.website.list_conversations(website_id, page_number) to loop until it reaches the last page.
4. Dumps the session data into 1 big JSON file, for archival purposes.
5. Goes through the list of all of the session data and picks out important information. This can be customized, as presented below.
6. Stores that data as a CSV, with every row of data seperated.

# How to customize the data stored in the CSV file?

JSON dump, from the 4. step explained above, contains all of the data. From there, in the "for i in conversation_data" loop you can easily add your own variables like this:
"additional_variable = str(i['parent_key']['child_key'])" where keys are derviced from the JSON structure.

Remember to also add the new variables as an additional argument in the "outputWriter.writerow" method.
