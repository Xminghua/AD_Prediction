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
document.getElementById("upload_time").value = today();

//获取MRI拍摄时间，并验证拍摄时间的正确性
function check_time(id){
	var Shoot_time = document.getElementById(id).value;
	var Upload_time = document.getElementById("upload_time").value;
	var date1 = new Date(Shoot_time);
	var date2 = new Date(Upload_time);
//	if(Shoot_time == ""){
//		alert("请选择MRI拍摄时间！");
//		document.getElementById(id).value = "";
//	}
	if(date1.getTime() > date2.getTime()){
		alert("MRI拍摄时间填写有误，请重新填写！");
		document.getElementById(id).value = "";
	}
}


function check_all(){
	var mri_name = document.getElementById("MRI_Name").value;
	var upload_time = document.getElementById("upload_time").value;
	var shoot_time = document.getElementById("dateBox4").value;
	if(mri_name == ""  || upload_time == "" || shoot_time == ""){
		alert("未填写完整，请按要求填写完成后再上传！");
		return false;
	}
}
