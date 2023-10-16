#what should this bot do
#it should generate a dataset of n rows of data for malaria patients
#columns(symptoms): id, fever, gender, cold, sweating, headache,severity,muscle pain,nausea, vomiting.
#dtypes: id-nominal(int), symptoms-boolean(0-false|1-True)gender-category(male|female),severity-category(Nil|Mild|Severe).

import random
import pandas as pd

def NRows():
    nrows = int(input("enter number of rows: "))
    return nrows

def id(nrows):
    ID = []
    for x in range(nrows):
        ID.append(x + 1)
    return ID

def gender(nrows):
    Genders = ['male', 'female']
    Gender = []
    for items in range(nrows):
        Gender.append(random.choice(Genders))
    return Gender

'''def fever(nrows):
    diag = ['Yes', 'No']
    status = []
    for items in range(nrows):
        status.append(random.choice(diag))
    return status
'''
    
def symptom(nrows):
    diag = ['Yes', 'No']
    Symptoms = ['fever', 'cold', 'sweating', 'headache', 'muscle pain', 'nausea', 'vomiting']
    symptom_data = {}

    for symptom_name in Symptoms:
        symptom_status = []
        for i in range(nrows):
            symptom_status.append(random.choice(diag))
        symptom_data[symptom_name] = symptom_status

    return symptom_data

'''def severity(nrows,symptom_data):
    for k,v in symptom_data.items()
        if k'''
    

    



nrows = NRows()
ids = id(nrows)
genders = gender(nrows)
#fever_statuses = fever(nrows)
symptom_data = symptom(nrows)

malaria={'id':ids,'Gender':genders}
malaria.update(symptom_data)

malaria_df = pd.DataFrame(malaria)
malaria_df.to_csv('malaria_df.csv', index=False)
#print(ids)
#print(genders)
#print(fever_statuses)
#for symptom_name, status_list in symptom_data.items():
    #print(f"{symptom_name}: {status_list}")
            
    