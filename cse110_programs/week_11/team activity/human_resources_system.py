# This program lists names, id, job titles,  and salaries of individuals at a company
# Patrick T. Edgett
# 11/25/24

with open("hr_system.txt") as file:
    for line in file:
        parts = line.split()
        name = parts[0].strip()
        id = int(parts[1])
        job_title = parts[2].strip()
        salary = float(parts[3])
        # Paid bi-weekly - 12 months * 2
        paycheck = salary / 24
        # Engineer Bonus
        if job_title == "Engineer":
            paycheck += 1000
        print(f"Name: {name} (ID: {id}), {job_title} - {paycheck:.2f}")