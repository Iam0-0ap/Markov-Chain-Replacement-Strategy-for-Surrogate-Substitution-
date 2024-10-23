import os
import random
import pandas as pd
from faker import Faker
from datetime import timedelta
from dataclasses import dataclass
fake = Faker()


random.seed(100)
Faker.seed(100)


@dataclass
class ClinicalNote:
    record_int : int
    patient_name : str
    dob: str
    admission_date : str
    discharge_date : str
    address: str
    phone_number: str
    mrn: str
    diagnosis: str
    treatment: str
    symptom: str
    clinical_note: str = ""



#Function to format the clinical notes

def format_clinical_note(note: ClinicalNote) -> str:
    choice = random.choice([1, 2, 3])
    if choice == 1:
        return(
            f"Patient {note.patient_name} (MRN: {note.mrn}) presented with {note.symptom} on {note.admission_date}. "
            f"Patient lives at {note.address}, and can be contacted at {note.phone_number}. "
            f"Patient was diagnosed with {note.diagnosis}. "
            f"Discharged on {note.discharge_date} with a prescription for {note.treatment}. "
        )
    elif choice == 2:
        return(
            f"{note.patient_name}, born {note.dob}, was admitted on {note.admission_date} with complaints of {note.symptom}. "
            f"After evaluation, the diagnosis was {note.diagnosis}. "
            f"Patient resides at {note.address} phone: {note.phone_number}. "
            f"Discharge planned for {note.discharge_date}. Recommended treatment: {note.treatment}."
        )
    else:
        return(
            f"On {note.admission_date}, {note.patient_name} (DOB: {note.dob}, MRN: {note.mrn}) came in for {note.symptom}. "
            f"The patient was diagnosed with {note.diagnosis}. "
            f"Currently living at {note.address}. Discharged on {note.discharge_date} with "
            f"instructions to follow-up and take {note.treatment}."
        )



#Main function to generate synthetic clinical note
def generate_clinical_note(record_id: int) -> ClinicalNote:
    patient_name = fake.name()

    # lamnda function to mask random dates
    mask_date = lambda date: date if random.random() > 0.5 else "YYYY-MM-DD"

    dob = fake.date_of_birth(minimum_age= 18, maximum_age= 90)
    admission_date = fake.date_this_decade()
    discharge_date = (admission_date + timedelta(days=random.randint(1, 10))).strftime("%Y-%m-%d")

    #Masking random dates 
    masked_dob = mask_date(dob)
    masked_admission_date = mask_date(admission_date)
    masked_discharge_date = mask_date(discharge_date)

    address = f"XXXXX Street, {fake.state()}, {fake.zipcode()}"
    phone_number = '+977-XXX-XXXX-XXX'
    mrn = str(fake.unique.random_number(digits = 2)) + '-XXXXXX'
 
    diagnosis = random.choice([
        "acute gastritis", "fall injury", "indigestion", "food poisoning", 
        "myocardial infarction", "cholelithiasis", "acute bronchitis", 
        "angina pectoris", "anemia", "hemorrhoid", "urinary tract infection"
    ])
    
    treatment = random.choice([
        "bed rest", "plenty of water", "oxygen therapy", "dietary modification", 
        "light exercise", "ambulation", "nebulization", "steam inhalation", 
        "proton pump inhibitor", "antibiotics", "corticosteroids"
    ])
    
    symptom = random.choice([
    "nausea/vomiting", "loose stool", "abdominal pain", "headache", 
    "palpitation", "shortness of breath", "skin rashes", "dizziness", 
    "drowsiness", "chest pain", "fever"
    ])

    clinical_note = ClinicalNote(
        record_int= record_id, 
        patient_name= patient_name,
        dob= masked_dob, 
        admission_date= masked_admission_date, 
        discharge_date= masked_discharge_date, 
        address= address, 
        phone_number= phone_number, 
        mrn= mrn, 
        diagnosis= diagnosis, 
        treatment= treatment,
        symptom= symptom
    )

    clinical_note.clinical_note = format_clinical_note(clinical_note)
    return clinical_note


record = [generate_clinical_note(i+1) for i in range(100)]

df = pd.DataFrame([{'Clinical_Note': note.clinical_note} for note in record])

output_path = "clinical_notes_dataset.csv"
df.to_csv(output_path, index= False)
print(f"Saved the csv to path : {output_path}")
