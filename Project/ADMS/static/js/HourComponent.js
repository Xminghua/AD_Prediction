/**
 * create by zhaomingqiang 2017.12.27
 * 
 * 选择时间界面
 */

;define([
	'../DateBox/extend',
	'../DateBox/Tit',
	'../DateBox/clearFix'
],function(
	extend,
	Tit,
	clearFix
){
	
	var HourComponent = function(dateBox,opts){
		
		var box = this.box = document.createElement('div');
		dateBox.container.appendChild(box);
		this.dateBox = dateBox;
		
		
		var opts = this.opts = extend(opts||{},{
			width:226,				//选择小时窗口宽度
			//height:197,				//选择小时窗口高度0
			leftSegLineColor:'#828790',	//左侧分割线颜色
			leftSegLineWidth:1,		//左侧分割线宽度
			
			titleInner:'小时',		//内标题内容
			titleHeight:21,			//内标题高度
			titleFontSize:12,		//内标题文字大小
			titleTextIndent:8,		//内标题文字缩进距离
			
			hourButoonFontSize:12,	//选择小时按钮字体大小
			hourButoonWidth:31,		//选择小时按钮宽度
			hourButoonHeight:32,	//选择小时按钮高度
			hourButoonRowSpace:4,	//选择小时按钮行间距
			hourButoonColSpace:4,	//选择小时按钮列间距
			hourButoonBorderWidth:1,			//选择小时按钮边线宽度
			hourButoonBorderColor:'#c3c3c3',	//选择小时按钮边线颜色
			hourButoonBackground:'#f9f9f9',		//选择小时按钮背景颜色
			hourButtonHoverBack:'#e6e6e6',		//选择小时按钮鼠标移动到上面的背景颜色
			
			
			minuteStyle:{
			
				width:226,				//选择分钟窗口宽度
				height:99,				//选择分钟窗口高度
				padding:7,				//容器内边距
				background:'#fff',		//选择分钟窗口背景颜色
				borderColor:'#828790',	//选择分钟窗口边线颜色
				borderWidth:1,			//选择分钟窗口边线宽度
				reLeft:25,				//分钟窗口对应小时按钮的左方距离
				reTop:25,				//分钟窗口对应小时按钮的上方距离
			
				titleInner:'分钟',		//内标题内容
				titleHeight:21,		//内标题高度
				titleFontSize:12,		//内标题文字大小
				titleTextIndent:8,	//内标题文字缩进距离
				
				butoonFontSize:12,	//选择分钟按钮字体大小
				butoonWidth:31,		//选择分钟按钮宽度
				butoonHeight:32,		//选择分钟按钮高度
				butoonRowSpace:4,		//选择分钟按钮行间距
				butoonColSpace:4,		//选择分钟按钮列间距
				butoonBorderWidth:1,			//选择分钟按钮边线宽度
				butoonBorderColor:'#c3c3c3',	//选择分钟按钮边线颜色
				butoonBackground:'#f9f9f9',	//选择分钟按钮背景颜色
				buttonHoverBack:'#e6e6e6',	//选择分钟按钮鼠标移动到上面的背景颜色
			},			
			
			
			
			
			titStyle:{
				showArrow:false
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
	
	HourComponent.prototype.addTit = function(){
		var opts = this.opts.titStyle;
		var _this = this;
		var tit = this.tit = new Tit(opts);
		this.box.appendChild(tit.obj);
	};
	
	HourComponent.prototype.update = function(date){
		var _this = this;
		var minute = date.minute>9?''+date.minute:'0'+date.minute;
		this.tit.setText(date.hour + ':' +minute);
			
			
			
	};
	
	HourComponent.prototype.initDOM = function(){
		this.box.innerHTML='';
		this.addTit();
		var con = this.con = document.createElement('div');
		this.box.appendChild(con);
		
		var title = this.title = document.createElement('div');
		title.innerHTML = this.opts.titleInner;
		con.appendChild(title);
		
		var hours = this.hours = [];
		for(var i=0;i<24;i++){
			var div = document.createElement('div');
			div.innerHTML = i>9?''+i:'0'+i;
			con.appendChild(div);
			hours.push(div);
		};
		
		var minuteBox = this.minuteBox = document.createElement('div');
		con.appendChild(minuteBox);

		var minuteTitle = this.minuteTitle =  document.createElement('div');
		minuteTitle.innerHTML = this.opts.minuteStyle.titleInner;
		minuteBox.appendChild(minuteTitle);

		var minutes = this.minutes = [];
		for(var i = 0; i < 12; i++ ){
			var div = document.createElement('div');
			div.innerHTML = (i*5)>9?''+(i*5):'0'+(i*5);
			minuteBox.appendChild(div);
			minutes.push(div);
		}
		
	};

	HourComponent.prototype.show = function(){
		this.box.style.display = 'block';
	};

	HourComponent.prototype.hide = function(){
		this.box.style.display = 'none';
		this.minuteHide();
	};

	HourComponent.prototype.initStyle = function(){
		var _this = this;
		//设置盒子样式
		var bs = this.box.style;
		bs.float = 'left';
		bs.width = parseInt(this.opts.width) + 'px';
		bs.paddingBottom = '2px';
		if(this.dateBox.opts.type != 'h-m')
		bs.borderLeft = parseInt(this.opts.leftSegLineWidth) + 'px solid '+this.opts.leftSegLineColor;
		//设置内容容器样式
		var cs = this.con.style;
		cs.position = 'relative';
		clearFix(this.con);
		//设置小时标题样式
		var tts = this.title.style;
		tts.float = 'left';
		tts.width = '100%';
		tts.height = tts.lineHeight = parseInt(this.opts.titleHeight)+'px';
		tts.fontSize = parseInt(this.opts.titleFontSize)+'px';
		tts.textIndent = parseInt(this.opts.titleTextIndent)+'px';
		//设置小时按钮样式
		for(var i=0;i<24;i++){
			var divs = this.hours[i].style;
			divs.float = 'left';
			divs.width = parseInt(this.opts.hourButoonWidth) + 'px';
			divs.height = divs.lineHeight = parseInt(this.opts.hourButoonHeight) + 'px';
			divs.margin = parseInt(this.opts.hourButoonRowSpace) + 'px 0 0 ' + parseInt(this.opts.hourButoonColSpace) +'px';
			divs.border = parseInt(this.opts.hourButoonBorderWidth) + 'px solid '+ this.opts.hourButoonBorderColor;
			divs.background = this.opts.hourButoonBackground;
			divs.fontSize = parseInt(this.opts.hourButoonFontSize) + 'px'; 
			divs.textAlign = 'center';
			divs.cursor = 'pointer';
			this.hours[i].addEventListener('mouseover',function(){
				this.style.background = _this.opts.hourButtonHoverBack;
			});
			this.hours[i].addEventListener('mouseout',function(){
				this.style.background = _this.opts.hourButoonBackground;
			});
		};

		//设置分钟盒子样式
		var minuteOpts = this.opts.minuteStyle;
		
		var minuteS = this.minuteBox.style;
		minuteS.width = parseInt(minuteOpts.width) + 'px';
		minuteS.height = parseInt(minuteOpts.height) + 'px';
		minuteS.border = parseInt(minuteOpts.borderWidth) + 'px solid '+minuteOpts.borderColor;
		minuteS.background = minuteOpts.background;
		minuteS.padding = parseInt(minuteOpts.padding) + 'px';		
		minuteS.position = 'absolute';
		minuteS.left = '10px';
		minuteS.top = '10px';
		clearFix(this.minuteBox);
		//涉资分钟标题样式	
		var mts = this.minuteTitle.style;
		mts.float = 'left';
		mts.width = '100%';
		mts.height = mts.lineHeight = parseInt(minuteOpts.titleHeight)+'px';
		mts.fontSize = parseInt(minuteOpts.titleFontSize)+'px';
		mts.textIndent = parseInt(minuteOpts.titleTextIndent)+'px';
		//设置分钟按钮 样式
		for(var i = 0;i<12;i++){
			var divs = this.minutes[i].style;
			divs.float = 'left';
			divs.width = parseInt(minuteOpts.butoonWidth) + 'px';
			divs.height = divs.lineHeight = parseInt(minuteOpts.butoonHeight) + 'px';
			divs.margin = parseInt(minuteOpts.butoonRowSpace) + 'px 0 0 ' + parseInt(minuteOpts.butoonColSpace) +'px';
			divs.border = parseInt(minuteOpts.butoonBorderWidth) + 'px solid '+ minuteOpts.butoonBorderColor;
			divs.background = minuteOpts.butoonBackground;
			divs.fontSize = parseInt(minuteOpts.butoonFontSize) + 'px'; 
			divs.textAlign = 'center';
			divs.cursor = 'pointer';
			this.minutes[i].addEventListener('mouseover',function(){
				this.style.background = minuteOpts.buttonHoverBack;
			});
			this.minutes[i].addEventListener('mouseout',function(){
				this.style.background = minuteOpts.butoonBackground;
			});
		}
		
	
	};

	HourComponent.prototype.minuteShow = function(){
		this.minuteBox.style.display = 'block';
	};
	HourComponent.prototype.minuteHide = function(){
		this.minuteBox.style.display = 'none';
	};

	HourComponent.prototype.addEL = function(){
		var _this = this;
		for(var i=0;i<24;i++){
			(function(index){
				_this.hours[index].addEventListener('click',function(){
					_this.dateBox.dateTime.setDateTime({
						hour: Number(this.innerHTML)
					});
					if(_this.dateBox.opts.type == 'h-m'){
						_this.dateBox.setFooter(_this.dateBox.dateTime.toString('h-m'));	
					}else{
						_this.dateBox.setFooter(_this.dateBox.dateTime.toString('y-m'));						
					}
					_this.minuteBox.style.left = this.offsetLeft + _this.opts.minuteStyle.reLeft + 'px';
					_this.minuteBox.style.top = this.offsetTop + _this.opts.minuteStyle.reTop + 'px';
					_this.minuteShow();
				});
			})(i);
		};
		for(var i=0;i<12;i++){
			(function(index){
				_this.minutes[index].addEventListener('click',function(){
					_this.dateBox.dateTime.setDateTime({
						minute: Number(this.innerHTML)
					});
					if(_this.dateBox.opts.type == 'h-m'){
						_this.dateBox.setFooter(_this.dateBox.dateTime.toString('h-m'));	
					}else{
						_this.dateBox.setFooter(_this.dateBox.dateTime.toString('y-m'));						
					}
					_this.dateBox.initCS();
					_this.dateBox.inputTime();
				});
			})(i);
		};
	};
	

	return HourComponent;
});
