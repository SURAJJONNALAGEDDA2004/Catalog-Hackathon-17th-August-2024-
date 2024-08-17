import csv
import os
if not os.path.exists('reports.csv'):
    with open('reports.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Patient ID", "Patient Name", "Diagnosis", "Date"])

def add(patient_id, patient_name, diagnosis, date):
    with open('reports.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([patient_id, patient_name, diagnosis, date])
    print(f"Report appended for the patient name {patient_name}.")

def checkreports(patient_id):
    with open('reports.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        temp= False
        for row in reader:
            if row[0] == patient_id:
                temp = True
                print(f"Patient ID: {row[0]}, Name: {row[1]}, Diagnosis: {row[2]}, Date: {row[3]}")
        if not temp:
            print(f"No reports found for Patient ID: {patient_id}")

def main():
    while True:
        print("\nThis is an automatic health monitoring system")
        print("Press 1 to 'Add a new report'")
        print("Press 2 to 'Check already added reports'")
        print("Press 3 to 'Exit'")
        choice = input("Please enter your choice: ")

        if choice == '1':
            patient_id = input("Enter the Patient Id: ")
            patient_name = input("Enter the Patient name: ")
            diagnosis = input("Enter Diagnosis: ")
            date = input("Enter Date: ")
            add(patient_id, patient_name, diagnosis, date)
        
        elif choice == '2':
            patient_id = input("Enter Patient Id whose reports you want to check: ")
            checkreports(patient_id)

        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("No Given choice found.Please enter again")

if __name__ == "__main__":
    main()
