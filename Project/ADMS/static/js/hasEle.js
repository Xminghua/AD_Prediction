/**
 * create by zhaomingqiang
 * 
 * 2017.12.26
 * 确定一个元素里是否包含另一个元素的方法
 */

;define(function(){
	
	var hasEle = function(parent,child){
		
		var result = false;
		
		var childs = parent.getElementsByTagName('*');
		var length = childs.length;
		for(var i=0;i<length;i++){
			if(childs[i] == child){
				result = true;
				break;
			}
		}
		
		return result;
		
	};
	
	return hasEle;
	
});
