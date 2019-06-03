//登录用户类型选择
$(document).ready(function(){
	$(":radio").click(function(){
		var user = $("input[name='radioname']:checked").val();
		if(user == "专家用户" || user == "管理员"){
			$("#Register").hide();
		}
		else if(user == "普通用户"){
			$("#Register").show();
		}
	});
});



// function check_login(){
// 	var name = $("#username").val();
// 		var pwd = $("#password").val();
// 		if(name != "" && pwd != ""){
// 			var user = $("input[type='radio']:checked").val();
// 			alert(user);
// 			var type = 0;
// 			if(user == "普通用户"){
// 				type = 0;
// 			}
// 			else if(user == "专家用户"){
// 				type = 1;
// 			}
// 			else if(user == "管理员"){
// 				type = 2;
// 			}
// 			var data = {
// 				data:JSON.stringify({
// 					"user":name,
// 					"pwd":pwd,
// 					"type":type
// 				}),
// 			}
// 			$.ajax({
// 				url:"/login",
// 				type:'post',
// 				data:data,
// 				dataType:'json',
// 				success:function(data){
// 					alert("登录成功");
// 					window.location = "/index";
//
// 				},
// 				error:function(e){
// 					alert("用户名或密码错误");
// 				}
// 			})
// 		}
// }


