$(function(){
  
    //editables 
    $('#username').editable({
           url: '/post',
           type: 'text',
           pk: 1,
           name: 'username',
           title: 'Enter username'
    });
    
    $('#firstname').editable({
        validate: function(value) {
           if($.trim(value) == '') return 'This field is required';
        }
    });
    
    $('#sex').editable({
        prepend: "not selected",
        source: [
            {value: 1, text: 'Male'},
            {value: 2, text: 'Female'}
        ],
        display: function(value, sourceData) {
             var colors = {"": "gray", 1: "green", 2: "blue"},
                 elem = $.grep(sourceData, function(o){return o.value == value;});
                 
             if(elem.length) {    
                 $(this).text(elem[0].text).css("color", colors[value]); 
             } else {
                 $(this).empty(); 
             }
        }   
    });    
    
    
$('#status').editable();   
    
    $('#group').editable({
       showbuttons: false 
    });   

   /* $('#vacation').editable({
        datepicker: {
            todayBtn: 'linked'
        } 
    });  */
        
    $('#dob').editable();
          
    $('#event').editable({
        placement: 'right',
        combodate: {
            firstItem: 'name'
        }
    });      
    
    /*$('#meeting_start').editable({
        format: 'yyyy-mm-dd hh:ii',    
        viewformat: 'dd/mm/yyyy hh:ii',
        validate: function(v) {
           if(v && v.getDate() == 10) return 'Day cant be 10!';
        },
        datetimepicker: {
           todayBtn: 'linked',
           weekStart: 1
        }        
    });            */
    
    $('#comments').editable({
        showbuttons: 'bottom'
    }); 
   

    //inline editables 
    $('#inline-username').editable({
		 mode: 'inline',
           url: '/post',
           type: 'text',
           pk: 1,
           name: 'username',
           title: 'Enter username'
    });
    
    $('#inline-firstname').editable({
		 mode: 'inline',
        validate: function(value) {
           if($.trim(value) == '') return 'This field is required';
        }
    });
    
    $('#inline-sex').editable({
		 mode: 'inline',
        prepend: "not selected",
        source: [
            {value: 1, text: 'Male'},
            {value: 2, text: 'Female'}
        ],
        display: function(value, sourceData) {
             var colors = {"": "gray", 1: "green", 2: "blue"},
                 elem = $.grep(sourceData, function(o){return o.value == value;});
                 
             if(elem.length) {    
                 $(this).text(elem[0].text).css("color", colors[value]); 
             } else {
                 $(this).empty(); 
             }
        }   
    });    
    
    
$('#inline-status').editable({
 mode: 'inline',
});   
    
    $('#inline-group').editable({
		 mode: 'inline',
       showbuttons: false 
    });   

    $('#inline-vacation').editable({
		 mode: 'inline',
        datepicker: {
            todayBtn: 'linked'
        } 
    });  
        
    $('#inline-dob').editable({
	 mode: 'inline',
	});
          
    $('#inline-event').editable({
		 mode: 'inline',
        placement: 'right',
        combodate: {
            firstItem: 'name'
        }
    });      
    
   /* $('#inline-meeting_start').editable({
		 mode: 'inline',
        format: 'yyyy-mm-dd hh:ii',    
        viewformat: 'dd/mm/yyyy hh:ii',
        validate: function(v) {
           if(v && v.getDate() == 10) return 'Day cant be 10!';
        },
        datetimepicker: {
           todayBtn: 'linked',
           weekStart: 1,
		   
        }        
    });      */      
    
    $('#inline-comments').editable({
        showbuttons: 'bottom',
		 mode: 'inline'
    }); 
    









	
   
});