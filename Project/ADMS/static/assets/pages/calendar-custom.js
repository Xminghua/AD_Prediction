 $(document).ready(function() {
        
        $('#external-events .fc-event').each(function() {
    
          // store data so the calendar knows to render an event upon drop
          $(this).data('event', {
            title: $.trim($(this).text()), // use the element's text as the event title
            stick: true // maintain when user navigates (see docs on the renderEvent method)
          });
    
          // make the event draggable using jQuery UI
          $(this).draggable({
            zIndex: 999,
            revert: true,      // will cause the event to go back to its
            revertDuration: 0  //  original position after the drag
          });
    
        });
    
    
        /* initialize the calendar
        -----------------------------------------------------------------*/
        $('#calendar').fullCalendar({
          header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,basicWeek,basicDay'
          },
          defaultDate: '2017-01-15',
          editable: true,
          droppable: true,
          eventLimit: true, 
          events: [
            {
              title: 'Event Meeting 1',
              start: '2017-01-15',
              color: '#FFBD4A'
            },
            {
              title: 'Birthday Party',
             start: '2017-01-05',
              color: '#FC8AB1'
            },
            {
              title: 'Birthday Party',
             start: '2017-01-09',
              color: '#668CFF'
            },
            {
              title: 'Birthday Party',
             start: '2017-01-11',
              color: '#F05050'
            },
            {
              title: 'Birthday Party',
             start: '2017-01-13',
              color: '#81C868'
            },
            {
              title: 'Birthday Party',
             start: '2017-01-14',
              color: '#F05050'
            }
			
			
          ]
        });
        
      });
    