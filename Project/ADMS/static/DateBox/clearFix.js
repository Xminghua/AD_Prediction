/**
 * create by zhaomingqiang 2012.12.27
 * 
 * 用于给DOM元素清浮动的js方法
 */

;define(function(){
	
	var clearFix = function(obj){
		var div = document.createElement('div');
		
		var ds = div.style;
		ds.height = ds.lineHeight = ds.fontSize = 0;
		ds.clear = 'both';
		
		obj.appendChild(div);
		
		//obj.innerHTML += '<div style="height:0;line-height:0;font-size:0;clear:both;"></div>';
		
	};
	
	return clearFix
	
});
