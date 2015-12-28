file_ = open("input_day2_1")
totalArea = 0
totalRibbon = 0
for line in file_:
	dimensions = line.split('x')
	dimensions = [int(i) for i in dimensions]
	areas = [dimensions[0]*dimensions[1], dimensions[0]*dimensions[2], dimensions[1]*dimensions[2]]
	volume = dimensions[0]*dimensions[1]*dimensions[2]
	largest = dimensions.index(max(dimensions))
	smaller = [dimensions[x] for x in range(3) if x != largest]
	perimeter = 2*smaller[0] + 2*smaller[1]
	totalArea += 2*areas[0] + 2*areas[1] + 2*areas[2] + min(areas)
	totalRibbon += volume + perimeter
print totalArea
print totalRibbon