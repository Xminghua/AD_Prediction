/**
 * create by zhaomingqiang 2017.12.25
 * 月份对象
 */

;define([
	'../DateBox/extend',
	'../DateBox/Tit'
],function(
	extend,
	Tit
){
	
	var MonthComponent = function(dateBox,opts){
		
		var box = this.box = document.createElement('div');
		dateBox.container.appendChild(box);
		this.dateBox = dateBox;
		
		
		var opts = this.opts = extend(opts||{},{
			width:224,				//选择月份窗口宽度
			height:165,				//选择月份窗口高度
			
			monthButoonFontSize:12,	//选择月份按钮字体大小
			monthButoonWidth:45,	//选择月份按钮宽度
			monthButoonHeight:32,	//选择月份按钮高度
			monthButoonRowSpace:10,	//选择月份按钮行间距
			monthButoonColSpace:7,	//选择月份按钮列间距
			monthButoonBorderWidth:1,			//选择月份按钮边线宽度
			monthButoonBorderColor:'#c3c3c3',	//选择月份按钮边线颜色
			monthButoonBackground:'#f9f9f9',	//选择月份按钮背景颜色
			monthButtonHoverBack:'#e6e6e6',		//选择月份按钮鼠标移动到上面的背景颜色
			
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
	
	MonthComponent.prototype.addTit = function(){
		var opts = this.opts.titStyle;
		var _this = this;

		var tit = this.tit = new Tit(opts);
		tit.addEL({
			left:function(){
				_this.dateBox.dateTime.plusYear(-1);
			},
			right:function(){
				_this.dateBox.dateTime.plusYear();
			}
		});
		
		this.box.appendChild(tit.obj);
	};
	
	MonthComponent.prototype.update = function(date){
		this.tit.setText(date.year);
	};
	
	MonthComponent.prototype.initDOM = function(){
		this.box.innerHTML='';
		this.addTit();
		var con = this.con = document.createElement('div');
		this.box.appendChild(con);
		
		var months = this.months = [];
		var monthStr =['一月','二月','三月','四月','五月','六月','七月','八月','九月','十月','十一月','十二月'];
		for(var i=1;i<13;i++){
			var div = document.createElement('div');
			div.innerHTML = monthStr[i-1];
			div.index = i;
			con.appendChild(div);
			months.push(div);
		};
		
	};
	
	MonthComponent.prototype.show = function(){
		this.box.style.display = 'block';
	};

	MonthComponent.prototype.hide = function(){
		this.box.style.display = 'none';
	};

	MonthComponent.prototype.initStyle = function(){
		var _this = this;
		
		var bs = this.box.style;
		bs.float = 'left';
		bs.width = parseInt(this.opts.width) + 'px';
		bs.height = parseInt(this.opts.height) + 'px';
		
		var cs = this.con.style;
		cs.overflow = 'hidden';
		
		for(var i=1;i<13;i++){
			var divs = this.months[i-1].style;
			divs.float = 'left';
			divs.width = parseInt(this.opts.monthButoonWidth) + 'px';
			divs.height = divs.lineHeight = parseInt(this.opts.monthButoonHeight) + 'px';
			divs.margin = parseInt(this.opts.monthButoonRowSpace) + 'px 0 0 ' + parseInt(this.opts.monthButoonColSpace) +'px';
			divs.border = parseInt(this.opts.monthButoonBorderWidth) + 'px solid '+ this.opts.monthButoonBorderColor;
			divs.background = this.opts.monthButoonBackground;
			divs.fontSize = parseInt(this.opts.monthButoonFontSize) + 'px'; 
			divs.textAlign = 'center';
			divs.cursor = 'pointer';
			this.months[i-1].addEventListener('mouseover',function(){
				this.style.background = _this.opts.monthButtonHoverBack;
			});
			this.months[i-1].addEventListener('mouseout',function(){
				this.style.background = _this.opts.monthButoonBackground;
			});
		};
		
	};

	MonthComponent.prototype.addEL = function(){
		var _this = this;
		for(var i=1;i<13;i++){
			(function(index){
				_this.months[index-1].addEventListener('click',function(){
					_this.dateBox.dateTime.setDateTime({
						month:index
					});
					_this.dateBox.setFooter('today');
					_this.hide();
					if(_this.dateBox.dateComponent){
						_this.dateBox.dateComponent.show();
					}else{
						_this.dateBox.initCS();
						_this.dateBox.inputTime();
					}					
				});
			})(i);
		};
		
	};


	return MonthComponent;
});
