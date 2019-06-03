//重置
$(document).ready(function(){
  $("#reset").click(function(){
$("#username").val("");
$("#password").val("");
  });
});
//选择用户类型
$(document).ready(function(){
	$(":radio").click(function(){
		var text = $("input[name='radioname']:checked").val();
		$("#user").html('用户类型:&nbsp;' + '<u id="user_type">' + text + '</u>');
	});
});
function setCookie(c_name,value,expiredays)
{
var exdate=new Date()
exdate.setDate(exdate.getDate()+expiredays)
document.cookie=c_name+ "=" +escape(value)+
((expiredays==null) ? "" : ";expires="+exdate.toGMTString())
}

function getCookie(c_name)
{
if (document.cookie.length>0)
  {
  c_start=document.cookie.indexOf(c_name + "=")
  if (c_start!=-1)
    { 
    c_start=c_start + c_name.length+1 
    c_end=document.cookie.indexOf(";",c_start)
    if (c_end==-1) c_end=document.cookie.length
    return unescape(document.cookie.substring(c_start,c_end))
    } 
  }
}


//登录验证
$(document).ready(function(){
	$("#login").click(function(event) {
		var name = $("#username").val();
		var pwd = $("#password").val();
		if(name=="")
		{
		   alert("用户名不能为空！");
		}
		else if(pwd=="")
		{
		   alert("密码不能为空！");
		}
		else if(pwd!="" && pwd.length < 6){
			alert("密码不能小于6位！");
		}
		else if(name!="" && pwd !="" && pwd.length >= 6)
		{
			var user = $("input[type='radio']:checked").val();
			var type = 0;
			if(user == "学生"){
				type = 0;
			}
			else if(user == "实习指导老师"){
				type = 1;
			}
			else if(user == "项目负责人"){
				type = 2;
			}
	
			var data = {
					"user":name,
					"pwd":pwd,
					"type":type
			};

		$.post("/practice_system/logintest",data,function(data, textStatus, xhr)
		{

			if(textStatus=="success")
			{
				if(data[0]["returnflag"]=="1")
				{
					setCookie("user",name,1);
					setCookie("SESSIONID",data[0]["SESSIONID"],1);
					setCookie("type",type,1);
					switch (type) {
						case 0:   
							window.location = "practice_system/html/StudentIndex.html";
							break;
						case 1:
							
							window.location = "practice_system/html/TeacherIndex.html";
							break;
						case 2:
							
							window.location = "practice_system/html/ProjectorIndex.html";
							break;
						default:
							alert("未知错误!");
							// statements_def
							break;
					}
				}
				else
				{
					alert("用户名或密码错误！");
				}
			}
			else
			{
				alert("服务器错误！");
			}
		});

		}
	});
});