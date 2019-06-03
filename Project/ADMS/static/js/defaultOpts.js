/**
 * create by zhaomingqiang 2017.12.28
 * 
 * DateBox 插件的默认配置项
 */

;define({
	
	
	type:'y-m',	//日期类型 'y-d':年月日，'M'：月日， y-m:年月日时分，h-m:时分, 
	minDate:'1990-1-1', //2018.2.7 添加配置项，最小日期,格式为 yyyy-mm-dd 不支持时分
	maxDate:'today', //2018.3.19添加配置项，最大日期,格式为 yyyy-mm-dd 不支持时分
	
	//时间设置
	/*
	date:{
		year:2017,		//默认年
		month:12,		//默认月
		date:25,		//默认日
		hour:12,		//默认小时
		minute:0		//默认分钟
	},
	*/
	//盒子样式
	boxStyle:{
		//width:224,					//盒子宽度
		//height:187,					//盒子高度 (尽量是 内容高度+底部分割线宽度+底部信息框高度)
		borderWidth:1,				//盒子边线宽度
		borderColor:'#828790',			//盒子边线颜色
		backgroundColor:'#fff',		//盒子背景颜色
		
		//containerHeight:165,			//内容高度
		
		footerHeight:21,			//底部信息框高度
		footerBackground:'#fff',	//底部信息框背景色
		footerFontSize:12,			//底部字体大小
		footerFontColor:'#000',		//底部字体颜色
		footerSegLineWidth:1,		//底部分割线宽度
		footerSegLineColor:'#d0d0d0'	//底部分割线颜色		
	},
	
	// 选择月份窗口的样式
	monthComponentStyle:{
		width:224,				//选择月份窗口宽度
		height:165,				//选择月份窗口高度
		
		monthButoonFontSize:12,	//选择月份按钮字体大小
		monthButoonWidth:45,	//选择月份按钮宽度
		monthButoonHeight:32,	//选择月份按钮高度
		monthButoonRowSpace:10,	//选择月份按钮行间距
		monthButoonColSpace:7,	//选择月份按钮列间距
		monthButoonBorderWidth:1,			//选择月份按钮边线宽度
		monthButoonBorderColor:'#c3c3c3',	//选择月份按钮边线颜色
		monthButoonBackground:'#f9f9f9',	//选择月份按钮背景颜色
		monthButtonHoverBack:'#e6e6e6',		//选择月份按钮鼠标移动到上面的背景颜色
		
		titStyle:{
			height:21,			//高度
			fontSize:12,		//字体大小
			arrowIdent:10,		//箭头距两侧的距离
			segLineWidth:1,		//下方分割线宽度
			segLineColor:'#d0d0d0',	//下方分割线颜色
			showArrow:true,			//是否显示箭头
			text:'标题信息'			//默认标题信息
		}		
	},
	
	//选择日期窗口样式
	dateComponentStyle:{
		width:198,				//选择日期窗口宽度
		//height:197,				//选择日期窗口高度

		
		dateButoonFontSize:12,	//选择日期按钮字体大小
		dateButoonWidth:28,		//选择日期按钮宽度
		dateButoonHeight:25,	//选择日期按钮高度
		weekTitBackground:'#ccc',
		weekTitBackground:'#f8f8f8',		//工作日标题背景颜色
		dateButtonBackground:'#fff',		//选择日期按钮背景颜色
		dateButtonHoverBack:'#e6e6e6',		//选择日期按钮鼠标移动到上面的背景颜色
		
		titStyle:{
			height:21,			//高度
			fontSize:12,		//字体大小
			arrowIdent:10,		//箭头距两侧的距离
			segLineWidth:1,		//下方分割线宽度
			segLineColor:'#d0d0d0',	//下方分割线颜色
			showArrow:true,			//是否显示箭头
			text:'标题信息'			//默认标题信息
		}
		
	},
	
	//选择小时窗口样式
	hourComponentStyle:{
		width:226,				//选择小时窗口宽度
		height:197,				//选择小时窗口高度
		leftSegLineColor:'#828790',	//左侧分割线颜色
		leftSegLineWidth:1,		//左侧分割线宽度
		
		titleInner:'小时',		//内标题内容
		titleHeight:21,			//内标题高度
		titleFontSize:12,		//内标题文字大小
		titleTextIndent:8,		//内标题文字缩进距离
		
		hourButoonFontSize:12,	//选择小时按钮字体大小
		hourButoonWidth:31,		//选择小时按钮宽度
		hourButoonHeight:32,	//选择小时按钮高度
		hourButoonRowSpace:4,	//选择小时按钮行间距
		hourButoonColSpace:4,	//选择小时按钮列间距
		hourButoonBorderWidth:1,			//选择小时按钮边线宽度
		hourButoonBorderColor:'#c3c3c3',	//选择小时按钮边线颜色
		hourButoonBackground:'#f9f9f9',		//选择小时按钮背景颜色
		hourButtonHoverBack:'#e6e6e6',		//选择小时按钮鼠标移动到上面的背景颜色
		
		
		minuteStyle:{
		
			width:226,				//选择分钟窗口宽度
			height:99,				//选择分钟窗口高度
			padding:7,				//容器内边距
			background:'#fff',		//选择分钟窗口背景颜色
			borderColor:'#828790',	//选择分钟窗口边线颜色
			borderWidth:1,			//选择分钟窗口边线宽度
			reLeft:25,				//分钟窗口对应小时按钮的左方距离
			reTop:25,				//分钟窗口对应小时按钮的上方距离
		
			titleInner:'分钟',		//内标题内容
			titleHeight:21,			//内标题高度
			titleFontSize:12,		//内标题文字大小
			titleTextIndent:8,		//内标题文字缩进距离
			
			butoonFontSize:12,	//选择分钟按钮字体大小
			butoonWidth:31,		//选择分钟按钮宽度
			butoonHeight:32,		//选择分钟按钮高度
			butoonRowSpace:4,		//选择分钟按钮行间距
			butoonColSpace:4,		//选择分钟按钮列间距
			butoonBorderWidth:1,			//选择分钟按钮边线宽度
			butoonBorderColor:'#c3c3c3',	//选择分钟按钮边线颜色
			butoonBackground:'#f9f9f9',	//选择分钟按钮背景颜色
			buttonHoverBack:'#e6e6e6',	//选择分钟按钮鼠标移动到上面的背景颜色
		},			
		
		
		
		
		titStyle:{
			height:21,			//高度
			fontSize:12,		//字体大小
			arrowIdent:10,		//箭头距两侧的距离
			segLineWidth:1,		//下方分割线宽度
			segLineColor:'#d0d0d0',	//下方分割线颜色
			showArrow:false,		//是否显示箭头
			text:'标题信息'			//默认标题信息
		}
		
	}

		
	
	
	
	
});