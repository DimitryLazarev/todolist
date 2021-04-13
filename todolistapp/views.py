from django.shortcuts import render, redirect

from todolistapp.forms import NoteForm
from todolistapp.models import ToDoList, ToDoListFiltered

DECODER = dict()


def main_page(request):
    notes = ToDoList.objects.all()
    return render(request, 'main_page.html', {'notes': notes})


def up_arrow(request, position):
    prev_position = position - 1
    note = ToDoList.objects.get(position=position)
    old_note = ToDoList.objects.get(position=prev_position)
    note.position, old_note.position = prev_position, position
    note.save()
    old_note.save()
    return redirect('main-page')


def down_arrow(request, position):
    next_position = position + 1
    note = ToDoList.objects.get(position=position)
    old_note = ToDoList.objects.get(position=next_position)
    note.position, old_note.position = next_position, position
    note.save()
    old_note.save()
    return redirect('main-page')


def note_deleter(request, position):
    note = ToDoList.objects.get(position=position)
    note.delete()
    notes = ToDoList.objects.all()
    for note in notes:
        if note.position > position:
            note.position -= 1
            note.save()
    return redirect('main-page')


def note_updater(request, position):
    if request.method == 'GET':
        note = ToDoList.objects.get(position=position)
        notes = ToDoList.objects.all()
        return render(request, 'main_page.html', {'notes': notes,
                                                  'form': NoteForm(initial={'note': note.text}),
                                                  'pos': position,
                                                  })
    else:
        form = NoteForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            old_note = ToDoList.objects.get(position=position)
            old_note.text = cd.get('note')
            old_note.save()
        return redirect('main-page')


def note_adder(request):
    notes = ToDoList.objects.all()
    for note in notes:
        note.position += 1
        note.save()
    ToDoList.objects.create(text='', position=1, priority='low', readiness=False)
    return redirect('note-updater', position=1)


def set_priority(request, position, priority, filter):
    if filter == 'None':
        note = ToDoList.objects.get(position=position)
        note.priority = priority
        note.save()
        return redirect('main-page')
    else:
        note = ToDoListFiltered.objects.get(position=position).todolist
        note.priority = priority
        note.save()
        return redirect('priority-filter', filter_type=filter)


def checkbox(request, position, filter):
    if filter == 'None':
        note = ToDoList.objects.get(position=position)
        if note.readiness:
            note.readiness = False
            note.save()
        else:
            note.readiness = True
            note.save()
        return redirect('main-page')
    else:
        note = ToDoListFiltered.objects.get(position=position).todolist
        if note.readiness:
            note.readiness = False
            note.save()
        else:
            note.readiness = True
            note.save()
        return redirect('priority-filter', filter_type=filter)


def priority_filter(request, filter_type):
    if filter_type == 'htl':
        ToDoListFiltered.objects.all().delete()
        position_counter = 1
        high_priority_notes = ToDoList.objects.filter(priority='high')
        for note in high_priority_notes:
            ToDoListFiltered.objects.create(
                        text=note.text,
                        position=position_counter,
                        priority=note.priority,
                        readiness=note.readiness,
                        todolist=note,
                    )
            position_counter += 1
        medium_priority_notes = ToDoList.objects.filter(priority='medium')
        for note in medium_priority_notes:
            ToDoListFiltered.objects.create(
                text=note.text,
                position=position_counter,
                priority=note.priority,
                readiness=note.readiness,
                todolist=note,

            )
            position_counter += 1
        low_priority_notes = ToDoList.objects.filter(priority='low')
        for note in low_priority_notes:
            ToDoListFiltered.objects.create(
                text=note.text,
                position=position_counter,
                priority=note.priority,
                readiness=note.readiness,
                todolist=note,
            )
            position_counter += 1
        notes = ToDoListFiltered.objects.all()
        return render(request, 'main_page.html', {'notes': notes, 'filter': True, 'filter_type': 'htl'})
    elif filter_type == 'lth':
        ToDoListFiltered.objects.all().delete()
        position_counter = 1
        low_priority_notes = ToDoList.objects.filter(priority='low')
        for note in low_priority_notes:
            ToDoListFiltered.objects.create(
                text=note.text,
                position=position_counter,
                priority=note.priority,
                readiness=note.readiness,
                todolist=note,
            )
            position_counter += 1
        medium_priority_notes = ToDoList.objects.filter(priority='medium')
        for note in medium_priority_notes:
            ToDoListFiltered.objects.create(
                text=note.text,
                position=position_counter,
                priority=note.priority,
                readiness=note.readiness,
                todolist=note,
            )
            position_counter += 1
        high_priority_notes = ToDoList.objects.filter(priority='high')
        for note in high_priority_notes:
            ToDoListFiltered.objects.create(
                text=note.text,
                position=position_counter,
                priority=note.priority,
                readiness=note.readiness,
                todolist=note,
            )
            position_counter += 1
        notes = ToDoListFiltered.objects.all()
        return render(request, 'main_page.html', {'notes': notes, 'filter': True, 'filter_type': 'lth'})
    elif filter_type == 'ho':
        ToDoListFiltered.objects.all().delete()
        position_counter = 1
        high_priority_notes = ToDoList.objects.filter(priority='high')
        for note in high_priority_notes:
            ToDoListFiltered.objects.create(
                text=note.text,
                position=position_counter,
                priority=note.priority,
                readiness=note.readiness,
                todolist=note,
            )
            position_counter += 1
        notes = ToDoListFiltered.objects.all()
        return render(request, 'main_page.html', {'notes': notes, 'filter': True, 'filter_type': 'ho'})
    elif filter_type == 'mo':
        ToDoListFiltered.objects.all().delete()
        position_counter = 1
        medium_priority_notes = ToDoList.objects.filter(priority='medium')
        for note in medium_priority_notes:
            ToDoListFiltered.objects.create(
                text=note.text,
                position=position_counter,
                priority=note.priority,
                readiness=note.readiness,
                todolist=note,
            )
            position_counter += 1
        notes = ToDoListFiltered.objects.all()
        return render(request, 'main_page.html', {'notes': notes, 'filter': True, 'filter_type': 'mo'})
    elif filter_type == 'lo':
        ToDoListFiltered.objects.all().delete()
        position_counter = 1
        low_priority_notes = ToDoList.objects.filter(priority='low')
        for note in low_priority_notes:
            ToDoListFiltered.objects.create(
                text=note.text,
                position=position_counter,
                priority=note.priority,
                readiness=note.readiness,
                todolist=note,
            )
            position_counter += 1
        notes = ToDoListFiltered.objects.all()
        return render(request, 'main_page.html', {'notes': notes, 'filter': True, 'filter_type': 'lo'})
