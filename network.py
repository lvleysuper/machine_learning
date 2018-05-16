# -*- coding:utf-8 -*-
"""
network.py
~~~~~~~~~~

* 随机梯度下降和前馈神经网络实现
* 梯度更新使用反向传播算法
"""
import random

# 三方库
import numpy as np

class Network(object):


	def __init__(self, sizes):
		"""
		sizes : 定义每一层的神经网络数目，格式如：[2, 3, 1]，第一层2个神经元，第二层3个神经元，输出层一个神经元
		biases : 神经第二层到输出层的偏置，第一层作为输入层，没有设置偏置
		weights : 层间权重，x-> [0, n-1], y-> [1, n]
		biases，weights使用高斯分布初始化，均值为0，标准差为1

		numpy.random.randn(d0, d1, …, dn)是从标准正态分布中返回一个或多个样本值。d0, d1,...,dn代表维度
		"""
		self.num_layers = len(sizes)
		self.sizes = sizes
		self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
		self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]

