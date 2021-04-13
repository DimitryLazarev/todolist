from django import forms


class NoteForm(forms.Form):
    note = forms.CharField(label='', max_length=20)

    note.widget.attrs.update({'class': 'form'})
    note.widget.attrs.update({'autofocus': ''})


