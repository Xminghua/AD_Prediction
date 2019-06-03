document.getElementById("salary_1").style.display = "none";
document.getElementById("salary_2").style.display = "none";
document.getElementById("salary_3").style.display = "none";
document.getElementById("salary_4").style.display = "none";

function check_identity(iden){
	if(iden == "请选择专家身份"){
		alert("请选择专家身份！");
		document.getElementById("salary_1").style.display = "none";
		document.getElementById("salary_2").style.display = "none";
		document.getElementById("salary_3").style.display = "none";
		document.getElementById("salary_4").style.display = "none";
	}
	else if(iden == "三级专家"){
		document.getElementById("salary_1").style.display = "block";
		document.getElementById("salary_2").style.display = "block";
		document.getElementById("salary_3").style.display = "none";
		document.getElementById("salary_4").style.display = "none";
	}
	else if(iden == "二级专家"){
		document.getElementById("salary_1").style.display = "block";
		document.getElementById("salary_2").style.display = "block";
		document.getElementById("salary_3").style.display = "block";
		document.getElementById("salary_4").style.display = "none";
	}
	else if(iden == "一级专家"){
		document.getElementById("salary_1").style.display = "block";
		document.getElementById("salary_2").style.display = "block";
		document.getElementById("salary_3").style.display = "block";
		document.getElementById("salary_4").style.display = "block";
	}
}

function check_salary(salary){
	if(salary == "请选择年薪"){
		alert("请选择年薪！");
	}
}

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
//将当前赋值给上传时间
document.getElementById("japply_time").value = today();