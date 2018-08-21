class Struct(object):
	"""docstring for Struct"""
	def __init__(self, portaOrigem, portaDestino, window, flag, offset, ack, seq, Dados):
		super(Struct, self).__init__()
		self.portaOrigem = portaOrigem
		self.portaDestino = portaDestino
		self.window = window
		self.flag = flag
		self.offset = offset
		self.ack = ack
		self.seq = seq
		self.Dados = Dados

	def imprimir(self):
		print(self.portaOrigem)
		print(self.portaDestino)
		print(self.window)
		print(self.flag)
		print(self.offset)
		print(self.ack)
		print(self.seq)
		print(self.Dados)			
		pass

