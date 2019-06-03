//验证注册用户名输入规范
//执行一个laydate实例，调用日期插件
laydate.render({
	elem:'#Age'
})


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

//验证用户名规范
function VerifyUserID(ID){
	document.getElementById("p1").style.display = "none";
	if(ID.length == 0){
		document.getElementById("p1").innerHTML = '用户名不能为空';
		document.getElementById("p1").style.display = "block";
	}
	else if(ID.length < 6 || ID.length > 30){
		document.getElementById("p1").innerHTML = '用户名长度为6-30位';
		document.getElementById("p1").style.display = "block";
	}
	else if(/^\d+$/.test(ID) || /^[a-zA-Z]+$/i.test(ID)){
		document.getElementById("p1").style.display = "none";
	}
	else{
		document.getElementById("p1").innerHTML = '6-30位数字或英文字母（区分大小写）';
		document.getElementById("p1").style.display = "block";
	}
}
//验证注册密码输入规范
function VerifyPwd_1(PWD){
	if(PWD.length == 0){
		document.getElementById("p2_1").innerHTML = '密码不能为空';
		document.getElementById("p2_1").style.display = "block";
	}
	else if(PWD.length < 6 || PWD.length > 30){
		document.getElementById("p2_1").innerHTML = '密码长度为6-30位';
		document.getElementById("p2_1").style.display = "block";
	}
	else if(/^\d+$/.test(PWD)){
		document.getElementById("p2_1").innerHTML = '密码必须包含字母，强度：弱';
		document.getElementById("p2_1").style.display = "block";
	}
	else if(/^[a-zA-Z]+$/i.test(PWD)){
		document.getElementById("p2_1").innerHTML = '密码必须包含数字，强度：中';
		document.getElementById("p2_1").style.display = "block";
	}
	else if(!/^[A-Za-z0-9]+$/.test(PWD)){
		document.getElementById("p2_1").innerHTML = '密码只能包含数字和字母，强度：强';
		document.getElementById("p2_1").style.display = "block";
	}
	else{
		document.getElementById("p2_1").style.display = "none";
	}
}

//验证重复密码规范
function VerifyPwd_2(PWD){
	var pwd1 = document.getElementById("PWD1").value;
	if(PWD.length == 0){
		document.getElementById("p2_2").innerHTML = '确认密码不能为空';
		document.getElementById("p2_2").style.display = "block";
	}
	else if(pwd1 != PWD){
		document.getElementById("p2_2").innerHTML = '两次输入密码不一致，请重新输入！';
		document.getElementById("p2_2").style.display = "block";
	}
	else{
		document.getElementById("p2_2").style.display = "none";
	}
}

//验证输入姓名规范
function VerifyUserName(UserName){
	if(UserName.length == 0){
		document.getElementById("p3").innerHTML = '姓名不能为空';
		document.getElementById("p3").style.display = "block";
	}
	else if(/^[a-zA-Z]+$/i.test(UserName) || /^[\u2E80-\u9FFF]+$/.test(UserName)){
		document.getElementById("p3").style.display = "none";
	}
	else if(UserName.length > 100){
		document.getElementById("p3").innerHTML = '姓名长度不能大于100位';
		document.getElementById("p3").style.display = "block";
	}
	else{
		document.getElementById("p3").innerHTML = '姓名只能为汉字或字母，请重新输入';
		document.getElementById("p3").style.display = "block";
	}
}

//验证输入性别规范
function VerifySex(Sex){
	if(Sex.length == 0){
		document.getElementById("p4").innerHTML = '性别不能为空';
		document.getElementById("p4").style.display = "block";
	}
	else if(Sex == "男" || Sex == "女"){
		document.getElementById("p4").style.display = "none";
	}
	else{
		document.getElementById("p4").innerHTML = '性别输入有误，请从下拉框中进行选择';
		document.getElementById("p4").style.display = "block";
	}
}

//获取修改的出生日期，并验证出生日期的正确性
function Check_BirthTime(id){
	var Birth_time = document.getElementById(id).value;
	var Now_time = today();
	var date1 = new Date(Birth_time);
	var date2 = new Date(Now_time);
	if(Birth_time.length == 0){
		document.getElementById("p5").innerHTML = '出生日期不能为空';
		document.getElementById("p5").style.display = "block";
	}
	else if(date1.getTime() > date2.getTime()){
		document.getElementById("p5").innerHTML = '出生日期选择错误，请重新选择！';
		document.getElementById("p5").style.display = "block";
		document.getElementById(id).value = "";
	}
	else{
		document.getElementById("p5").style.display = "none";
	}
	
	
}

//验证输入电话号码规范
function VerifyPhone(Phone){
	var myreg = /^(((13[0-9]{1})|(14[0-9]{1})|(17[0-9]{1})|(15[0-3]{1})|(15[4-9]{1})|(18[0-9]{1})|(199))+\d{8})$/;
	if(Phone.length == 0){
		document.getElementById("p6").innerHTML = '电话号码不能为空';
		document.getElementById("p6").style.display = "block";
	}
	else if(Phone.length != 11){
		document.getElementById("p6").innerHTML = '请输入11位手机号码';
		document.getElementById("p6").style.display = "block";
	}
	else if(!myreg.test(Phone)){
		document.getElementById("p6").innerHTML = '请输入有效的手机号码';
		document.getElementById("p6").style.display = "block";
	}
	else{
		document.getElementById("p6").style.display = "none";
	}
}

//检查函数
function check() {
	var ckh_result = true;
	var UserID = document.getElementById("UserID").value;
	var PWD1 = document.getElementById("PWD1").value;
	var PWD2 = document.getElementById("PWD2").value;
	var UserName = document.getElementById("UserName").value;
	var Sex = document.getElementById("Sex").value;
	var Age = document.getElementById("Age").value;
	var Phone = document.getElementById("Phone").value;
	var check = document.getElementById("Accept").checked;
	
	if(UserID == '' || PWD1 == '' || PWD2 == '' || UserName == '' || Sex == '' || Age == '' || Phone == '' || check == false){
		alert("您的注册信息未填写完整，请补充完整！");
		if(UserID.length == 0) {
		document.getElementById("p1").innerHTML = '用户名输入不能为空';
		document.getElementById("p1").style.display = "block";
		}
		if(PWD1.length == 0) {
			document.getElementById("p2_1").innerHTML = '第一次密码输入不能为空';
			document.getElementById("p2_1").style.display = "block";
		}
		if(PWD2.length == 0) {
			document.getElementById("p2_2").innerHTML = '第二次密码输入不能为空';
			document.getElementById("p2_2").style.display = "block";
		}
		if(UserName.length == 0){
			document.getElementById("p3").innerHTML = '姓名不能为空';
			document.getElementById("p3").style.display = "block";
		}
		if(Sex.length == 0){
			document.getElementById("p4").innerHTML = '性别不能为空';
			document.getElementById("p4").style.display = "block";
		}
		if(Age.length == 0){
			document.getElementById("p5").innerHTML = '出生日期不能为空';
			document.getElementById("p5").style.display = "block";
		}
		if(Phone.length == 0){
			document.getElementById("p6").innerHTML = '电话号码不能为空';
			document.getElementById("p6").style.display = "block";
		}
		if(check == false){
			document.getElementById("p7").innerHTML = '请勾选准则，表示同意平台规则';
			document.getElementById("p7").style.display = "block";
	}
			ckh_result = false;
	}
	else{
		document.getElementById("p1").style.display = "none";
		document.getElementById("p2_1").style.display = "none";
		document.getElementById("p2_2").style.display = "none";
		document.getElementById("p3").style.display = "none";
		document.getElementById("p4").style.display = "none";
		document.getElementById("p5").style.display = "none";
		document.getElementById("p6").style.display = "none";
		document.getElementById("p7").style.display = "none";
		ckh_result = true;
	}
	return ckh_result;
}
