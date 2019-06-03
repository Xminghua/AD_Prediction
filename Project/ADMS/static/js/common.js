// 通用进行session验证的js

function getCookie(cookieName) {
    var strCookie = document.cookie;
    var arrCookie = strCookie.split("; ");
    for(var i = 0; i < arrCookie.length; i++){
        var arr = arrCookie[i].split("=");
        if(cookieName == arr[0]){
            return arr[1];
        }
    }
    return "";
}
function illegalUser()
{
	var html = '<div class="row-fluid"><div class="span12"><div class="widget-box"><div class="widget-title"> <span class="icon"> <i class="icon-briefcase"></i> </span><h5 >非法用户</h5></div><div class="widget-content"><div class="row-fluid"><div class="span6"><a href="http://localhost:8080/practice_system/"><h3>请先登录！</h3></a></div></div></div></div></div></div>';
	$(".container-fluid").html(html);

}
function check_login(value,Func) {
	
	if(getCookie("user")=="" || getCookie("SESSIONID")=="")
	{
		illegalUser();
	}
	else
	{
	
		$.post('/practice_system/session_send',{},function(data, textStatus, xhr) {
			/*optional stuff to do after success */
			var data = $.parseJSON(data);
			if(textStatus=="success")
			{
	
				var sessionid = data[0]["SESSIONID"];
				var user = data[0]["user"];
				var type = data[0]["type"];
				if(getCookie("user")==user && getCookie("SESSIONID")==sessionid &&getCookie("type")==type)
				{
					
					Func(value);
				}
				else
				{
					illegalUser();
				}
					
				
			}
			else
			{
				illegalUser();
			}
		});
		
	}
}
	
