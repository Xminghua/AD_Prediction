/**
 * create by zhaommingqiang 2018.2.7
 * 
 * 比较两个日期的大小,是否大于等于
 */

;define(function(){
	
	function toDateObj(str){
		var arr = str.split('-');
		return {
			year:Number(arr[0]),
			month:Number(arr[1]),
			date:Number(arr[2])
		}
	}
	
	
	
	//参数格式为'yyyy-mm-dd'或者{year:year,month:month,date:date}
	var compareDate = function(date1,date2){
		var dateObj1 = (typeof date1 == 'string')?toDateObj(date1):date1;
		var dateObj2 = (typeof date2 == 'string')?toDateObj(date2):date2;
		
		if(dateObj1.year != dateObj2.year){
			return dateObj1.year > dateObj2.year;
		}else{
			if(dateObj1.month != dateObj2.month){
				return dateObj1.month > dateObj2.month;
			}else{
				return dateObj1.date >= dateObj2.date;
			}
		}
		
		
	};
	
	return compareDate;
	
});
