class LetterMeter:
	def __init__(self):
		self.vowel="aeıioöuüAEIİOÖUÜ"
		self.consonant="bcçdfgğhjklmnprsştvyzBCÇDFGĞHJKLMNPRSŞTVYZ"
		self.vowel_meter=0
		self.consonant_meter=0

	def ask_word(self):
		return input("Enter a text: ")

	def it_is_vowel(self,letter):
		return letter in self.vowel

	def it_is_consonant(self,letter):
		return letter in self.consonant

	def increase(self):
		for letter in self.word:
			if self.it_is_vowel(letter):
				self.vowel_meter+=1
			if self.it_is_consonant(letter):
				self.consonant_meter+=1
		return (self.vowel_meter,self.consonant_meter)

	def press(self):
		vowel,consonant=self.increase()
		message="In {}, there are {} vowel and {} consonant letter."
		print(message.format(self.word,vowel,consonant))

	def run(self):
		self.word=self.ask_word()
		self.press()

if __name__=="__main__":
	meter=LetterMeter()
	meter.run()