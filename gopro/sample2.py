from gpiozero import Button

 pin_number=26

 def pressed_callback(): 
     print("Pin26 detected") 
 
 button=Button(pin_number, pull_up=False) 
 button.when_pressed = pressed_callback
 
 try: 
      while True:
      	  pass
 except KeyboardInterrupt:
 	  print("Program END")