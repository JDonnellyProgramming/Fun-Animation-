import tkinter as tk
import math
from PIL import Image, ImageTk
import pygame

pygame.init()

root = tk.Tk()
root.geometry("1200x800")
root.config(bg="white")

text = tk.Text(root, height=1, width=1200)
text.config(background="white", borderwidth=0, highlightthickness=0)
text.place(x=0, y=600)

for i in range(1200):
  if i % 2 == 0:
      text.insert("end", "-")
  else:
      text.insert("end", " ")

label1 = tk.Label(root, text=" o\n\/|\\\n/ \\", bg="white", font=('Arial', 20, 'bold'))
label1.place(x=500, y=510)

label2 = tk.Label(root, text="----/-o", bg="white")
label3 = tk.Label(root, text="*", bg="white", fg="white", font=('Arial', 20, 'bold'))
text_label = tk.Label(root, text="", bg="white", fg="black",
                     font=('Arial', 16, 'bold'),
                     bd=1, relief="solid", width=16, height=4)
label4 = tk.Label(root, bg="red", width=2, height=3)


new_x = 300
new_y = 300
new_x1 = 500
new_y1 = 510
new_x2 = 600
new_y2 = 550
new_x3 = 1200
new_y3 = 560
animate1_finish = False
animate2_finish = False
animate3_finish = False
exploded = False
def animate():
      global new_x
      global new_y
      x = label2.winfo_x()
      y = label2.winfo_y()
      new_x = x + 10
      new_y = y + 10
      label2.place(x=new_x, y=new_y)
      if x >= 400:
          animate1_finish == True
          animate2()
          animate3()
      elif animate1_finish == False:
          root.after(100, animate)
def animate2():
  global new_x1
  global new_y1
  x = label1.winfo_x()
  y = label1.winfo_y()
  new_x1 = x + 6
  new_y1 = y
  label1.place(x=new_x1, y=new_y1)
  if x >= 650:
      animate2_finish == True
      animate4()
  elif animate2_finish == False:
      root.after(100, animate2)
def animate3():
  global new_x
  global new_x
  x = label2.winfo_x()
  y = label2.winfo_y()
  new_x = x + 6
  new_y = y + 2
  label2.place(x=new_x, y=new_y)
  if x >= 600:
      animate3_finish == True
      animate5()
  elif animate3_finish == False:
      root.after(100, animate3)
def animate4():
  global new_x2
  global new_y2
  global exploded
  x = label3.winfo_x()
  y = label3.winfo_y()
  new_x2 = x - 4
  new_y2 = y - 8
  label3.place(x=new_x2, y=new_y2)
  label3.config(fg="black")
  if exploded == False:
      root.after(100, animate4)
      label3.config(fg="black")
  else:
      label3.config(fg="white")
def animate5():
  global exploded
  x1, y1 = label1.winfo_x(), label1.winfo_y()
  x2, y2 = label3.winfo_x(), label3.winfo_y()
  if -50 <= (x1 - x2) <= 50 and not exploded:
      exploded = True
      label3.config(fg="white")
      animate6()
  root.after(100, animate5)
def animate6():
  label2.config(text="----/-o")
  root.after(20, lambda: label2.config(text="- - - - / - o"))
  root.after(400, lambda: label2.config(text="-  -  -  -  /  -  o"))
  root.after(600, lambda: label2.config(text="-    -    -    -    /    -    o"))
  root.after(800, lambda: label2.config(text="-     -     -     -     /      -     o"))
  root.after(1000, lambda: label2.config(text="-       -        -        -        /          -           o"))
  root.after(1200, lambda: label2.config(text="-         -          -          -          /            -             o"))
  root.after(1400, lambda: label2.config(text="-             -             -              -               /                  -                   o"))
  root.after(1600, lambda: label2.config(fg="white"))
  root.after(1600, lambda: label2.place_forget())
  root.after(1600, animate7)
g = 0
direction = 'up'
def animate7():
  import time
  global direction
  global g
  global new_x
  global new_y
  x = label1.winfo_x()
  y = label1.winfo_y()
  if direction == 'up':
      new_x = x
      new_y = y - g
      g += 10
  if y <= 400:
      direction = 'down'
      g = 5
  if direction == 'down':
      new_x = x
      new_y = y + g
      g += 10
      if new_y >= 510:
          g = 0
          animate8()
  label1.place(x=new_x, y=new_y)
  root.after(100, animate7)
text_ = ""
text_finished = False
def animate8():
   import time
   global text_
   global text_finished
   real_text = "Phew!! That was a close one!!"
   text_label.place(x=520, y=350)
   if text_finished == False:
       for i in real_text:
           text_ += i
           text_label.config(text=text_)
           text_label.update()
           time.sleep(0.2)
   if len(text_) >= len(real_text):
       text_finished = True
   if text_finished == True:
       text_label.place_forget()
       animate9()


direction2 = 'up'
g2 = 20
animate9_finished = False
def animate9():
   global new_x3
   global new_y3
   global direction2
   global g2
   global animate9_finished
   x = label4.winfo_x()
   y = label4.winfo_y()
   if animate9_finished == False:
       new_x3 = x + 10
       if direction2 == 'up':
           new_x3 = x - 10
           new_y3 = y - g2
           g2 -= 2
           if g2 <= 0:
               direction2 = 'down'
       if direction2 == 'down':
           new_x3 = x - 10
           new_y3 = y + g2
           g2 += 2
           if new_y3 >= 560:
               direction2 = 'up'
               g2 = 20
   if new_x3 <= 800:
       animate9_finished = True
   if animate9_finished == True:
       new_x3 = 800
       new_y3 = 560
       animate10()
   label4.place(x=new_x3, y=new_y3)
   root.update()
   root.after(100, animate9)

image = Image.open(r"C:\Users\josep\Downloads\dragon-png-14.png")
resize_image = image.resize((150, 150))
img = ImageTk.PhotoImage(resize_image)
label5 = tk.Label(image=img)
label5.image = img

new_x4 = 0
new_y4 = 200
sound_played = False
stop = False

def animate10():
   global sound_played
   global new_x4
   global new_y4
   global stop
   x = label5.winfo_x()
   y = label5.winfo_y()
   if not stop:
       if sound_played == False:
           sound = pygame.mixer.Sound(r"C:\Users\josep\Downloads\dragon-roar-96996.wav")
           sound.play()
           sound_played = True
       if sound_played == True:
           new_x4 = x + 10
           new_y4 = y + 4
           label5.place(x=new_x4, y=new_y4)
   if new_x4 >= 500:
       stop = True
   if stop:
       new_x4 = 500
       new_y4 = 300
       animate11()
   root.after(100, animate10)
label6 = tk.Label(root, width=2, height=1, bg="white")
new_x5 = 500
new_y5 = 250
def animate11():
   global new_x5
   global new_y5
   label6.config(bg="orange")
   new_x5 += 1
   new_y5 += 1
   label6.place(x=new_x5, y=new_y5)
label6.place(x=new_x5, y=new_y5)
label4.place(x=new_x3, y=new_y3)
animate()
label3.place(x=650, y=550)

root.mainloop()

root.mainloop()
