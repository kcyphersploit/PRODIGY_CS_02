'''Welcome To Pixel Image Manipulation Tool For Steganography Written By KUSHAGRA VERMA'''
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os

def encode_message(image_path, message):
  img = Image.open(image_path).convert("RGB")
  width, height = img.size
  # Convert message to binary and add padding for byte alignment
  binary_message = ''.join(format(ord(char), '08b') for char in message)
  total_bits = len(binary_message)
  padded_message = binary_message + '0' * ((width * height * 3 - len(binary_message)) % 8)
  usable_pixels = width * height // 3
  # Check message length based on usable pixels (Method 2)
  if len(message) * 8 > usable_pixels:
    print("Error: Message is too long to fit in the image!")
    return None  # Encode message into LSB of pixels and total bits at the beginning
  x, y = 0, 0
  encoded_message = format(total_bits, '08b') + padded_message
  for bit in encoded_message:
    # Get current pixel RGB values
    r, g, b = img.getpixel((x, y))
    new_r = r & ~1 | int(bit)
    img.putpixel((x, y), (new_r, g, b))
    x += 1
    if x >= width:
      x = 0
      y += 1

  return img

def choose_image():
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    file_path = filedialog.askopenfilename()
    root.destroy()
    check_extension(file_path)
    return file_path

def check_extension(file_path):
  _, file_extension = os.path.splitext(file_path)
  valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif")
  if file_extension.lower() in valid_extensions:
    print()
    print(f"\033[3;92;40mImage Selected : {file_path}\033[m")
  else:
    print('\033[3;91;40mUsage: Allowed Extensions = ".jpg",".jpeg",".png",".bmp",".gif"\033[m')
    print("\033[3;91;40mRun the Script Again with valid usage..\033[m")
    exit()

def decode_message(image_path):
  img = Image.open(image_path).convert("RGB")
  width, height = img.size
  binary_message = ""
  for y in range(height):
    for x in range(width):
      r, g, b = img.getpixel((x, y))
      binary_message += str(r & 1)
  total_bits = int(binary_message[:8], 2)
  message = binary_message[8:total_bits]  # Extract only intended message length
   # Remove padding and convert binary to string
  return ''.join(chr(int(message[i:i+8], 2)) for i in range(0, len(message), 8))

def main():
    while True:
        print("-*-" * 30)
        print('''\033[1;96;40m
         _______  _______  ______    _______  _______  __    _  _______ 
        |       ||       ||    _ |  |       ||       ||  |  | ||       |
        |  _____||    ___||   | ||  |    _  ||    ___||   |_| ||_     _|
        | |_____ |   |___ |   |_||_ |   |_| ||   |___ |       |  |   |  
        |_____  ||    ___||    __  ||    ___||    ___||  _    |  |   |  
         _____| ||   |___ |   |  | ||   |    |   |___ | | |   |  |   |  
        |_______||_______||___|  |_||___|    |_______||_|  |__|  |___|  
        \033[m''')
        print("-*-" * 30)
        print("\033[3;95;40mWelcome To Steganography Tool By Pixel Image Manipulator -- Written By KUSHAGRA VERMA\033[m")
        print("-*-" * 30)
        print()
        mode = input("Enter \033[1;92;40m'encode'\033[m or \033[1;91;40m'decode'\033[m: ").lower()
        if mode not in ('encode', 'decode'):
            print("\033[3;93;40mInvalid mode. Please enter 'encode' or 'decode'.\033[m")
            continue
        image_path = choose_image()
        if mode == 'encode':
            print()
            message = input("\033[3;36;40mEnter the message (for Encoding -- please append space -> '' after end of message  :\033[m ")
            print()
            encoded_img = encode_message(image_path, message)
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.asksaveasfilename(defaultextension=".png")
            if file_path:
                print()
                encoded_img.save(file_path)
                print("\033[7;92;40mImage saved successfully at:\033[m", file_path)
                print("-*-" * 35)
            else:
                print("\033[7;91;40mNo Directory selected.\033[m")
                print("-*-" * 35)
        else:
            print()
            decoded_message = decode_message(image_path)
            print()
            print(f"Decoded message: \033[1;93;40m{decoded_message}\033[m")
            print()
        break




if __name__ == "__main__":
  main()

# Signing Off -- KUSHAGRA VERMA
