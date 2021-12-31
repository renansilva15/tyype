import sys
import datetime



class Tyype(object):

	def inty(message=None, s=None):
		i = None


		if(message is None):
			try:
				aux = int(input())

			except:
				aux = None

			else:
				i = aux


		elif(message == 1):
			i = []


			for l in sys.argv[1:]:
				aux = None


				if(s is None):
					try:
						aux = int(l)

					except:
						aux = None

					else:
						i.append(aux)


				else:
					aux2 = []


					try:
						aux = l.split(s)


						for c in aux:
							try:
								c = int(c)

							except:
								c = None

							else:
								aux2.append(c)

					except:
						aux=None

					else:
						if(aux2 != []):
							i.append(aux2)


		elif(message == 2):
			i = []


			for l in sys.argv[1:]:
				aux = None


				try:
					aux = open(l, 'r')

				except:
					aux = None


				if(aux):
					aux2 = []


					try:
						for c in aux:


							if(s):
								c = c.split(s) #


							for x in c:
								try:
									x = int(x)

								except:
									x = None

								else:
									aux2.append(x)

					except:
						pass #

					else:
						i.append(aux2)


		else:
			while(i is None):
				try:
					i = int(input())

				except:
					i = None
					print('{}'.format(message))


		return i



	def floaty(message=None, s=None):
		i = None


		if(message is None):
			try:
				aux = float(input())

			except:
				aux = None

			else:
				i = aux


		elif(message == 1):
			i = []


			for l in sys.argv[1:]:
				aux = None


				if(s is None):
					try:
						aux = float(l)

					except:
						aux = None

					else:
						i.append(aux)


				else:
					aux2 = []


					try:
						aux = l.split(s)


						for c in aux:
							try:
								c = float(c)

							except:
								c = None

							else:
								aux2.append(c)

					except:
						aux=None

					else:
						i.append(aux2)


		elif(message == 2):
			i = []


			for l in sys.argv[1:]:
				aux = None


				try:
					aux = open(l, 'r')

				except:
					aux = None


				if(aux):
					aux2 = []


					try:
						for c in aux:


							if(s):
								c = c.split(s) #


							for x in c:
								try:
									x = float(x)

								except:
									x = None

								else:
									aux2.append(x)

					except:
						pass #

					else:
						if(aux2 != []):
							i.append(aux2)


		else:
			while(i is None):
				try:
					i = float(input())

				except:
					i = None
					print('{}'.format(message))


		return i



	def datey(message='\nDigite uma data válida.', yearMessage='\nDigite o ano:', monthMessage='\nDigite o mês:', dayMessage='\nDigite o dia:'):
		i = None


		while(i is None):
			print('{}'.format(yearMessage))


			y = None
			while(y is None):
				try:
					y = Tyype.inty(message)
					datetime.date(y, 1, 1)

				except:
					y = None
					print('\n{}'.format(message))


			print('{}'.format(monthMessage))


			m = None
			while(m is None):
				try:
					m = Tyype.inty(message)
					datetime.date(y, m, 1)

				except:
					m = None
					print('\n{}'.format(message))


			print('{}'.format(dayMessage))


			d = None
			while(d is None):
				try:
					d = Tyype.inty(message)
					datetime.date(y, m, d)

				except:
					d = None
					print('{}'.format(message))


			try:
				i = datetime.date(y, m, d).strftime('%d/%m/%Y')

			except:
				i = None
				print('{}'.format(message))


		return i



	def inty2(i=None):
		try:
			if(type(i) is not float):
				i = int(i)

			else:
				i = None

		except:
			i = None


		return i



	def floaty2(i=None):
		try:
			i = float(i)

		except:
			i = None


		return i



	def datey2(y=1, m=1, d=1, s='%d/%m/%Y'):
		i = None


		try:
			i = datetime.date(int(y), int(m), int(d)).strftime(s)

		except:
			i = None


		return i




	def intyFile(name=None, s=None):
		i = None


		try:
			aux = open(name, 'r')

		except:
			aux = None


		else:
			i = []


			try:
				for l in aux:
					if(s):
						l = l.split(s) #


					for c in l:
						try:
							c = int(c)

						except:
							c = None

						else:
							i.append(c)

			except:
				i = None


		return i



	def floatyFile(name=None, s=None):
		i = None


		try:
			aux = open(name, 'r')

		except:
			aux = None


		else:
			i = []


			try:
				for l in aux:
					if(s):
						l = l.split(s) #


					for c in l:
						try:
							c = float(c)

						except:
							c = None

						else:
							i.append(c)

			except:
				i = None


		return i