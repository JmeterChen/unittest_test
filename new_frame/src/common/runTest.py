# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-12


import unittest
from src.common.runMethod import RunMethod


class RunTest(unittest.TestCase, unittest.SkipTest):
	
	def __init__(self, methodName='runTest'):
		super(RunTest, self).__init__(methodName)
		self.desc = ""     # 用例描述
		self.case_id = ""  # 用例id
		self.method = RunMethod()
	
	def skipTest(self, reason):
		"""
		过滤用例
		:param reason:  过滤用例原因
		:return:   unittest.SkipTest
		"""
		raise unittest.SkipTest
	
	def getCasePro(self):
		"""
		获取用例基本信息
		:return: case_id， desc
		"""
		return self.desc
	
	def start(self, method_num, url, para_num, body_num, desc_num, *args, **kw):
		"""
		用例运行主入口
		:param url:         请求地址
		:param method_num:  请求方法所在列数
		:param para_num:    接口请求参数所在列数
		:param body_num:    接口请求体所在列数
		:param desc_num:    接口描述所在列数
		:param args:        从excle表中获取到的每条用例的测试数据
		:return:            None
		"""
		# print(args[0])
		# print(desc_num)
		self.desc = args[0][desc_num]
		# self.header = args[0][header_num]
		res = self.method.run_main(method_num, url, para_num, body_num, *args, **kw)
		return res