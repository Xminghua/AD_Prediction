  
$(document).ready(function() {
   var sparklineChart = function() { 



       $('#sparkline1').sparkline([22, 24, 45, 36,46, 55, 65, 55, 40], {
            type: 'line',
            width: '100%',
            height: '170',
            chartRangeMax: 50,
            resize: true,
            lineColor: '#13dafe',
            fillColor: 'rgba(3, 169, 243, 0.6)',
            highlightLineColor: 'rgba(0,0,0,.1)',
            highlightSpotColor: 'rgba(0,0,0,.2)',
        });
    
        $('#sparkline1').sparkline([20, 25, 26, 24, 25, 33, 30, 22, 19], {
            type: 'line',height: '165',
            chartRangeMax: 40,
            lineColor: '#03A9F3',
            fillColor: 'rgba(150, 117, 206, 0.3)',
            composite: true,
            highlightLineColor: 'rgba(0,0,0,.1)',
            highlightSpotColor: 'rgba(0,0,0,.2)',
        });
    
        $('#sparkline2').sparkline([6, 6, 7, 8, 6, 4, 7,12, 7, 12, 8, 9, 12, 13, 11, 12], {
            type: 'bar',
            height: '170',
            barWidth: '10',
            barSpacing: '3',
            barColor: '#5CB85C'
        });
        
        $('#sparkline3').sparkline([25, 20, 25, 30], {
            type: 'pie',
            width: '170',
            height: '170',
            sliceColors: ['#03A9F3', '#FFAA00', '#EF5350', '#9675CE']
        });
    
        $('#sparkline4').sparkline([0, 24, 40, 32, 40, 45, 55, 36, 40], {
            type: 'line',height: '165',
			width: '100%',
            chartRangeMax: 50,
            lineColor: '#fb6d9d',
            fillColor: 'transparent',
            highlightLineColor: 'rgba(0,0,0,.1)',
            highlightSpotColor: 'rgba(0,0,0,.2)'
        });
    
        $('#sparkline4').sparkline([20, 25, 27, 22, 25, 30, 35, 20,24], {
            type: 'line',height: '165',
            chartRangeMax: 40,
            lineColor: '#5d9cec',
            fillColor: 'transparent',
            composite: true,
            highlightLineColor: 'rgba(0,0,0,1)',
            highlightSpotColor: 'rgba(0,0,0,1)'
        });
    
	
  $("#sparkline5").sparkline([4, 6, 7, 7, 4, 3, 2, 1, 4, 4, 5, 6, 3, 4, 5, 8, 7, 6, 9, 3, 2, 4, 1, 5, 6, 4, 3, 7, ], {
        type: 'discrete',
        lineColor: '#6059ee',height: '170',
		width: $('#sparkline4').width(),
    });	
	
        $('#sparkline6').sparkline([4, 7, 8, 5, 8, 9, 4, 10, 12, 7, 4, 6, 11, 12, 7, 12], {
            type: 'bar',
            height: '170',
            barWidth: '10',
            barSpacing: '3',
            barColor: '#03A9F3'
        });
    
        $('#sparkline6').sparkline([4, 7, 8, 5, 8, 9, 4, 10, 12, 7, 4, 6, 11, 12, 7, 12],{
            type: 'line',height: '165',
            lineColor: '#FB6D9D',
            fillColor: 'transparent',
            composite: true,
            highlightLineColor: 'rgba(0,0,0,.1)',
            highlightSpotColor: '#03A9F3'
        });
        
   
   
   
   }
    var sparkResize;
 
        $(window).resize(function(e) {
            clearTimeout(sparkResize);
            sparkResize = setTimeout(sparklineChart, 500);
        });
        sparklineChart();

});