def generate_job_number():
    with open("job_number.txt", "a+") as file:
        file.seek(0)
        current_number = int(file.read() or 0)

    new_number = current_number + 1

    with open("job_number.txt", "w") as file:
        file.write(str(new_number))

    job_number = f"ATLAS-{new_number:06d}"

    return job_number