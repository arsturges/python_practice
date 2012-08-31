import math

class Polygon():
	def __init__(self, coords):
		self.coords = coords

	def dist_between_2_pts(self,a,b):
		ax = a[0]
		ay = a[1]
		bx = b[0]
		by = b[1]
		x = bx - ax
		y = by - ay
		d = math.sqrt(x**2 + y**2)
		return d

	def perimeter(self):
		total_points = len(self.coords)
		print("total points:", total_points)
		perimeter = 0
		point_number = 0	
		while point_number < total_points-1:
			print("point number:", point_number)
			perimeter += self.dist_between_2_pts(self.coords[point_number],self.coords[point_number+1])
			point_number += 1
		perimeter += self.dist_between_2_pts(self.coords[point_number],self.coords[0]) #close the loop
		return perimeter

a = Polygon([[0,0],[0,1],[1,1],[1,0]])
print a.perimeter()

b = Polygon([[0,-2],[1,1],[3,3],[5,1],[4,0],[4,-3]])
print b.perimeter()
