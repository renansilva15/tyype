import sys



class Floaty(object):

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
								c = c.split(s)


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
	


	def floaty2(i=None):
		try:
			i = float(i)

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