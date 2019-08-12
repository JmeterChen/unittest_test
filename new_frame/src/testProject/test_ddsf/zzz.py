# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-08

import sys


class HTest:
	
	a = (sys._getframe().f_code.co_name)[:-4]
	print(a)
	
	
b = HTest()