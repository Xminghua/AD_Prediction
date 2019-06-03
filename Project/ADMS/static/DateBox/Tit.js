/**
 * create by zhaomingqiang 2017.12.25
 * 
 * 日历的标题
 */

;define([
	'../DateBox/extend'
],function(
	extend
){
	var Tit = function(opts){
		var obj = this.obj = document.createElement('div');
		
		
		var opts = this.opts = extend(opts||{},{
			height:21,			//高度
			fontSize:12,		//字体大小
			arrowIdent:10,		//箭头距两侧的距离
			segLineWidth:1,		//下方分割线宽度
			segLineColor:'#d0d0d0',	//下方分割线颜色
			showArrow:true,			//是否显示箭头
			text:'标题信息'			//默认标题信息
		});
		
		
		this.initDOM();
		this.initStyle();
	};
	
	Tit.prototype.initDOM = function(){
		var arrowLeft = this.arrowLeft = document.createElement('div');
			arrowLeft.innerHTML = '&lt;'
		var arrowRight = this.arrowRight = document.createElement('div');
			arrowRight.innerHTML = '&gt;'
		var info = this.info = document.createElement('div');
		this.obj.appendChild(arrowLeft);
		this.obj.appendChild(arrowRight);
		this.obj.appendChild(info);
		this.setText(this.opts.text);
	};

	Tit.prototype.setText = function(str){
		this.info.innerHTML = str;
	};
	
	Tit.prototype.initStyle = function(){
		var os = this.obj.style;
		os.position = 'relative';
		os.borderBottom = parseInt(this.opts.segLineWidth) + 'px solid '+this.opts.segLineColor;
		
		var als = this.arrowLeft.style;
		
		var ars = this.arrowRight.style;
		
		var is = this.info.style;
		is.textAlign = 'center';
		is.fontSize = parseInt(this.opts.fontSize) + 'px';
		
		als.position = ars.position = 'absolute';
		als.top = ars.top = '0';
		als.left = ars.right = parseInt(this.opts.arrowIdent) + 'px';
		als.cursor = ars.cursor = 'pointer';
		als.display = ars.display = this.opts.showArrow?'block':'none';
		als.height = ars.height = is.height = os.height = parseInt(this.opts.height)+'px';
		als.lineHeight = ars.lineHeight = is.lineHeight = parseInt(this.opts.height)+'px';
		
	};
	
	
	
	Tit.prototype.addEL = function(json){
		var json = json||{};
		this.arrowLeft.addEventListener('click',function(){
			json.left&&json.left();
		});
		this.arrowRight.addEventListener('click',function(){
			json.right&&json.right();
		});
	};

	return Tit;
});
