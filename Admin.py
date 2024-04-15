from Doctor import Doctor


class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        return self.__username in username and self.__password == password
        #ToDo1
        pass

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        first_name = input("Enter the first name: ")
        surname = input("Enter the surname: ")
        speciality = input("Enter the speciality: ")

        return first_name, surname, speciality
        pass

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        op = input("Input: ")
        #ToDo3 op input = input
        pass


        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            
            first_name, surname, speciality = self.get_doctor_details()
            #ToDo4 ^ the line above
            pass

            # check if the name is already registered
            
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    name_exists = True
                    pass # save time and end the loop

            if name_exists == False:
                doctors.append(Doctor(first_name,surname,speciality))
            
            #ToDo6
            
            # add the doctor ...
           

                                                         # ... to the list of doctors
            print('Doctor registered. ')

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            #ToDo7
            print('ID |          Full name           |  Speciality')
            self.view(doctors)
            pass

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    
                    if doctor_index!=False:
                
                        break
                        
                    else:
                        print("Doctor not found")

                    
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = int(input('Input: ')) # make the user input lowercase

            if op == 1:
                firstname = input("What is the new first name?")
                #Doctor.set_first_name(self,firstname)
    
                doctors[index].set_first_name(firstname)
                print(f"Firstname was updated to {firstname}")
                
            elif op == 2:
                surname = input("What is the new surname?")
                doctors[index].set_surname(surname)
                print(f"Surname was updated to {surname}")

            elif op == 3:
                speciality = input("What is the new speciality?")
                doctors[index].set_speciality(speciality)

            else:
                print("Invalid input")
                op = int(input('Input: '))


            #ToDo8
            pass

        # Delete
        elif op == '4':
            
            
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)
            doctor_index = input('Please enter the doctor ID: ')
            
            try:
                doctor_index = int(doctor_index) -1
                
                if self.find_index(doctor_index,doctors)!=False:     
                  
                
                    #doctors.pop(doctors[doctor_index])
                    doctors.pop(doctor_index)
                    print("Doctor Deleted")
                    
                        
                else:
                    print("Doctor not found")

                    
                        # doctor_index is the ID mines one (-1)
                        

            except ValueError: # the entered id could not be changed into an int
                print('The ID entered is incorrect')

            
    


    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |     Symptoms     ')
        self.view(patients)
        pass

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |     Symptoms     ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                #patients[patient_index].link(doctors[doctor_index])
                patients[patient_index].link(doctors[doctor_index].full_name())
                #doctors[index].set_first_name(firstname)
                
                pass
                
                print('The patient is now assign to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def discharge(self, patients, discharge_patients): #check if discharged or discharge
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        #print("-----Discharge Patient-----")

        #patient_index = input('Please enter the patient ID: ')
        
        while True:
            print("-----Discharge Patient-----")
            print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |     Symptoms     ')
            self.view(patients)
            patient_index = input('Enter the ID of the patient to be discharged: ')
            try:
                patient_index = int(patient_index) -1
                if self.find_index(patient_index,patients)!=False:   

                    discharge_patients.append(patients[patient_index])
                    patients.pop(patient_index)
                    print("Patient Discharged")


                    break
                        
                else:
                    print("Patient not found")

                    
                    # doctor_index is the ID mines one (-1)
                        

            except ValueError: # the entered id could not be changed into an int
                print('The ID entered is incorrect')

   
        

        #ToDo12
        pass



    

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |     Symptoms     ')
        self.view(discharged_patients)
        #ToDo13
        pass

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            print("The current username is ", self.__username)
            username = input("Enter the new username")
            self.__username = username
            print(f"Username updated to {self.__username} ")
            pass

        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__password = password

        elif op == 3:
            #ToDo15
            print("The current address is ", self.__address)
            address = input("Enter the new address ")
            self.__address = address
            print(f"Address was updated to {self.__address} ")
            pass

        else:
            #ToDo16
            print("Invalid input")
            pass


    def update_symptoms(self, patients):
            """
            Allow the admin to assign symptoms to a patient
            Args:
                patients (list<Patients>): the list of all the active patients
                doctors (list<Doctor>): the list of all the doctors
            """
           

            print("-----Select Patients-----")
            print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |     Symptoms     ')
            self.view(patients)

            patient_index = input('Please enter the patient ID: ')

            try:
                # patient_index is the patient ID mines one (-1)
                patient_index = int(patient_index) -1

                # check if the id is not in the list of patients
                if patient_index not in range(len(patients)):
                    print('The id entered was not found.')
                    return # stop the procedures

            except ValueError: # the entered id could not be changed into an int
                print('The id entered is incorrect')
                return # stop the procedures

            print("-----Symptom Select-----")
            newsymptoms = input("What are the new symptoms? ")
            patients[patient_index].set_symptoms(newsymptoms)
            patients[patient_index].print_symptoms() # print the patient symptoms


        
######################
    def swap_patients_doctor(self, patients, doctors):
        """
        Allow the admin to swap the doctor of a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |     Symptoms     ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')
        """

      #  try:
            # patient_index is the patient ID mines one (-1)
            #patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            #if patient_index not in range(len(patients)):
            #    print('The id entered was not found.')
             #   return # stop the procedures

     #   except ValueError: # the entered id could not be changed into an int
      #      print('The id entered is incorrect')
      #      return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor to transfer to')
       # patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                #patients[patient_index].link(doctors[doctor_index])
                for patient in patients:
                        patient.link(doctors[doctor_index].full_name())
                #doctors[index].set_first_name(firstname)
                
                
                pass
                
                print('The patients are now assigned to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')

    def group_by_family(self, patients):
        family_groups = {}
        for patient in patients:
            if patient.surname() in family_groups:
                family_groups[patient.surname()].append(patient)
            else:
                family_groups[patient.surname()] = [patient]
        

        for family_name, family_members in family_groups.items():
             print(f"Family name: {family_name}")
             print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |     Symptoms     ')
             self.view(family_members)
                
             print("\n")
        