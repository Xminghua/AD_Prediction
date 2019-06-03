//获取当前时间
function today(){
	var today=new Date();//new 出当前时间
    var h=today.getFullYear();//获取年
    var m=today.getMonth()+1;//获取月
    var d=today.getDate();//获取日
    var H = today.getHours();//获取时
    var M = today.getMinutes();//获取分
    return h+"-"+m+"-"+d+" "+H+":"+M; //返回 年-月-日 时:分:秒
}

//获取修改的出生日期，并验证出生日期的正确性
function Check_BirthTime(id){
	var Birth_time = document.getElementById(id).value;
	var Now_time = today();
	var date1 = new Date(Birth_time);
	var date2 = new Date(Now_time);
	if(date1.getTime() > date2.getTime()){
		alert("出生日期选择错误，请重新选择！");
		document.getElementById(id).value = "";
	}
}


function Reset(){
	document.getElementById("name").value = "";
	document.getElementById("phone").value = "";
	document.getElementById("dateBox4").value = "";
	document.getElementById("pwd1").value = "";
	document.getElementById("pwd2").value = "";
}

$("radios").removeAttr("checked");
