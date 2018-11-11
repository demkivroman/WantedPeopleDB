from peoplesWDB.models.wanted_person import WantedPerson
import random
import pdb

def basePerList(request):
    allRecords = WantedPerson.objects.all()
    context = {}
    if len(allRecords) < 5:
        context['BASEPERSONS'] = allRecords
    else:
        ls = []
        for i in range(0,5):
            ls.append(allRecords[random.randint(0, len(allRecords)-1)])
        context['BASEPERSONS'] = ls
    return context