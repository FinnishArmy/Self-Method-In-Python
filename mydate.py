class Date(object):
	""" a blueprint (class) for objects
		that represent calendar days
	"""
	def __init__(self, month, day, year):
		self.month = month
		self.day = day
		self.year = year

	def __repr__( self ):
		""" used for printing Dates """
		s = "%02d/%02d/%04d" % (self.month, self.day, self.year)
		return s

	def isLeapYear(self):
		""" determines if data is leap year """
		if self.year % 400 == 0: return True
		if self.year % 100 == 0: return False
		if self.year % 4 == 0: return True
		return False

	def copy(self):
		return Date(self.month, self.day, self.year)

	def yesterday(self):
		""" Changes the day to yesterday """
		
		#Changing Month
		if self.day == 1:
			#January
			if self.month == 1:
				self.month = 12
				self.day = 31
				self.year -= 1

			#To Feb
			elif self.month == 3:
				if self.isLeapYear():
					self.day = 29
				else:
					self.day = 28
				self.month -= 1

			elif self.month in [5, 7, 10, 12]:
				self.month -= 1
				self.day = 30

			else:
				self.month -= 1
				self.day = 31
		else:
			self.day -= 1

date1 = Date(3,1,2020)
date2 = Date(10,9,2020)
print(date1)
print(date1.yesterday())
date2.yesterday()
print(date1)
print(date2)

# Copy
# date1 = Date(10,10,2019)
# date2 = Date(10,9,2020)
# date3 = date1.copy()
# print('date1 ', date1)
# print('date3 ', date3)
# print('date1 id ', id(date1))
# print('date2 id ', id(date2))
# print('date3 id ', id(date3))

# Checking leap year
# print(date1.isLeapYear())
# print(date2.isLeapYear())
# print(date1)

# Fancy printing
# x = 1.121
# print('this is CS %f howdy ho' % x)
# print('this is cs', x, 'howdy ho')
#Examining IDs of objects
# print('Date1 ID is: %d' % id(date1))
# print('Date2 ID is: %d' % id(date2))
# date2 = date1
# print('date2 = date1')
# print('Date1 ID is: %d' % id(date1))
# print('Date2 ID is: %d' % id(date2))
# print('Date1 day: ', date1.day)
# print('Date2 day: ', date2.day)
# date2.day = 50
# print('date2.day=50')
# print('Date1 day: ', date1.day)
# print('Date2 day: ', date2.day)
