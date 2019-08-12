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
import requests


@ddt.ddt
class MapSourceTest(RunTest):
	"""地图找店模块"""
	
	# 通过文件名获取project参数的值
	project = os.path.dirname(__file__)[-4:]
	a = ReadData(project)
	
	# 通过类名获取fieldname的值
	fieldname = sys._getframe().f_code.co_name[:-4]
	
	@classmethod
	def setUpClass(cls):
		cls.env_num = cls.a.get_num_name("环境")
		cls.header_num = cls.a.get_num_name("请求头")
		cls.method_num = cls.a.get_num_name("请求方法")
		cls.para_num = cls.a.get_num_name("请求参数")
		cls.desc_num = cls.a.get_num_name("用例描述")
		cls.data_num = cls.a.get_num_name("请求体")
		cls.expect_num = cls.a.get_num_name("预期结果")

	@ddt.data(*a.get_data_by_api(fieldname, "CityDistrict"))
	def test_CityDistrict(self, value):
		"""城市区域列表"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		env = value[self.env_num]
		url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
		result = self.start(self.method_num, url, self.para_num, self.data_num, self.desc_num, value)
		# print(type(value[self.data_num]))
		# result = requests.post(url=url, json=value[self.data_num])
		res = result.json()
		# print(res["code"])
		self.assertEqual(res["code"], value[self.expect_num]["code"])

	@ddt.data(*a.get_data_by_api(fieldname, "CitySection"))
	def test_CitySection(self, value):
		"""城市区域板块列表"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		env = value[self.env_num]
		url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
		result = self.start(self.method_num, url, self.para_num, self.data_num, self.desc_num, value)
		# result = requests.post(url=url, json=value[self.data_num])
		res = result.json()
		# print(res["code"])
		self.assertEqual(res["code"], value[self.expect_num]["code"])

	@ddt.data(*a.get_data_by_api(fieldname, "StoreInfoList"))
	def test_StoreInfoList(self, value):
		"""地图门店区域列表"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		env = value[self.env_num]
		url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
		result = self.start(self.method_num, url, self.para_num, self.data_num, self.desc_num, value)
		# result = requests.post(url=url, json=value[self.data_num])
		res = result.json()
		# print(res["code"])
		self.assertEqual(res["code"], value[self.expect_num]["code"])

	@ddt.data(*a.get_data_by_api(fieldname, "StoreByCodition"))
	def test_StoreByCodition(self, value):
		"""门店列表-地图区域条件"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		env = value[self.env_num]
		url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
		result = self.start(self.method_num, url, self.para_num, self.data_num, self.desc_num, value)
		# result = requests.post(url=url, json=value[self.data_num])
		res = result.json()
		# print(res["code"])
		self.assertEqual(res["code"], value[self.expect_num]["code"])

if __name__ == '__main__':
	unittest.main()