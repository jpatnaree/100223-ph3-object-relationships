# CAR - GARAGE RELATIONSHIP ###


# CAR ###
class Car:

    all_cars = []
    
    def __init__(self, make, model, license_plate, garage):
        self.make = make
        self.model = model
        self.license_plate = license_plate
        self.garage = garage
        Car.all_cars.append(self)

    def __repr__(self):
        return f"Car(make={self.make}, model={self.model}, license_plate={self.license_plate})"

# Car belongs to Garage => Car has to be in a Garage, Garage can store many Cars

# GARAGE ###
class Garage:
    
    def __init__(self, address):
        self.address = address

    def __repr__(self):
        return f"Garage(address={self.address})"
    
    def filter_car(self, car):
        return car.garage == self

    def my_car(self):
        return list(filter(self.filter_car, Car.all_cars))
        #return [car for car in Car.all_cars if car.garage == self] # filter through all garage to find car
    
my_garage = Garage("Main Street")
free_park = Garage("Free Park")
pontiac = Car("Pontiac", "Sedan", "123", free_park)
batmobile = Car("Wayney Vroom Vroom", "Batmobile", "JUSTICE", my_garage)
ferrari = Car("Ferrari", "Sport", "VinDee", my_garage)
##############################

# DOCTOR - PATIENT RELATIONSHIP ###

# DOCTOR ###
class Doctor:

    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

    def __repr__(self):
        return f"Doctor(name={self.name}, specialty={self.specialty})"

    def appointments(self):
        return [appt for appt in Appointment.all_appointments if appt.doctor == self]
    
    def patient(self):
        all_patients = [appt.patient for appt in Appointment.all_appointments if appt.doctor == self]

        unique_patients = list(set(all_patients))

        return unique_patients

# PATIENT ###
class Patient:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"Patient(first_name={self.first_name}, last_name={self.last_name})"
    
    def appointments(self):
        return [appt for appt in Appointment.all_appointments if appt.patient == self]
    
    def doctor(self):
        all_doctors = [appt.doctor for appt in Appointment.all_appointments if appt.patient == self]

        unique_doctors = list(set(all_doctors))

        return unique_doctors

#APPOINTMENT

class Appointment:

    all_appointments = []
    
    def __init__(self, date, doctor, patient):
        self.date = date
        self.doctor = doctor
        self.patient = patient
        Appointment.all_appointments.append(self)

    def __repr__(self):
        return f"Appointment(date={self.date}, doctor={self.doctor.name}, patient_name={self.patient.first_name} {self.patient.last_name})"
    
p1 = Patient("John", "Smith")
p2 = Patient("Jane", "Doe")
d1 = Doctor("Oz", "Cardiology")
d2 = Doctor("Phil", "Neurology")
a1 = Appointment("Nov 1", d1, p1)
a2 = Appointment("Nov 2", d2, p2)
a3 = Appointment("Nov 3", d1, p2)
a4 = Appointment("Nov 4", d2, p1)
##############################
    


# STUDENT - INSTRUCTOR - COURSE - ASSIGNMENT - SCHOOL RELATIONSHIP ###

# STUDENT ###
class Student:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Student(name={self.name})"
    
# INSTRUCTOR ###
class Instructor:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Instructor(name={self.name})"
    
# COURSE ###
class Course:

    def __init__(self, subject, start_date):
        self.subject = subject

    def __repr__(self):
        return f"Course(subject={self.subject})"

# ASSIGNMENT ###
class Assignment:

    def __init__(self, title, grade):
        self.title = title
        self.grade = grade

    def __repr__(self):
        return f"Assignment(title={self.title}, grade={self.grade})"

# SCHOOL ###
class School:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"School(name={self.name})"
    
##############################

