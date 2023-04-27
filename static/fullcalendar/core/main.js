

document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
      plugins: [ 'dayGrid', 'timeGrid', 'list' ],
      defaultView: 'dayGridMonth',
      events: [
          {
            title: "{{ event.title }}",
            start: "{{ event.start_time.isoformat() }}",
            end: "{{ event.end_time.isoformat() }}",
            url: "{{ url_for('schedule.edit_event', event_id=event.id) }}",
          },
      ],
    });
    calendar.render();
  });