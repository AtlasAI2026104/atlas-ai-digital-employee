"""
Atlas AI Digital Employee
Version: 1.1
Founder: Beatriz
Company: Atlas AI Technologies
"""

from customer_manager import (
    collect_customer_name,
    collect_phone_number,
    collect_address,
    collect_city,
    collect_preferred_day,
    collect_preferred_time,
    collect_problem_description,
    collect_emergency_status,
    respond_to_emergency,
    detect_emergency,
    detect_service,
    determine_priority,
    save_customer_record,
    returning_customer,
    get_customer_history,
    
)


from display import display_startup
from job_manager import generate_job_number
from dispatch_manager import (
    add_to_dispatch_queue,
    assign_technician,  assign_available_technician,
    estimate_arrival,
)


display_startup()

job_number = generate_job_number()

customer_name = collect_customer_name()

phone_number = collect_phone_number()
if returning_customer(phone_number):
    print()
    print("Welcome back! We found your previous customer records.")
    print()

    history = get_customer_history(phone_number)

    if history:
        print(history)
address = collect_address()
city = collect_city()
preferred_day = collect_preferred_day()
preferred_time = collect_preferred_time()
problem_description = collect_problem_description(customer_name)

if "gas leak" in problem_description.lower() or "smell gas" in problem_description.lower():
    print()
    print("SAFETY ALERT:")
    print("Leave the area immediately and avoid using switches, flames, or electrical devices.")
    print("Call your gas utility or emergency services from a safe location.")

# emergency = collect_emergency_status()

emergency = detect_emergency(problem_description)
service = detect_service(problem_description)
priority = determine_priority(emergency, service)

technician = assign_available_technician(service)
estimated_arrival = estimate_arrival(priority)

respond_to_emergency(emergency)
save_customer_record(
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
)

add_to_dispatch_queue(
    job_number,
    customer_name,
    city,
    service,
    priority,
    preferred_day,
    preferred_time,
    technician,
)

print()
print("========== SERVICE CONFIRMATION ==========")
print(f"Thank you, {customer_name}. Your service request has been received.")
print(f"Job Number: {job_number}")
print(f"Preferred Day: {preferred_day}")
print(f"Preferred Time: {preferred_time}")
print(f"Assigned Technician: {technician}")
print(f"Estimated Arrival: {estimated_arrival}")
print("We will contact you if there are any updates.")
print("==========================================")

   


print()
print("============== JOB TICKET ==============")

print()
print(f"Job Number: {job_number}")
print("Status: Waiting for Dispatch")
print()
print("Customer Information")
print("--------------------")

print(f"Name: {customer_name}")
print(f"Phone: {phone_number}")
print(f"Address: {address}")
print(f"City: {city}")
print()
print("Service Details")
print("----------------")

print(f"Problem: {problem_description}")
print(f"Service: {service}")
print(f"Emergency: {emergency}")
print(f"Priority: {priority}")
print()
print("Dispatch Information")
print("--------------------")
print(f"Technician: {technician}")
print(f"Estimated Arrival: {estimated_arrival}")
print("Job Status: Waiting for Dispatch")
print("==========================================")