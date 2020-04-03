import win10toast
import time

def get_reminder_details():
	print("Hey there, what do you want me to remind you about? Let me help!")
	title = input("Enter the title for the reminder: \n")
	message = input("Enter the Message for the reminder: \n")
	tt = input("When do you want to be reminded?\n [Please enter the time in this format = HH:MM:SS]\n Tell me: ")
	return tt, title, message

def setReminder():
	tt, title, message = get_reminder_details()
	while(True):
		curr_time = time.strftime("%H:%M:%S")
		if curr_time == tt:
			print(curr_time)
			break
		else:
			pass


	toaster = win10toast.ToastNotifier()
	toaster.show_toast(title,
			message,
			duration = 15
		)


setReminder()
