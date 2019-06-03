/**
 * create by zhaomingqiang 2017.12.25
 * 
 * 日期时间对象
 */

;define(function(){
	//时间对象
	var DateTime = function(opts){
		
		var opts = opts||{};
		
		var dateTime = this.dateTime = new Date();
		this.year = opts.year || dateTime.getFullYear();
		this.month = opts.month || dateTime.getMonth()+1;
		this.date = opts.date || dateTime.getDate();
		this.hour = opts.hour || dateTime.getHours();
		this.minute = opts.minute || dateTime.getMinutes();
		this.changeCallBack = opts.changeCallBack||null;
		
		this.setDateTime();
	};
	
	//添加时间改变时的回调函数
	DateTime.prototype.setChangeCallBack = function(fn){
		this.changeCallBack = fn||this.changeCallBack;
		fn&&fn(this);
	};
	
	//更改时间
	DateTime.prototype.setDateTime = function(opts){
		var opts = opts || {};
		
		var year = opts.year||this.year;
		var month = (typeof opts.month != 'undefined')?opts.month-1:this.month-1;
		var date = (typeof opts.date != 'undefined')?opts.date:this.date;
		var hour = (typeof opts.hour != 'undefined')?opts.hour:this.hour;
		var minute = (typeof opts.minute != 'undefined')?opts.minute:this.minute;
		
		if(month<=0){
			year = year - parseInt((Math.abs(month))/12) -1;
			month = 12-Math.abs(month%12);
		}
		
		this.dateTime.setFullYear(year,month,date);
		//this.dateTime.setHours(hour,minute,0);
		
		this.year = this.dateTime.getFullYear();
		this.month = this.dateTime.getMonth()+1;
		this.date = this.dateTime.getDate();
//		this.hour = this.dateTime.getHours();
//		this.minute = this.dateTime.getMinutes();
		this.hour = hour;
		this.minute = minute;
		this.changeCallBack&&this.changeCallBack(this);
	};
	
	
	//将时间增加几年, 不填则是一年
	DateTime.prototype.plusYear = function(n){
		var n = n||1;
		this.setDateTime({
			year:this.year + n
		});
	};
	//将月份增加几月, 不填则是1月
	DateTime.prototype.plusMonth = function(n){
		var n = n||1;		
		this.setDateTime({
			month:this.month + n
		});
	};
	
	//获取今天日期的字符串
	DateTime.prototype.getTodayStr = function(){
		var oDate = new Date();	
		return oDate.getFullYear() + '-' + (oDate.getMonth()+1) + '-' + oDate.getDate();
	};
	//将日期设置成今天
	DateTime.prototype.toToday = function(){
		var oDate = new Date();	
		this.setDateTime({
			year:oDate.getFullYear(),
			month:oDate.getMonth()+1,
			date:oDate.getDate()
		});
	};

	//当月日期数据
	DateTime.prototype.getMonthDates = function(){
		var dates = [];
		
		var oDate = new Date();
		oDate.setFullYear(this.year,this.month-1,0);
		var lastMonthLastday = oDate.getDate();
		var lastweek = oDate.getDay();
		var firstday = lastMonthLastday - lastweek;
		
		oDate.setFullYear(this.year,this.month,0);
		var curMonthLastday = oDate.getDate();
		
		
		for(var i=0;i<42;i++){
			var d = firstday + i;
			var json = {};
			if(d<=lastMonthLastday){
				json.date = d;
				json.dm = -1;
			}else if(d>lastMonthLastday&&d<=lastMonthLastday+curMonthLastday){
				json.date = d - lastMonthLastday;
				json.dm = 0;
			}else if(d>lastMonthLastday+curMonthLastday){
				json.date = d - lastMonthLastday - curMonthLastday;
				json.dm = 1;
			}
			dates.push(json);
		}
		
		
		return dates;
	};
	
	DateTime.prototype.toString = function(type){
		var type = type||'y-m';
		
		function toDou(n){return Number(n)>9?''+n:'0'+n;}
		var year = this.year;
		var month = toDou(this.month);
		var date = toDou(this.date);
		var hour = toDou(this.hour);
		var minute = toDou(this.minute);
		
		switch(type){
			case 'y-d':
				return year+'-'+month+'-'+date;
			break;
			case 'M':
				return year+'-'+month+'-'+date;
			break;
			case 'y-m':
				return year+'-'+month+'-'+date+' '+hour+':'+minute;
			break;
			case 'h-m':
				return hour+':'+minute;
			break;
			case 'y-M':
				return year+'-'+month;
			break;
			case 'Y':
				return year+'-'+month;
			break;
		}
		
		
		
	};
	
	return DateTime;
});
