class Unit:
	def __init__(self):
		pass

	def _get_speed(self):
		if self.action == 'fly':
			return self.speed * 1.2
		elif self.action == 'crawl':
			return self.speed * 0.5
		else:
			raise ValueError('')

	def move(self, direction):

		speed = self._get_speed()

		if direction == 'UP':
			self.field.set_unit(y=self.y + speed, x=self.x, unit=self)
		elif direction == 'DOWN':
			self.field.set_unit(y=self.y - speed, x=self.x, unit=self)
		elif direction == 'LEFT':
			self.field.set_unit(y=self.y, x=self.x - speed, unit=self)
		elif direction == 'RIGTH':
			self.field.set_unit(y=self.y, x=self.x + speed, unit=self)


class Field:
	def set_unit(self, x, y, unit: Unit):
		pass
