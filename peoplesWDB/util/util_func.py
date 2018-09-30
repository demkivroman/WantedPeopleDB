from ..models.wanted_person import WantedPerson
import pdb

# function for seeking records in database
def util_main_searc(param):
    results = []
    allRecords = WantedPerson.objects.all()
    for record in allRecords:
        s = str(record.first_name) + " " + str(record.last_name) + " " + str(
        record.country) + " " + str(record.city)
        if str(param).lower() in s.lower():
            results.append(record)
    return results

# function for return id of persons from currentURL
def util_currId(param):
    perId = ""
    for item in param:
        perId += str(item.id) + "/"
    return perId
