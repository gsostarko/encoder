class Encrypter:
	"""
	Encripter class consists of:
	.stringToHex - string to HEX converter
	.__getDecDigit - HEX to decimal converter
	.b58encode - Base58 encoder 
	"""

	def stringToHex(self, str_var):
		"""
		String to HEX converter. 
		Args:
		: var - string to convert to HEX value

		Returns:
		Returns HEX value of converted text
		"""
		hex_str = str_var.encode('utf-8')
		#print(hex_str.hex())
		return hex_str.hex()
	
	def hexToString(self, hex_var):
		if hex_var[2:] == '0x':
			hex_var = hex_var[2:]
		str_var = bytes.fromhex(hex_var).decode('utf-8')
		return str_var

	def hexToDecimal(self, hexNum:str):
		"""
		Converts HEX to integer value.

		Args:
		: hexNum - <class 'str'> - input string to convert to decimal value 

		Retruns:
		Returns integer value as a integer - <class 'int'>
		"""
		return int(hexNum, 16)

	def decimalToHex(self, int_var:int):
		"""
		Converts integer to HEX value.

		Args:
		: int_var - <class 'int'> - input integer to convert to HEX value 

		Retruns:
		Returns HEX value as a string - <class 'str'>
		"""
		return hex(int_var)[2:]

	def b58encode(self, v):
		"""
		Base58 encoder

		Args:
		: v - input string of HEX value

		Returns:
		Returns encoded base58 string
		"""
		v = self.stringToHex(v)
		alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
		number = self.hexToDecimal(v)
		
		string = ""
		while number: #if number > 0 tehn do X
			modulo = number % 58
			number = number // 58
			string = alphabet[modulo] + string
			#print("\n number: {}, modulo: {}, string: {}".format(number,modulo,string))
		return string

	def b58decode(self, v):
		
		alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
		power = 0
		decimal = 0
		for character in reversed(v):
			#print(character)
			#print(alphabet.rfind(character))

			number = (alphabet.rfind(character)*58**power)
			power += 1
			decimal = decimal + number
		hex_var = self.decimalToHex(decimal)
		string = self.hexToString(hex_var)
		return string
		

