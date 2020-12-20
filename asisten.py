import pyttsx3
tts = pyttsx3.init()
tts.setProperty('voice', 'ru')

def say_bot(msg):
	'''Бот говорит'''
	tts.say(msg)
	print(msg)
	tts.runAndWait()
	
	
say_bot('Анёнгхасэё, я  Алкаши Хатаке')
say_bot('А ты кто?')
NAME = input('->  ')
command = input('Введите команду')
if 'Привет' in command:
	say_bot('Привет' + NAME)
command = input('Введите команду')	
if 'как дела?' in command:
	say_bot('Ну как всегда, норм')
command = input('Введите команду')
if 'что делаешь?' in command:
	say_bot('На задании')
	

