def patient_catogeroy(dob_input):

    from datetime import datetime

    current_time = datetime.now()

    current_date= current_time.date()

    date_of_birth = datetime.strptime(dob_input, "%d-%m-%Y")

    birth= date_of_birth.date()

    difference = current_date - birth

    years = difference.days / 365

    print("Age in years (float):", years)

    if(years<14):
        print("The patient is a Child")

    elif(years>=14 and years<=20):
        print("The patient is a teenager")

    elif(years>20 and years<60):
        print("The patient is a adult")

    elif(years>+60):
        print("The patient is senior")

dob_input = input("Enter your date of birth (DD-MM-YYYY): ")  
patient_catogeroy(dob_input)
