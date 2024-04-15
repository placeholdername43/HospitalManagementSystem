class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode,doctor,symptoms):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """
        self.__first_name = first_name
        self.__surname = surname
        #self.__age = age
        self.__age = int(age)
        self.__mobile = mobile
        self.__postcode = postcode
        self.__doctor = doctor
        self.__symptoms = symptoms

        
        #ToDo1
        
        pass
        
       
    def first_name(self):
        return self.__first_name

    def surname(self):
        return self.__surname

    def age(self):
        return self.__age

    def mobile(self):
        return self.__mobile

    def postcode(self):
        return self.__postcode

    def symptoms(self):
        return self.__symptoms

    def doctor(self):
        return self.__doctor

    def set_symptoms(self, newsymptoms):
        self.__symptoms = newsymptoms
        return self.__symptoms
        
        
    
    def full_name(self) :
        """full name is first_name and surname"""


        #ToDo2
        return f"{self.__first_name} {self.__surname}"
        pass


    def get_doctor(self) :
        return f"{self.__doctor}"
        
        #ToDo3
        pass

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def print_symptoms(self):
        """prints all the symptoms"""
        print(self.__symptoms, "was added as a symptom")
        
        #ToDo4
        pass



    def __str__(self):
        return f'{self.full_name():^30}|{self.get_doctor():^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}|{self.__symptoms:^20}'
