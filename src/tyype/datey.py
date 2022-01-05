import datetime


from tyype.inty import Inty



class Datey(object):

	def datey(message='\nDigite uma data válida.', yearMessage='\nDigite o ano:', monthMessage='\nDigite o mês:', dayMessage='\nDigite o dia:', s=None):
		i = None


		while(i is None):
			print('{}'.format(yearMessage))


			y = None
			while(y is None):
				try:
					y = Inty.inty(message)
					datetime.date(y, 1, 1)

				except:
					y = None
					print('\n{}'.format(message))


			print('{}'.format(monthMessage))


			m = None
			while(m is None):
				try:
					m = Inty.inty(message)
					datetime.date(y, m, 1)

				except:
					m = None
					print('\n{}'.format(message))


			print('{}'.format(dayMessage))


			d = None
			while(d is None):
				try:
					d = Inty.inty(message)
					datetime.date(y, m, d)

				except:
					d = None
					print('{}'.format(message))


			try:
				if(s is None):
					i = datetime.date(y, m, d)
			
				else:
					i = datetime.date(y, m, d).strftime(s)

			except:
				i = None
				print('{}'.format(message))


		return i



	def datey2(y=1, m=1, d=1, s=None):
		i = None


		try:
			if(s is None):
				i = datetime.date(int(y), int(m), int(d))
			
			else:
				i = datetime.date(int(y), int(m), int(d)).strftime(s)

		except:
			i = None


		return i