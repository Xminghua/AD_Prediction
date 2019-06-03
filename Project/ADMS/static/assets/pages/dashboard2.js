$(document).ready(function () {
	
	
	/*Sales Statics chart*/
	
    $(function () {

    var sharpLineData = {
        labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [
            {
                label: "Example dataset",
                fillColor: "rgba(3,169,243,0.7)",
                strokeColor: "rgba(23,112,233,0.7)",
                pointColor: "rgba(23,112,233,1)",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(23,112,233,1)",
                data: [30, 55, 45, 20, 55, 30, 60]
            }
        ]
    };

    var sharpLineOptions = {
	scaleShowGridLines: true,
	scaleGridLineColor: "rgba(0,0,0,.00)",
	scaleGridLineWidth: 1,
	bezierCurve: false,
	pointDot: true,
	pointDotRadius: 4,
	pointDotStrokeWidth: 1,
	pointHitDetectionRadius: 20,
	datasetStroke: false,
	datasetStrokeWidth: 1,
	datasetFill: true,
	responsive: true,
	resize: true
    };

    var ctx = document.getElementById("sharpLinechart").getContext("2d");
    var myNewChart = new Chart(ctx).Line(sharpLineData, sharpLineOptions);


    });
    


  /* Sparkline chart	*/
	
   var sparklineLogin = function() { 
   

   $('#sparklinestats1').sparkline([ 7, 9, 11, 10, 11, 12, 9, 12], {
            type: 'bar',
            height: '30',
            barWidth: '4',
            resize: true,
            barSpacing: '5',
            barColor: '#E5051F'
        });


 $('#sparklinestats2').sparkline([ 7, 9, 11, 10, 11, 12, 9, 12], {
            type: 'bar',
            height: '30',
            barWidth: '4',
            resize: true,
            barSpacing: '5',
            barColor: '#BA0C83'
        });



       
        $('#sparklinestats3').sparkline([ 7, 9, 11, 10, 11, 12, 9, 12], {
            type: 'bar',
            height: '30',
            barWidth: '4',
            resize: true,
            barSpacing: '5',
            barColor: '#E05316'
        });
         $('#sparklinestats4').sparkline([ 7, 9, 11, 10, 11, 12, 9, 12], {
            type: 'bar',
            height: '30',
            barWidth: '4',
            resize: true,
            barSpacing: '5',
            barColor: '#7134E3'
        });
         
        
   
   }
    var sparkResize;
 
        $(window).resize(function(e) {
            clearTimeout(sparkResize);
            sparkResize = setTimeout(sparklineLogin, 500);
        });
        sparklineLogin();

});
   
  
  
  /*To do list*/
		
	 $(".list-task li label").click(function() {
            $(this).toggleClass("task-done");
     });
		
		
