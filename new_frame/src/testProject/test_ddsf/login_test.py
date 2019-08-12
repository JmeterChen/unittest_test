# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-08


import unittest
import os
import inspect
from src.common.read_data import ReadData
import ddt
import sys
from src.common.runTest import RunTest

# # fieldname = "Login"
#
# # project = os.path.dirname(__file__)[-4:]
# # a = ReadData(project)
# # data = a.get_module_data("Login")
# data = [['prod', 'Login', 'ByPassword', 'post', '{"content-type": "application/json"}', '', '用户名密码正确登录', '{\n"username":"18682236985",\n"password":"Wawa520."\n}', '{"code":200}', ''], ['prod', 'Login', 'ByPassword', 'post', '{"content-type": "application/json"}', '', '用户名或密码为空', '{\n"username":"",\n"password":"Wawa521."\n}', '{\n"code":-1,\n"msg":"用户名或密码为空"\n}', ''], ['prod', 'Login', 'ByPassword', 'post', '{"content-type": "application/json"}', '', '用户名或密码为空', '{\n"username":"18682236985",\n"password":""\n}', '{\n"code":-1,\n"msg":"用户名或密码为空"\n}', ''], ['prod', 'Login', 'ByPassword', 'post', '{"content-type": "application/json"}', '', '用户名或密码错误', '{\n"username":"18682236985",\n"password":"Wawa520"\n}', '{\n    "code": "40352",\n    "msg": "User not exists or password incorrect"\n}', ''], ['prod', 'Login', 'ByPassword', 'post', '{"content-type": "application/json"}', '', '用户名或密码错误', '{\n"username":"13217176556",\n"password":"Wawa520."\n}', '{\n    "code": "40352",\n    "msg": "User not exists or password incorrect"\n}', '']]
#
#
# def get_data_by_key(source, data_key):
# 	list_data = []
# 	for i in range(len(source)):
# 		if source[i][2] == data_key:
# 			list_data.append(source[i])
# 	return list_data
#
#
# # fieldname = "Login"
# print(data)

# #########初始用例
# @ddt.ddt
# class LoginTest(unittest.TestCase):
# 	"""登录模块"""
#
# 	# 通过文件名获取project参数的值
# 	project = os.path.dirname(__file__)[-4:]
# 	a = ReadData(project)
# 	#
# 	# # 通过类名获取fieldname的值
# 	fieldname = sys._getframe().f_code.co_name[:-4]
#
# 	@classmethod
# 	def setUpClass(cls):
# 		cls.env_num = cls.a.get_num_name("环境")
# 		# cls.headers_num = cls.a.get_num_name("请求头")
# 		cls.body_num = cls.a.get_num_name("请求体")
# 		cls.expect_num = cls.a.get_num_name("预期结果")
#
# 	@ddt.data(*a.get_data_by_api(fieldname, "ByPassword"))
# 	def test_ByPassword(self, value):
# 		"""用户名密码登录"""
# 		# 通过函数名获取apiName参数的值
# 		self.apiName = (inspect.stack()[0][3])[5:]
# 		env = value[self.env_num]
# 		url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
# 		result = requests.post(url=url, json=value[self.body_num])
# 		res = result.json()
# 		# print(res["code"])
# 		self.assertEqual(res["code"], value[self.expect_num]["code"])


@ddt.ddt
class LoginTest(RunTest):
	"""登录模块"""

	# 通过文件名获取project参数的值
	project = os.path.dirname(__file__)[-4:]
	a = ReadData(project)
	#
	# # 通过类名获取fieldname的值
	fieldname = sys._getframe().f_code.co_name[:-4]

	@classmethod
	def setUpClass(cls):
		cls.env_num = cls.a.get_num_name("环境")
		# cls.headers_num = cls.a.get_num_name("请求头")
		cls.method_num = cls.a.get_num_name("请求方法")
		cls.para_num = cls.a.get_num_name("请求参数")
		cls.desc_num = cls.a.get_num_name("用例描述")
		cls.data_num = cls.a.get_num_name("请求体")
		cls.expect_num = cls.a.get_num_name("预期结果")

	@ddt.data(*a.get_data_by_api(fieldname, "ByPassword"))
	def test_ByPassword(self, value):
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		env = value[self.env_num]
		url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
		# result = requests.post(url=url, json=value[self.body_num])
		result = self.start(self.method_num, url, self.para_num, self.data_num, self.desc_num, value)
		# print(self.desc)
		res = result.json()
		self.assertEqual(res["code"], value[self.expect_num]["code"])
		
if __name__ == '__main__':
	unittest.main()