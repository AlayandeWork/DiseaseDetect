import pandas as pd
import random

def NRows():
    nrows = int(input("Enter The Number of Rows: "))
    return nrows

def id(nrows):
    ID = []
    for x in range(nrows):
        ID.append(x + 1)
    return ID

def gender(nrows):
    Genders = ["Male", "Female"]
    Gender = []
    for items in range(nrows):
        Gender.append(random.choice(Genders))
    return Gender

def symptom(nrows):
    multiple_diag = ["Yes", "No"]
    Symptoms = ["Akinesia", "Tremors", "Postural Instability", "Rigidity", "Cognitive Challenge", "Insomnia", "Constipation"]
    symptom_data = {}

    for symptoms_name in Symptoms:
        symptom_status = []
        for i in range(nrows):
            symptom_status.append(random.choice(multiple_diag))
        symptom_data[symptoms_name] = symptom_status
    return symptom_data

def calculate_severity(row):
    yes_count = row[row == "Yes"].count()
    if yes_count == 1:
        return "Negative"
    elif yes_count == 2:
        return "Low"
    elif yes_count == 3:
        return "Medium"
    elif yes_count >= 4 and yes_count <= 5:
        return "High"
    elif yes_count >= 6:
        return "Critical"
    else:
        return "Negative"


nrows = NRows()
ids = id(nrows)
genders = gender(nrows)
symptom_data = symptom(nrows)

Parkinson = {'id': ids, 'Gender': genders}
Parkinson.update(symptom_data)

Parkinson_df = pd.DataFrame(Parkinson)

# Calculate the Severity column based on symptom_data
Parkinson_df['Severity'] = Parkinson_df.iloc[:, 2:].apply(calculate_severity, axis=1)

Parkinson_df.to_csv('Parkinson_Data.csv', index=False)
