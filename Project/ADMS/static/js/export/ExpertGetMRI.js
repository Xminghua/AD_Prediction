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
document.getElementById("feedback_time").value = today();
