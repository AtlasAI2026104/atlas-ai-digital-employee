def collect_customer_name():
    customer_name = input("What is your name? ")
    return customer_name


def collect_phone_number():
    phone_number = input("What is your phone number? ")
    return phone_number


def collect_address():
    address = input("What is your street address? ")
    return address


def collect_city():
    city = input("What city are you located in? ")
    return city

def collect_preferred_day():
    preferred_day = input("What day would you prefer for service? ")
    return preferred_day


def collect_preferred_time():
    preferred_time = input("What time would you prefer? ")
    return preferred_time


def collect_problem_description(customer_name):
    problem_description = input(
        f"Thank you, {customer_name}. How can I help you today? "
    )
    return problem_description

def collect_emergency_status():
    emergency = input("Is this an emergency? (yes/no): ")
    return emergency

def respond_to_emergency(emergency):
    if emergency.lower() == "yes":
        print()
        print("Emergency request received.")
        print("We will prioritize your request and contact you as soon as possible.")
    else:
        print()
        print("Thank you.")
        print("We will schedule the next available appointment.")

def detect_emergency(problem_description):
    emergency_keywords = [
        "burst",
        "flood",
        "flooding",
        "overflow",
        "gas leak",
        "no water",
        "sewer",
        "sewage",
        "fire",
        "smell gas",
        "pipe broke",
        "broken pipe",
        "water pouring",
        "water is pouring"
        "backing up",
        "dirty water",
    ]        

    problem = problem_description.lower()

    for keyword in emergency_keywords:
        if keyword in problem:
            return "yes"

    return "no"

def detect_service(problem_description):
    problem = problem_description.lower()

    if "no water" in problem:
        return "Water Supply Service"

    if "backing up" in problem and (
    "toilet" in problem
    or "bathtub" in problem
    or "dirty water" in problem
):
        return "Sewer Service"

    if "water heater" in problem:
        return "Water Heater Service"

    if "toilet" in problem:
        return "Toilet Service"

    if "garbage disposal" in problem:
        return "Garbage Disposal Service"

    if "sewer" in problem or "sewage" in problem:
        return "Sewer Service"

    if "drain" in problem or "clog" in problem:
        return "Drain Cleaning"

    if (
       "leak" in problem
        or "burst" in problem
        or "pipe broke" in problem
        or "broken pipe" in problem
        or "water pouring" in problem
        or "water is pouring" in problem
):
        
        return "Leak Repair" 

    return "General Plumbing Service"      

def determine_priority(emergency, service):

    if emergency == "yes":
        return "Critical"

    if service == "Sewer Service":
        return "High"

    if service == "Water Heater Service":
        return "High"

    if service == "Toilet Service":
        return "Normal"

    return "Normal"

def save_customer_record(
    job_number,
    customer_name,
    phone_number,
    address,
    city,
    problem_description,
    service,
    emergency,
    preferred_day,
    preferred_time,
    priority,
):
    with open("customer_records.txt", "a") as file:
        file.write(f"Job Number: {job_number}\n")
        file.write(f"Name: {customer_name}\n")
        file.write(f"Phone: {phone_number}\n")
        file.write(f"Address: {address}\n")
        file.write(f"City: {city}\n")
        file.write(f"Problem: {problem_description}\n")
        file.write(f"Service: {service}\n")
        file.write(f"Emergency: {emergency}\n")
        file.write(f"Preferred Day: {preferred_day}\n")
        file.write(f"Preferred Time: {preferred_time}\n")
        file.write(f"Priority: {priority}\n")
        file.write("----------------------------------------\n")


def returning_customer(phone_number):
    with open("customer_records.txt", "r") as file:
        records = file.read()

    if phone_number in records:
        return True

    return False
def get_customer_history(phone_number):
    with open("customer_records.txt", "r") as file:
        records = file.read()

    phone_search = "Phone: " + phone_number

    if phone_search not in records:
        return None

    record_start = records.rfind(
        "Job Number:", 0, records.find(phone_search)
    )

    record_end = records.find(
        "----------------------------------------",
        record_start,
    )

    return records[record_start:record_end]

def safety_response(problem_description):
    problem = problem_description.lower()
    print("SAFETY CHECK:", problem)

    if "gas leak" in problem or "smell gas" in problem:
        print()
        print("SAFETY ALERT:")
        print("Leave the area immediately and avoid using switches, flames, or electrical devices.")
        print("Call your gas utility or emergency services from a safe location.")
        return True

    return False


    

                   





