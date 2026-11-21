
# Q4 - Junior Data Analyst Recruitment

required = {"python", "sql", "excel", "statistics"}

applicants = [
    {"name": "Ram", "age": 24, "cgpa": 3.4,
     "skills": {"python", "excel", "html"}},

    {"name": "Sita", "age": 37, "cgpa": 3.8,
     "skills": {"python", "sql", "excel", "statistics"}},

    {"name": "Gita", "age": 26, "cgpa": 3.6,
     "skills": {"python", "sql", "statistics", "tableau"}},

    {"name": "Hari", "age": 29, "cgpa": 2.7,
     "skills": {"sql", "excel", "statistics", "python"}},
]

shortlisted = []
extra_skills = set()

for applicant in applicants:
    name = applicant["name"]
    age = applicant["age"]
    cgpa = applicant["cgpa"]
    skills = applicant["skills"]

    # Collect skills that are not required
    extra_skills.update(skills - required)

    # Reject applicants outside the age range
    if age < 21 or age > 35:
        print(f"{name}: rejected (age {age})")
        continue

    # Find matching and missing skills
    matching = required & skills
    missing = required - skills

    match_percentage = len(matching) / len(required) * 100

    # Check shortlist conditions
    if match_percentage >= 75 and cgpa >= 2.5:
        status = "shortlisted"
        shortlisted.append((name, match_percentage, cgpa))
    else:
        status = "not shortlisted"

    print(
        f"{name}: {match_percentage:g}% match, "
        f"{status}, missing {sorted(missing)}"
    )

# Sort by highest match percentage, then highest CGPA
shortlisted.sort(key=lambda x: (-x[1], -x[2]))

interview_order = []

for applicant in shortlisted:
    interview_order.append(applicant[0])

print("Interview order:", interview_order)
print("Extra skills seen (not required):", sorted(extra_skills))
