import pandas as pd
import os
import json

#Keys with useful data that we want pulled out of our dataset
KEYS_TO_USE= ['id', 'all_artists', 'title', 'medium', 'dateText', 'acquisitionYear', 'height', 'width', 'units']

#===================================================================
#get_record() function: Processes single JSON file and returns a tuple containing specific fields
#===================================================================
def get_record(file_path, keys_to_use):

#Opens file path and loads file into JSON module
    with open(file_path) as artwork_file:
        content = json.load(artwork_file)
    
    #Defines list to be returned
    record = []

    #Appends data that aligns with defined keys to record list.
    for field in keys_to_use:
        record.append(content[field])

    #Returns record
    return tuple(record)

#Tests
# test_path = os.path.join('data sets', 'artworks', 'a', '000', 'a00001-1035.json')
# test_record= get_record(test_path, KEYS_TO_USE)


#========================================================================================
#read_artworks_from_json() function: Iterates through  JSON files in artworks folder and runs get_record() function on them
#========================================================================================
def read_artworks_from_json(keys_to_use):

    #Path to dataset
    JSON_ROOT = os.path.join('data sets', 'artworks')

    #Define list to pass into dataframe
    artworks = []

    #Iterates through artworks folder and: 
        # Verifys each file is a .json file, extracts records with keys matching the defined keys using get_record() function, adds records to artworks list.
    for root, _, files in os.walk(JSON_ROOT): 
        for f in files:
            if f.endswith('json'):
                record = get_record(os.path.join(root, f), keys_to_use)
                artworks.append(record)
            break

    #Creates and returns dataframe from artworks list and defined keys 
    df = pd.DataFrame.from_records(artworks, columns=keys_to_use, index='id')
    return df

#Constructs the dataframe by funning the function and inputting the defined Keys
df = read_artworks_from_json(KEYS_TO_USE)