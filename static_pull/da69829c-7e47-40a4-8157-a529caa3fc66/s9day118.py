s9day118 

内容回顾：
	1.flask功能：
		- 路由
		- 视图
		- 蓝图
		...
	2. 请求上下文管理（ctx）：request，session 
		- 请求到来之后wsgi会触发__call__方法，由__call__方法再次调用wsgi_app方法
		- 在wsgi_app方法中：
			- 首先将 请求相关+空session 封装到一个RequestContext对象中，即：ctx。
			- 将ctx交给LocalStack对象，再由LocalStack将ctx添加到Local中，Local结构：
				__storage__ = {
					1231:{stack:[ctx,] }
				}
			- 根据请求中的cookie中提取名称为sessionid对应的值，对cookie进行加密+反序列化，再次赋值给ctx中的session
			
			-> 视图函数
			
			- 把session中的数据再次写入到cookie中。
			- 将ctx删除
		- 结果返回给用户浏览器
		- 断开socket连接

	3. 什么是偏函数？以及应用场景？
	
	4. 面向对象中双下线的个数方法：
		init
		str
		repr
		
		new，单例/rest framework序列化
		call，flask源码请求入口，django请求入口（WSGIHandler.__call__）。
		getattr
		setattr
		delattr，flask Local对象
		
		setitem
		getitem
		delitem，
			class Foo(object):

				def __getitem__(self, item):
					return 1

				def __setitem__(self, key, value):
					pass
					
				def __delitem__(self, key):
					pass
					
			obj = Foo()
			obj['k1']
			obj['k1'] = 123
			del obj['k1']
		
		dict，api封装返回数据时：BaseResponse
		mro， 继承顺序
		slots，Local对象
	
	5. 栈 
		class Stack(object):
			
			def push(self,item):
				pass 
				
			def pop(self):
				pass 
				
		class Queue(object):
			def push(self,item):
				pass 
				
			def pop(self):
				pass 
				
	6. super/类.func(...)
	
	7. 什么是函数？什么是方法？
		
			def func():
				pass


			class Foo(object):

				def func(self):
					pass

			# 执行方式一
			# obj = Foo()
			# obj.func() # 方法

			# 执行方式二
			# Foo.func(123) # 函数

			from types import FunctionType,MethodType

			# obj = Foo()
			# print(isinstance(obj.func,FunctionType)) # False
			# print(isinstance(obj.func,MethodType))   # True


			print(isinstance(Foo.func,FunctionType)) # True
			print(isinstance(Foo.func,MethodType))   # False
	
	8. threading.local 
		
今日内容：
	- 代码统计
	- pymysql
	- 数据库连接池：
		 - DBUtils
	- 初步认识：SQLAlchemy
	

内容详细：
	- 代码统计
	
	- 数据库连接池：	
		pip3 install DBUtils
	
	
	
	注意：
		- 使用数据库连接池
		- 封装SQLHelper
	
	
	
作业：
	1. 功能完善
	2. BootStrap 模板
	3. 详细页面： http://127.0.0.1:5000/detail/1  -> 折线图
	4. 用户列表：
				- 柱状图
				- 表格
				PS: select user_id,sum(line) from record group by user_id + 连表查询到用户姓名
					
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	