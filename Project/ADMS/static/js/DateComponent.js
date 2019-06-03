/**
 * create by zhaomingqiang 2017.12.26
 * 
 * 日期界面
 */

;define([
	'../DateBox/extend',
	'../DateBox/Tit',
	'../DateBox/compareDate'
],function(
	extend,
	Tit,
	compareDate
){
	
	var DateComponent = function(dateBox,opts){
		
		var box = this.box = document.createElement('div');
		dateBox.container.appendChild(box);
		this.dateBox = dateBox;
		
		
		var opts = this.opts = extend(opts||{},{
			width:198,				//选择日期窗口宽度
			height:197,				//选择日期窗口高度

			
			dateButoonFontSize:12,	//选择日期按钮字体大小
			dateButoonWidth:28,		//选择日期按钮宽度
			dateButoonHeight:25,	//选择日期按钮高度
			weekTitBackground:'#f8f8f8',		//工作日标题背景颜色
			
			dateButtonBackground:'#fff',		//选择日期按钮背景颜色
			dateButtonHoverBack:'#e6e6e6',		//选择日期按钮鼠标移动到上面的背景颜色
			
			titStyle:{
				
			}
			
		});
		//初始化DOM元素
		this.initDOM();
		//初始化样式
		this.initStyle();
		//根据dateBox更新内容
		this.update(dateBox.dateTime);
		//添加事件
		this.addEL();
	};
	
	DateComponent.prototype.addTit = function(){
		var opts = this.opts.titStyle;
		var _this = this;

		var tit = this.tit = new Tit(opts);
		tit.addEL({
			left:function(){
				_this.dateBox.dateTime.plusMonth(-1);
			},
			right:function(){
				_this.dateBox.dateTime.plusMonth();
			}
		});	
		this.box.appendChild(tit.obj);
	};
	
	DateComponent.prototype.update = function(date){
		var _this = this;
		var monthStr =['一月','二月','三月','四月','五月','六月','七月','八月','九月','十月','十一月','十二月'];
			this.tit.setText(date.year + ' ' +monthStr[date.month-1]);
			
			var dates = date.getMonthDates();
			for(var i = 0;i<42;i++){
				_this.dates[i].innerHTML = dates[i].date;
				var dm = dates[i].dm;
				_this.dates[i].index = dm;
				if(dm!=0){
					_this.dates[i].style.color = '#787878';
				}else{
					_this.dates[i].style.color = '#000';
				}
			}
			
	};
	
	DateComponent.prototype.initDOM = function(){
		this.box.innerHTML='';
		this.addTit();
		var con = this.con = document.createElement('div');
		this.box.appendChild(con);
		
		var weekStr = ['日','一','二','三','四','五','六'];
		var weeks = this.weeks = [];
		var dates = this.dates = [];

		for(var i=0;i<7;i++){
			var div = document.createElement('div');
			div.innerHTML = weekStr[i];
			con.appendChild(div);
			weeks.push(div);
		};
		for(var i=0;i<42;i++){
			var div = document.createElement('div');
			con.appendChild(div);
			dates.push(div);
		};
		
	};

	DateComponent.prototype.show = function(){
		this.box.style.display = 'block';
	};

	DateComponent.prototype.hide = function(){
		this.box.style.display = 'none';
	};


	DateComponent.prototype.initStyle = function(){
		var _this = this;
		
		var bs = this.box.style;
		bs.float = 'left';
		bs.width = parseInt(this.opts.width) + 'px';
		bs.height = parseInt(this.opts.height) + 'px';
		
		var cs = this.con.style;
		cs.overflow = 'hidden';

		for(var i=0;i<7;i++){
			var divs = this.weeks[i].style;
			commonStyle(divs);
			divs.background = _this.opts.weekTitBackground;
		};
		for(var i=0;i<42;i++){
			var divs = this.dates[i].style;
			divs.cursor = 'pointer';
			commonStyle(divs);
			divs.background = _this.opts.dateButtonBackground;			
		};
		
		function commonStyle(objs){
			objs.float = 'left';
			objs.fontSize = parseInt(_this.opts.dateButoonFontSize) + 'px';
			objs.width = parseInt(_this.opts.dateButoonWidth) + 'px';
			objs.height = objs.lineHeight = parseInt(_this.opts.dateButoonHeight) + 'px';
			objs.textAlign = 'center'; 
		}
				
	};

	DateComponent.prototype.addEL = function(){
		var _this = this;
		var maxDate = _this.dateBox.opts.maxDate == 'today'?_this.dateBox.dateTime.getTodayStr(): _this.dateBox.opts.maxDate;
		for(var i=0;i<42;i++){
			(function(index){				
				_this.dates[index].addEventListener('click',function(){
					var date = {
						year:_this.dateBox.dateTime.year,
						month:_this.dateBox.dateTime.month + this.index,
						date: Number(this.innerHTML)
					};
					//检测日期是否在范围之内	
					if(!compareDate(date,_this.dateBox.opts.minDate))return;
					if(!compareDate(maxDate,date))return;
					
					_this.dateBox.dateTime.setDateTime(date);

					_this.dateBox.setFooter(_this.dateBox.dateTime.toString('y-d'));
					if(_this.dateBox.hourComponent){
						_this.dateBox.hourComponent.show();
					}else{
						_this.dateBox.initCS();
						_this.dateBox.inputTime();
					}
				});
				
				_this.dates[index].addEventListener('mouseover',function(){
					this.style.cursor = 'pointer';
					var date = {
						year:_this.dateBox.dateTime.year,
						month:_this.dateBox.dateTime.month + this.index,
						date: Number(this.innerHTML)
					};
					//检测日期是否在范围之内	
					if((!compareDate(date,_this.dateBox.opts.minDate))||(!compareDate(maxDate,date))){
						this.style.cursor = 'not-allowed';
					}else{
						this.style.cursor = 'pointer';
						this.style.background = _this.opts.dateButtonHoverBack;
					};
				});
				_this.dates[index].addEventListener('mouseout',function(){
					this.style.background = _this.opts.dateButtonBackground;
				});

				
			})(i);
		};
		
	};
	

	return DateComponent;
});
