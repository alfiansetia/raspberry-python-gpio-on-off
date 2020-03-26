#mengimpor library gpio
import RPi.GPIO as GPIO
#mengubah penomoran ke BCM /BOARD 
GPIO.setmode(GPIO.BCM)
#Mematikan warning
GPIO.setwarnings(False)
#Mengkonfigurasi GPIO pin 4 sebagai output
pin = 4
GPIO.setup(pin, GPIO.OUT)
#Mematikan dipimpin
GPIO.output(pin, GPIO.LOW)
#Dan kita membebaskan GPIO
GPIO.cleanup()
