import numpy as np

class Agent:
	def __init__(self, point:[int, int], team:int): #エージェント生成(point:座標,team:チーム)
		self._point = np.array(point) #座標
		self._team = team #所属チーム(1or2)

	def move(self,vector:[int, int]): #エージェントを動かす(vector:方向)
		self._point += np.array(vector)