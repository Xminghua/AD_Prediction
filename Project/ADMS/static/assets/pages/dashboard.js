
 $(document).ready(function() {
	
    Morris.Bar({
        element: 'morris2',
        data: [
            { year: '2010', a: 30, b: 25 },
            { year: '2011', a: 60, b: 40 },
            { year: '2012', a: 85, b: 65 },
            { year: '2013', a: 100, b: 90 },
            { year: '2014', a: 60, b: 50 },
            { year: '2015', a: 75, b: 65 },
            { year: '2016', a: 100, b: 90 } 
        ],
        xkey: 'year',
        ykeys: ['a', 'b'],
        labels: ['Section A', 'Section B'],
        barRatio: 0.4,
        xLabelAngle: 0,
        hideHover: 'auto',
        barColors: ['#03A9F3','#FFAA00'],
        resize: true
    });	
	
	
	

});
  Morris.Area({
        element: 'morris-area-chart',
        data: [{
                    period: '2010',
                    iphone: 0,
                    ipad: 0,
                    itouch: 0
                }, {
                    period: '2011',
                    iphone: 50,
                    ipad: 40,
                    itouch: 30
                }, {
                    period: '2012',
                    iphone:90,
                    ipad: 70,
                    itouch: 60
                }, {
                    period: '2013',
                    iphone:50,
                    ipad: 40,
                    itouch:30
                }, {
                    period: '2014',
                    iphone:70,
                    ipad: 50,
                    itouch: 30
                }, {
                    period: '2015',
                    iphone:120,
                    ipad: 90,
                    itouch: 60
                }, {
                    period: '2016',
                    iphone:70,
                    ipad: 50,
                    itouch:30
                }


                ],
                lineColors: ['#F9C851', '#01c0c8', '#D5EEE9'],
                xkey: 'period',
                ykeys: ['iphone', 'ipad', 'itouch'],
                labels: ['iphone', 'ipad', 'itouch'],
                pointSize: 0,
                lineWidth: 0,
                resize:true,
                fillOpacity: 0.9,
                behaveLikeLine: true,
                gridLineColor: '#e0e0e0',
                hideHover: 'auto'
        
    });
Morris.Area({
        element: 'morris-area-chart2',
        data: [{
            period: '2010',
            SiteA: 0,
            SiteB: 0,
            
        }, {
            period: '2011',
            SiteA: 130,
            SiteB: 100,
            
        }, {
            period: '2012',
            SiteA: 120,
            SiteB: 60,
            
        }, {
            period: '2013',
            SiteA: 70,
            SiteB: 200,
            
        }, {
            period: '2014',
            SiteA: 180,
            SiteB: 150,
            
        }, {
            period: '2015',
            SiteA: 105,
            SiteB: 90,
            
        },
         {
            period: '2016',
            SiteA: 250,
            SiteB: 150,
           
        }],
        xkey: 'period',
        ykeys: ['SiteA', 'SiteB'],
        labels: ['Site A', 'Site B'],

        pointSize: 0,
        fillOpacity: 0.4,
        pointStrokeColors:['#b4becb', '#01c0c8'],
        behaveLikeLine: true,
        gridLineColor: '#e0e0e0',
        lineWidth: 0,
        smooth: false,
        hideHover: 'auto',
        lineColors: ['#b4becb', '#01c0c8'],
        resize: true
        
    });
$(document).ready(function() {
    
   var sparklineLogin = function() { 
        $('#sales1').sparkline([20, 40, 30], {
            type: 'pie',
            height: '100',
            resize: true,
            sliceColors: ['#808f8f', '#fecd36', '#f1f2f7']
        });
        $('#sales2').sparkline([6, 10, 9, 11, 9, 10, 12], {
            type: 'bar',
            height: '154',
            barWidth: '4',
            resize: true,
            barSpacing: '10',
            barColor: '#25a6f7'
        });
        
   }
    var sparkResize;
 
        $(window).resize(function(e) {
            clearTimeout(sparkResize);
            sparkResize = setTimeout(sparklineLogin, 500);
        });
        sparklineLogin();

});

