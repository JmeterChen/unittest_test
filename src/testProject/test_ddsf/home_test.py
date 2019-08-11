# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-08


import unittest
import os
import inspect
from src.common.read_data import ReadData
import ddt
import sys
import requests


@ddt.ddt
class MapSourceTest(unittest.TestCase):
	"""地图找店模块"""
	
	# 通过文件名获取project参数的值
	project = os.path.dirname(__file__)[-4:]
	a = ReadData(project)
	
	# 通过类名获取fieldname的值
	fieldname = sys._getframe().f_code.co_name[:-4]
			
	@ddt.data(*a.get_data_by_api(fieldname, "CityDistrict"))
	def test_CityDistrict(self, value):
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		env_num = self.a.get_num_name("环境")
		body_num = self.a.get_num_name("请求体")
		expect_num = self.a.get_num_name("预期结果")
		env = value[env_num]
		url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
		result = requests.post(url=url, json=eval(value[body_num]))
		res = result.json()
		# print(res["code"])
		self.assertEqual(res["code"], eval(value[expect_num])["code"])

	@ddt.data(*a.get_data_by_api(fieldname, "CitySection"))
	def test_CitySection(self, value):
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		env_num = self.a.get_num_name("环境")
		body_num = self.a.get_num_name("请求体")
		expect_num = self.a.get_num_name("预期结果")
		env = value[env_num]
		url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
		result = requests.post(url=url, json=eval(value[body_num]))
		res = result.json()
		# print(res["code"])
		self.assertEqual(res["code"], eval(value[expect_num])["code"])

	@ddt.data(*a.get_data_by_api(fieldname, "StoreInfoList"))
	def test_StoreInfoList(self, value):
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		env_num = self.a.get_num_name("环境")
		body_num = self.a.get_num_name("请求体")
		expect_num = self.a.get_num_name("预期结果")
		env = value[env_num]
		url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
		result = requests.post(url=url, json=eval(value[body_num]))
		res = result.json()
		self.assertEqual(res["code"], eval(value[expect_num])["code"])

	@ddt.data(*a.get_data_by_api(fieldname, "StoreByCodition"))
	def test_StoreByCodition(self, value):
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		env_num = self.a.get_num_name("环境")
		body_num = self.a.get_num_name("请求体")
		expect_num = self.a.get_num_name("预期结果")
		env = value[env_num]
		url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
		result = requests.post(url=url, json=eval(value[body_num]))
		res = result.json()
		self.assertEqual(res["code"], eval(value[expect_num])["code"])

if __name__ == '__main__':
	unittest.main()