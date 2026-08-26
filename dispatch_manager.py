def add_to_dispatch_queue(
    job_number,
    customer_name,
    city,
    service,
    priority,
     preferred_day,
    preferred_time,
    technician,
):
  
  with open("dispatch_queue.txt", "a") as file:
        file.write(f"Job Number: {job_number}\n")
        file.write(f"Customer: {customer_name}\n")
        file.write(f"City: {city}\n")
        file.write(f"Service: {service}\n")
        file.write(f"Priority: {priority}\n")
        file.write(f"Preferred Day: {preferred_day}\n")
        file.write(f"Preferred Time: {preferred_time}\n")

        file.write(f"Technician: {technician}\n")
        file.write("----------------------------------------\n")  

def assign_technician(service):


    if service == "Leak Repair":
        return "Mike"

    if service == "Water Heater Service":
        return "Sarah"

    if service == "Water Supply Service":
        return "Carlos"

    if service == "Toilet Service":
        return "David"

    if service == "Garbage Disposal Service":
        return "David"

    if service == "Sewer Service":
        return "Carlos"

    if service == "Drain Cleaning":
        return "David"

    return "General Technician"

def estimate_arrival(priority):

    if priority == "Critical":
        return "30 Minutes"

    if priority == "High":
        return "1 Hour"

    return "Next Available" 

def technician_available(technician):

    unavailable_technicians = [
        "Mike",
    ]

    if technician in unavailable_technicians:
        return False

    return True 

def assign_available_technician(service):

    technician = assign_technician(service)

    if technician_available(technician):
        return technician

    if service == "Leak Repair":
        return "David"

    if service == "Water Heater Service":
        return "Carlos"

    if service == "Water Supply Service":
        return "Sarah"

    if service == "Toilet Service":
        return "Mike"

    if service == "Garbage Disposal Service":
        return "Sarah"

    if service == "Sewer Service":
        return "Sarah"

    if service == "Drain Cleaning":
        return "Carlos"

    return "General Technician"  

       