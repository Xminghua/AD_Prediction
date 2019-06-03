## AD_Prediction
毕业设计项目-基于深度学习的阿兹海默症早期诊断辅助系统设计与实现
## 系统启动说明
  1，打开Pycharm，导入该项目，并安装Tensorflow、keras、Flask等需要的包（命令行安装）；
	2，运行ADMS项目下的app.py文件，运行成功后，会出现一个URL，点击或复制到浏览器中打开，并可自动跳转到系统登录首页。
	3，ADMS/app文件夹下：
		create_db.py：增删改查表命令
		models.py：创建数据库表项
		views.py：在该项目中暂时没有用
		ExpertPush.py：导入专家用户信息
	4，ADMS/Model文件夹：
		放置的是训练好的模型，需要进行联合预测的两种模型
	5，ADMS/Pred文件夹：
		HipvoluSum.py：获得预测得到的标签文件中的海马体体积
		ImagCrop..py：对用户输入的图像进行分割
		SinglePrediction.py：对单张图片通过加载模型进行预测，并得到预测标签文件
	6，ADMS/static文件夹：
		放置的是Web系统所需要的css、js以及用户上传图像、预测图像以及上传的诊断结果保存目录
	7，ADMS/templates文件夹：
		放置的是Web系统的前端HTML页面
		
## 关于具体的如何使用基于Flask搭建Web系统可以参考一下链接中的内容：
  1，如何利用Flask框架实现注册登录功能：https://blog.csdn.net/m0_37997046/article/details/86304398
  2，Flask配置数据库：https://blog.csdn.net/qq_33196814/article/details/80866094
  3，Flask实现如何将后端的HTML代码在前端中正常显示出来：http://www.codes51.com/itwd/1091263.html
  4，Flask数据库基本操作：https://blog.csdn.net/weixin_41782050/article/details/80347661
  5，注意下static下的DateBox日期控件的使用
