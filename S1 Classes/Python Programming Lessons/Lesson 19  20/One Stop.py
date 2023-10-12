########################################################################
#Program Description: Keep track of policy information.
#Written by: Austin Reid
#Date written 6/5/2023
########################################################################

import datetime
import re
allowed_letters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
allowed_numbers = set("0123456789-")

while True:

    while True:
        policyDate = input("Enter the policy date (YYYY-MM-DD): ")

        if policyDate == "":
            print("Invalid policy date must be in the format of YYYY-MM-DD.")
        else:
            break
        
        

    customerFirst = input("What is the name of the customer?: ").title()
    customerLast = input("What is the last name of the customer?: ").title()
    streetAdd = input("What is the street address?: ").capitalize()
    currCity = input("What is the city of the customer?: ").capitalize()
    

    while True:

        postalCode = input("What is the postal code of the customer? (A01A01): ").upper()
        if postalCode == "":
            print("Error - Please enter postal code.").upper()
        elif len(postalCode) != 6:
            print("Error - Postal code can only be 6 characters.")
        elif not set(postalCode[0::2]).issubset(allowed_letters):
            print("Error - 1ST, 3RD and 5TH characters must be letters.")
        elif not set(postalCode[1::2]).issubset(allowed_numbers):
            print("Error - 2ND, 4TH and 6TH characters must be digits.")
        else:
            break

    while True:

        provinces = ["NL","LB","AB","BC","ON","MB","NB","NS","NT","NU","PE","QC","SK","YT"]
        custProv = input("What is the province of the customer? (XX): ").upper()
    
        if custProv not in provinces:
            print("Invalid Province, please provide the initials for your province.")
        else:
            break

    while True:

        homePhone = input("What is the home phone number? (1(XXX)-XXX-XXXX): ")
        workPhone = input("What is the work phone number? (1(XXX)-XXX-XXX):  ")
        cellPhone = input("What is the cell phone number? (1(XXX)-XXX-XXX):  ")


        if homePhone and workPhone and cellPhone == "":
            print("Error - Type in a valid phone number.")
        elif not set(homePhone).issubset(allowed_numbers) and not set(workPhone).issubset(allowed_numbers) and not set(cellPhone):
            print("Error - Invalid characters for phone numbers.")
        


        def format_home_phone(homePhone):
            homeDigits = re.sub(r'\D','', homePhone)
    
            homePhoneFormat = re.sub(r'^(\d{1})(\d{3})(\d{3})(\d{4})$', r'+\1 (\2) \3-\4', homeDigits)
            return homePhoneFormat

        formatted_Home = format_home_phone(homePhone)
    

        def format_home_phone(workPhone):
            workDigits = re.sub(r'\D','', workPhone)
    
            workPhoneFormat = re.sub(r'^(\d{1})(\d{3})(\d{3})(\d{4})$', r'+\1 (\2) \3-\4', workDigits)
            return workPhoneFormat

        formatted_Work = format_home_phone(workPhone)
    

        def format_home_phone(cellPhone):
            cellDigits = re.sub(r'\D','', cellPhone)
    
            cellPhoneFormat = re.sub(r'^(\d{1})(\d{3})(\d{3})(\d{4})$', r'+\1 (\2) \3-\4', cellDigits)
            return cellPhoneFormat

        formatted_Cell = format_home_phone(cellPhone)
        break

    while True:

        policy = input("Is this a New policy or a Renewal? (N/R): ")

        if policy == "":
            print("Error" )
print(policyDate, customerFirst, customerLast,streetAdd, currCity, custProv, postalCode)
print("Home: ", formatted_Home, formatted_Work, formatted_Cell)