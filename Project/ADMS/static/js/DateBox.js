/**
 * create by zhaomingqiang 2017.12.21
 * 
 * 只依赖于requirejs
 * 
 * 参数说明
 * obj 为原生对象或者id
 * opts 为参数
 * 
 */


define([
	'../DateBox/extend',
	'../DateBox/DateTime',
	'../DateBox/MonthComponent',
	'../DateBox/DateComponent',
	'../DateBox/HourComponent',
	'../DateBox/hasEle',
	'../DateBox/clearFix',
	'../DateBox/defaultOpts'
],function(
	extend,
	DateTime,
	MonthComponent,
	DateComponent,
	HourComponent,
	hasEle,
	clearFix,
	defaultOpts
){
	
	var DateBox = function(obj,opts){
		//容器
		this.obj = document.getElementById(obj)?document.getElementById(obj):obj;
		//参数
		this.opts = extend(opts||{},defaultOpts);
		//默认日期
		this.dateTime = new DateTime(this.opts.date||{});
		
		this.initDOM();						//初始化dom
		this.initStyle();					//初始化样式
		this.addEL();						//添加事件
		this.addComponent();				//添加组成部分
		this.initCS();						//初始化组建状态
		this.timeChangeCallBack();			//添加时间更改后的回掉函数

	};
	//初始化DOM元素
	DateBox.prototype.initDOM = function(){
		var box = this.box = document.createElement('div');
		var container = this.container = document.createElement('div');
		var footer = this.footer = document.createElement('div');
		this.setFooter();
		box.appendChild(container);
		box.appendChild(footer);
		document.body.appendChild(box);
	};
	
	//设置footer属性
	DateBox.prototype.setFooter = function(str){
		this.removeFootClick();
		var _this = this;
		if(str == 'today'){
			var dateTime = this.dateTime;
			this.footer.innerHTML = '今天:&nbsp;&nbsp;' + dateTime.getTodayStr();
			this.addFootClick(function(){
				dateTime.toToday();
				_this.inputTime();
			});
		}else{
			this.footer.innerHTML = '当前:&nbsp;&nbsp;' + str ||'';
		}		
	};
	
	//添加footer点击事件
	DateBox.prototype.addFootClick = function(fn){
		this.removeFootClick();
		this.footClick = fn;
		this.footer.addEventListener('click',this.footClick);
		this.footer.style.cursor = 'pointer';
	};
	//移除footer点击事件
	DateBox.prototype.removeFootClick = function(fn){
		this.footClick && this.footer.removeEventListener('click',this.footClick);
		this.footClick = null;
		this.footer.style.cursor = 'auto';
	};
	
	//初始化样式
	DateBox.prototype.initStyle = function(){
		
		this.hide();
		
		var boxStyle = this.opts.boxStyle;		
		var bs = this.box.style;
		//bs.width = parseInt(boxStyle.width) + 'px';
		//bs.height = parseInt(boxStyle.height) + 'px';
		bs.border = parseInt(boxStyle.borderWidth) + 'px solid '+boxStyle.borderColor;
		bs.background  = boxStyle.backgroundColor;
		bs.position = 'absolute';
		bs.top = this.obj.getBoundingClientRect().bottom + 'px';
		bs.left = this.obj.getBoundingClientRect().left + 'px';
		
		var cs = this.container.style;
		//cs.overflow = 'hidden';
		//cs.height = parseInt(boxStyle.containerHeight) + 'px';
		
		var fs = this.footer.style;
		fs.height = parseInt(boxStyle.footerHeight) + 'px';
		fs.background = boxStyle.footerBackground;
		fs.color = boxStyle.footerFontColor;
		fs.lineHeight = parseInt(boxStyle.footerHeight) + 'px';
		fs.textAlign = 'center';
		fs.fontSize = parseInt(boxStyle.footerFontSize) + 'px';
		fs.borderTop = parseInt(boxStyle.footerSegLineWidth) + 'px solid '+boxStyle.footerSegLineColor;
	};
	//添加事件
	DateBox.prototype.addEL = function(){
		var _this = this;
		//获取焦点
		this.obj.addEventListener('focus',function(){
			_this.show();
		});
		//失去焦点
		this.obj.addEventListener('blur',function(){
			_this.hide();
			_this.initCS();
		});
		//阻止日期插件的点击失去焦点事件
		document.addEventListener('mousedown',function(ev){
			
			var e = ev||event;
			var a = e.srcElement || e.target;
			if((_this.status == 'show')&&(_this.box == a||_this.obj == a||hasEle(_this.box,a))){
				e.preventDefault();
				return false;
			}
			
		});
	};
	//显示
	DateBox.prototype.show = function(){
		this.status = 'show';
		this.box.style.top = this.obj.getBoundingClientRect().bottom + 'px';
		this.box.style.left = this.obj.getBoundingClientRect().left + 'px';
		this.box.style.display = 'block';
	};
	//隐藏
	DateBox.prototype.hide = function(){
		this.status = 'hide';
		this.box.style.display = 'none';
	};
	//根据类型添加组建
	DateBox.prototype.addComponent = function(){	
		var month,date,hour;
		switch(this.opts.type){
			case 'y-d':
				month=date=true;
			break;
			case 'y-m':
				month=date=hour=true;
			break;
			case 'h-m':
				hour=true;
			break;
			case 'M':
				date = true;
			break;
			case 'Y':
				month = true;
			break;
		}
		
		if(month){
			this.monthComponent = new MonthComponent(this,this.opts.monthComponentStyle);
		}
		if(date){
			this.dateComponent = new DateComponent(this,this.opts.dateComponentStyle);
		}
		if(hour){
			this.hourComponent = new HourComponent(this,this.opts.hourComponentStyle);
		}
		//清浮动
		clearFix(this.container);
	};
	
	//初始化组建状态 initComponentsStatus 简化 initCS
	DateBox.prototype.initCS = function(){
		this.monthComponent&&this.monthComponent.hide();
		this.dateComponent&&this.dateComponent.hide();
		this.hourComponent&&this.hourComponent.hide();
		switch(this.opts.type){
			case 'y-d':
				this.monthComponent.show();
				this.setFooter(this.dateTime.year);
			break;
			case 'y-m':
				this.monthComponent.show();
				this.setFooter(this.dateTime.year);
			break;
			case 'h-m':
				this.hourComponent.show();
				this.setFooter(this.dateTime.hour + ':00');
			break;
			case 'M':
				this.dateComponent.show();
				//this.setFooter(this.dateTime.year);
				this.setFooter('today');
			break;
			case 'Y':
				this.monthComponent.show();
				//this.setFooter(this.dateTime.year);
				this.setFooter(this.dateTime.toString('y-M'));
			break;
		}
		
	};
	
	DateBox.prototype.setDateTime = function(opts){
		this.dateTime.setDateTime(opts);
		this.inputTime();
	};
	
	DateBox.prototype.timeChangeCallBack = function(){
		var _this = this;
		this.dateTime.setChangeCallBack(function(){
			_this.monthComponent&&_this.monthComponent.update(_this.dateTime);
			_this.dateComponent&&_this.dateComponent.update(_this.dateTime);
			_this.hourComponent&&_this.hourComponent.update(_this.dateTime);		
		});
	};
	
	DateBox.prototype.inputTime = function(){
		this.obj.value = this.dateTime.toString(this.opts.type);
		this.obj.blur();
	};
	
	return DateBox;
	
});