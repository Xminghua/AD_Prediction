/*$( document ).ready(function() {*/
	
	  Morris.Area({
        element: 'morris1',
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
	
	
	
    Morris.Bar({
        element: 'morris2',
        data: [
            { year: '2010', a: 30, b: 60 },
            { year: '2011', a:80, b: 120 },
            { year: '2012', a: 130, b:150 },
            { year: '2013', a: 90, b: 110 },
            { year: '2014', a: 130, b: 150 },
            { year: '2015', a: 120, b: 140 },
            { year: '2016', a: 165, b: 190 } 
        ],
        xkey: 'year',
        ykeys: ['a', 'b'],
        labels: ['a', 'b'],
        barRatio: 0.4,
        hideHover: 'auto',
        barColors: ['#03A9F3','#FFAA00'],
        resize: true
    });
    
    Morris.Line({
        element: 'morris3',
        data: [
            { year: '2010', a: 25, b: 15, c:2 },
            { year: '2011', a: 50, b: 40 ,  c:25},
            { year: '2012', a: 75, b: 65,  c:55 },
            { year: '2013', a: 100, b: 90,  c:75 },
            { year: '2014', a: 60, b: 50,  c:35 },
            { year: '2015', a: 75, b: 65 ,  c:55},
            { year: '2016', a: 100, b: 90,  c:75 } 
        ],
        xkey: 'year',
        ykeys: ['a', 'b','c'],
        labels: ['a', 'b','c'],
        resize: true,
        lineColors: ['#03a9f3','#03a9f3','#03a9f3']
    });
    
    Morris.Donut({
        element: 'morris4',
        data: [
            {label: 'Javascript', value: 45 },
            {label: 'HTML5', value: 60 },
            {label: 'CSS3', value: 90 },
            {label: 'PHP', value: 55 }
        ],
        resize: true,
        colors: ['#6E8CD7', '#34D3EB', '#7266BA','#5DDCEF'],
    });
/*});*/