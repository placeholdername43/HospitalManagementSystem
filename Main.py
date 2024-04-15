# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient
import csv

def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    #patients = [Patient('Sara','Smith', 20, '07012345678','B1 234'), Patient('Mike','Jones', 37,'07555551234','L2 2AB'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC')]
    discharged_patients = []
    
   
    #current_directory = os.getcwd()
    #file_path = os.path.join(current_directory, 'file.csv')

    def read_patients_from_csv():
        patients = []
        with open('test.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                name, surname, age, mobile, postcode, doctor, symptoms = row
                patients.append(Patient(name, surname, int(age), mobile, postcode, doctor, symptoms))
        return patients


    patients = read_patients_from_csv()


    """ READ ME 
    
    # PLEASE SPECIFY CSV PATH ON YOUR MACHINE IF THE ABOVE CODE DOES NOT WORK FOR YOU 
    

    def read_patients_from_csv(filepath):
        patients = []
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                name, surname, age, mobile, postcode, doctor, symptoms = row
                patients.append(Patient(name, surname, int(age), mobile, postcode, doctor, symptoms))
        return patients


    patients = read_patients_from_csv(r"FILE PATH HERE") # <---------- PLEASE PASTE THE FILEPATH TO test.csv HERE AND AT THE BOTTOM OF THE PROGRAM IN the write_patients_to_csv FUNCTION

    # Thank you
    
    """
    

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin detais')
        print(' 6- View patient')
        print(' 7- Update patient symptoms')
        print(' 8- Swap all patients to a doctor')
        print(' 9- View patients by family')
        print('10- Quit')


        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
            admin.doctor_management(doctors)
            pass
         
         #ToDo1
          

        elif op == '2':
            # 2- View or discharge patients
            #ToDo2
            pass

            while True:
                op = input('Do you want to discharge a patient(Y/N):').lower()

                if op == 'yes' or op == 'y':
                    admin.discharge(patients,discharged_patients)
                    pass

                elif op == 'no' or op == 'n':
                    break

                # unexpected entry
                else:
                    print('Please answer by yes or no.')
        
        elif op == '3':
            # 3 - view discharged patients
            admin.view_discharge(discharged_patients)
            pass

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '5':
            # 5- Update admin detais
            admin.update_details()

        elif op == '6':
            # show all active patients - test option
            admin.view_patient(patients)

        elif op == '7':
            #  update patient symptoms
            admin.update_symptoms(patients)

        elif op == '8':
            admin.swap_patients_doctor(patients,doctors)

        elif op == '9':
            admin.group_by_family(patients)

        elif op == '10':
            # 10 - quit
            break

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

        def write_patients_to_csv(patients):
            with open("test.csv", 'w', newline='') as f:
                writer = csv.writer(f)
                for patient in patients:
                    writer.writerow([patient.first_name(),patient.surname(),patient.age(),patient.mobile(),patient.postcode(),patient.doctor(),patient.symptoms()])    

        write_patients_to_csv(patients)

    """# READ ME 
    
    # PLEASE SPECIFY CSV PATH ON YOUR MACHINE IF THE ABOVE CODE DOES NOT WORK FOR YOU 
    

        def write_patients_to_csv(patients, filepath):
            with open(filepath, 'w', newline='') as f:
                writer = csv.writer(f)
                for patient in patients:
                    writer.writerow([patient.first_name(),patient.surname(),patient.age(),patient.mobile(),patient.postcode(),patient.doctor(),patient.symptoms()])    

        write_patients_to_csv(patients, r'FILE PATH HERE') # <---------- PLEASE PASTE THE FILEPATH TO test.csv HERE AND AT THE BOTTOM OF THE PROGRAM IN the write_patients_to_csv FUNCTION
    


     

    # Thank you
    
    """

if __name__ == '__main__':
    main()
