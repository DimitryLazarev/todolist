from django.urls import path

from todolistapp.views import main_page, up_arrow, down_arrow, note_deleter, note_updater, note_adder, set_priority, \
    checkbox, priority_filter

urlpatterns = [
    path('', main_page, name='main-page'),
    path('up-arrow/<int:position>', up_arrow, name='up-arrow'),
    path('down-arrow/<int:position>', down_arrow, name='down-arrow'),
    path('note-deleter/<int:position>', note_deleter, name='note-deleter'),
    path('note-updater/<int:position>', note_updater, name='note-updater'),
    path('note-adder/', note_adder, name='note-adder'),
    path('set-priority/<int:position>&<str:priority>&<str:filter>', set_priority, name='set-priority'),
    path('checkbox/<int:position>&<str:filter>', checkbox, name='checkbox'),
    path('filter/<str:filter_type>', priority_filter, name='priority-filter'),

]
