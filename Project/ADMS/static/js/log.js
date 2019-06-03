
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
      return unescape(document.cookie.substring(c_start,c_end));
    } 
  }
  
}
var totalpage=0;
function TeacherLogR(pageno)
{

    var tid = getCookie("user");
    data = {"id":tid,"type":"1","pageno":pageno};
    $.post('/practice_system/diary_search', data, function(data, textStatus, xhr) {
      if(textStatus=="success")
      {
        var total = data[0]["page_total_number"];
        totalpage = total;
        var page= ''
          for(var i=1;i<=total;i++)
          {
            if(i==pageno)
            {
              page += '<a tabindex="0" class="fg-button ui-button ui-state-default ui-state-disabled">'+i+'</a>';
            }
            else
            {
              page += '<a tabindex="0" class="fg-button ui-button ui-state-default ">'+i+'</a>';
            } 
          }
          
          $("#page").html(page);
        var html = '';
        for(var i = 1;data[i]!=null;i++)
        {
          html += '<tr><td>'+data[i]["sid"]+'</td><td>'+data[i]["sname"]+'</td><td>'+data[i]["sproject"]+'</td><td><button  class="btn btn-primary" onclick="check_log('+data[i]["sid"]+')">查看</button></td></tr>';
        }
        $("#stulog").empty();
        $("#stulog").html(html);
      }
         
      else
      {
        alert("发生未知错误！");
      }
    });
  

}
$(document).ready(function() {
  check_login(1,TeacherLogR);
});

function check_log(sid)
{
  window.location.href = "../html/TeacherLogCheck.html?sid="+sid; 
}

$("#DataTables_Table_0_previous").click(function(event) {
  var current_page = $(".ui-state-disabled").text();
  if(current_page!=1 && current_page!="")
  {
    current_page--;
    check_login(current_page,TeacherLogR);
  }
});
$("#DataTables_Table_0_next").click(function(event) {
  var current_page = $(".ui-state-disabled").text();
  if(current_page!=totalpage && current_page!="")
  {
    current_page++;
    check_login(current_page,TeacherLogR);

  }
});
$("#DataTables_Table_0_last").click(function(event) {
  var current_page = $(".ui-state-disabled").text();
  if(current_page!=totalpage && current_page!="")
  {
    check_login(totalpage,TeacherLogR);

  }
});
$("#DataTables_Table_0_first").click(function(event) {
 var current_page = $(".ui-state-disabled").text();
  if(current_page!=1 && current_page!="")
  {

    check_login(1,TeacherLogR);

  }
});
