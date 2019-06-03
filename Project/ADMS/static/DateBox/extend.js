/**
 * create by zhaomingqiang 2017.12.11
 * 
 * 用于将两个json合并的工具。通常用于参数处理，后者填写默认值
 * 
 * 
 */


define(function(){
	
	var extend = function(opts,defau){

		var result = {};
		
		for(var name in opts){
			result[name] = opts[name];
		}
		
		for(var name in defau){
			
			
			if(typeof result[name] == 'undefined'){
				result[name] = defau[name];
			}else if(result[name].toString() == '[object Object]'){				
				result[name] = extend(result[name],defau[name]);				
			}
				
			
		}
		
		return result;
	};
	
	return extend;
	
});
