from django.shortcuts import render
from ..models.wanted_person import WantedPerson

def comment_add(request, pk):
    person = WantedPerson.objects.get(pk=pk)
    return render(request, 'comment.html', {'person': person})
