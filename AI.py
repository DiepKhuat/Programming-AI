import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_mouth = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()
robot_brain=""

while True:
	with speech_recognition.Microphone() as mic:
		print ("Robot: I'm listening")
		audio = robot_ear.listen(mic)
	#statement with bằng với mic = peech_recognition.Microphone()
	# khác nhau là với with thì khi run đến hết audio thì mic sẽ tự động dừng

	print("Robot: ...")

	try:
		you = robot_ear.recognize_google(audio)
	except:
		you = ""
	print("You:" + you)


	if you =="":
		robot_brain ="I can't hear you, try again"
	elif "hello" in you:
		robot_brain ="Hello Diep"
	elif "today" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
	elif "time" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S seconds")
	elif "prime minister" in you:
		robot_brain= "Yoshihide Suga"
	elif "bye" in you:
		robot_brain ="Bye Diep"
		print ("Robot:" + robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	else:
		robot_brain = "I'm fine thank you, and you"

	print ("Robot:" + robot_brain)
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()