import streamlit as st
from customer_manager import detect_service, detect_emergency, determine_priority, save_customer_record
from job_manager import generate_job_number
from dispatch_manager import add_to_dispatch_queue
st.title("Atlas AI Digital Employee")
customer_name = st.text_input("What is your name?")
phone_number = st.text_input("What is your phone number?")
address = st.text_input("What is your street address?")
city = st.text_input("What city are you located in?")
preferred_day = st.text_input("What day would you prefer for service?")
preferred_time = st.text_input("What time would you prefer?")
problem_description = st.text_area("Please describe the plumbing problem:")
submit = st.button("Submit Service Request")
if submit:
    if not customer_name:
       st.error("Please enter your name.")
       st.stop() 
    if not phone_number: 
       st.error("Please enter your phone number.")
       st.stop()
    if not address:
       st.error("Please enter your street address.")
       st.stop()
    if not city:
       st.error("Please enter your city.")
       st.stop()   
    if not problem_description: 
       st.error("Please describe the plumbing problem.")
       st.stop()
    st.success("Service Request Confirmed!")
    service = detect_service(problem_description)
    st.write("Detected Service:", service)
    emergency = detect_emergency(problem_description)
    st.write("Emergency:", emergency)
    priority = determine_priority(emergency, service)
    st.write("Priority:", priority)
    job_number = generate_job_number()
    technician = "Unassigned"
    st.success(f"Job Number: {job_number}")
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
 