#mengimpor GPIO
import RPi.GPIO as GPIO
#Ubah pengkabelan BCM/BOARD
GPIO.setmode(GPIO.BCM)
#mematikan warning /True
GPIO.setwarnings(False)
#Mengkonfigurasi GPIO pin 4 sebagai output
pin = 4
GPIO.setup(pin, GPIO.OUT)
#Kami menyalakan led
GPIO.output(pin, GPIO.HIGH)
