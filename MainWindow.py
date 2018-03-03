import os
import random
import json
import pprint
import time
import datetime
import LeetcodeAPI
import milsUtils
import webbrowser
import LeetData

try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    import Tkinter as tk
    from Tkinter import messagebox
import pathlib


TITLE_VALUE = "LeetCode Tracker"

class mainWindow:    
  def __init__(self, master, root, json):
      self.mw = master
      self.tk = root
      self.mainFrame = tk.Frame(master=master, bg="black")
      self.mainFrame.pack(fill=tk.BOTH, expand=1)
      self.mainFrame.option_add("*Label.Background", "black")
      self.mainFrame.option_add("*Label.Foreground", "white")
      self.mainFrame.grid_columnconfigure(0,weight=1)
      self.mainFrame.grid_columnconfigure(1,weight=1)
      self.mainFrame.grid_columnconfigure(2,weight=1)
      self.mainFrame.grid_columnconfigure(3,weight=1)


      #LeetCodeTracker!
      self.ltcString = tk.StringVar(master=self.mainFrame, value=TITLE_VALUE)
      self.leetCodeTrackerLabel = tk.Label(master = self.mainFrame, textvariable=self.ltcString, font=("Futura", 28))
      self.leetCodeTrackerLabel.grid(row=0, column=0, pady=25, columnspan=4)

      #Info frame to hold all info
      self.infoFrame = tk.Frame(master=self.mainFrame,bg="black")
      self.infoFrame.grid_columnconfigure(0,weight=1)
      self.infoFrame.grid(row=1, columnspan=4)
      
      #Clock setup
      self.clockTime = tk.StringVar(master, "0:00:00.000")
      self.clock = tk.Label(master=self.infoFrame,textvariable=self.clockTime, font=("Futura", 24))
      self.clock.grid(row=1,column=1,padx=15,pady=10)
      self.clockRunning = False
      self.stopped = True
      self.startTime = 0
      self.update_clock()

      #Left Labels
      #Elapsed time
      self.elapsedTimeLabel = tk.Label(master=self.infoFrame, text="Time:", font = ("Futura", 18))
      self.elapsedTimeLabel.grid(row=1,column=0,padx=10,pady=10, sticky=tk.E)

      #Number To Do
      #Label
      self.numberLabel = tk.Label(master=self.infoFrame, text="Assignment: ", font=("Futura", 18))
      self.numberLabel.grid(row=2,column=0,padx=10,pady=10, sticky=tk.E)

      #Actual number
      self.numberToDoVariable = tk.StringVar(master=self.infoFrame, value = "N/A")
      self.numberToDoLabel = tk.Label(master=self.infoFrame, textvariable=self.numberToDoVariable, font=("Futura", 28))
      self.numberToDoLabel.grid(row=2,column=1,padx=15,pady=10)

      #Language To Use:
      #Label
      self.languageLabel = tk.Label(master=self.infoFrame, text="Language: ", font=("Futura", 18))
      self.languageLabel.grid(row=3,column=0,padx=10,pady=10, sticky=tk.E)

      #Actual language
      self.languageToUse = tk.StringVar(master=self.infoFrame, value="N/A")
      self.languageToUseLabel = tk.Label(master=self.infoFrame, textvariable=self.languageToUse, font=("Futura", 28))
      self.languageToUseLabel.grid(row=3,column=1,padx=15,pady=10)


      #Setup Buttons
      self.buttonFrame = tk.Frame(master=self.mw)
      self.buttonFrame.pack(side=tk.LEFT, fill=tk.X, expand=True)

      #Start/Stop button
      self.startStopText = tk.StringVar(master=self.buttonFrame, value="Start")
      self.startButton = tk.Button(master=self.buttonFrame, textvariable=self.startStopText, font=("Futura", 12), bg="green", fg="black")
      self.startButton.bind("<ButtonRelease-1>", self.startPressed)
      self.startButton.pack(side=tk.LEFT, fill=tk.X, expand=True)

      #Finished button
      self.finishedButton = tk.Button(master=self.buttonFrame, text="Finished", font=("Futura", 12))
      self.finishedButton.bind("<ButtonRelease-1>", self.finishedPressed)
      self.finishedButton.configure(state=tk.DISABLED)
      self.finishedButton.pack(side=tk.LEFT, fill=tk.X, expand=True)
      
      #Change assignment button
      self.changeAssignmentButton = tk.Button(master=self.buttonFrame, text="Change Assignment", font=("Futura", 12), state=tk.DISABLED)
      self.changeAssignmentButton.bind("<ButtonRelease-1>", self.updateNumberToDo)
      # self.changeAssignmentButton.pack(side=tk.LEFT, fill=tk.X, expand=True)

      #Change language button
      self.changeLang = tk.Button(master=self.buttonFrame, text="Change Language", font=("Futura", 12))
      self.changeLang.bind("<ButtonRelease-1>", self.cycleLanguage)
      self.changeLang.pack(side=tk.LEFT, fill=tk.X, expand=True)


  def getNewProblem(self):
      self.prob = LeetData.getNextProblem()

  
  def update_clock(self):
      if not self.stopped:
          if not self.clockRunning:
              self.startTime = milsUtils.currentTime()
              self.clockRunning = True
          self.elapsed = milsUtils.currentTime() - self.startTime
          timeStamp = milsUtils.getStopwatchString(self.elapsed)
          self.clockTime.set(timeStamp)
          self.mw.after(1, self.update_clock)
      else:
          self.clockRunning = False

  def updateNumberToDo(self, event=None):
      self.getNewProblem()
      if self.stopped:
          self.numberToDoVariable.set(self.prob.frontend_id)

  def updateLanguageToUse(self, event=None):
      self.languageToUse.set(LeetData.getRandomLanguage())
  
  def cycleLanguage(self, event):
      if self.languageToUse.get() == "N/A":
          return "N/A"
      currentLanguageIndex = LeetData.LANGUAGES.index(self.languageToUse.get())
      if currentLanguageIndex == len(LeetData.LANGUAGES) - 1:
          return self.languageToUse.set(LeetData.LANGUAGES[0])
      else:
          return self.languageToUse.set(LeetData.LANGUAGES[currentLanguageIndex+1])

  def start(self):
      self.updateNumberToDo()
      self.updateLanguageToUse()
      self.stopped = False
      self.startButton.configure(bg="red")
      self.startStopText.set("Stop")
      self.changeAssignmentButton.configure(state=tk.DISABLED)
      self.finishedButton.configure(state=tk.NORMAL)
      webbrowser.open_new_tab(LeetcodeAPI.getProblemURL(self.prob))
      self.update_clock()

  def stop(self, ask=True):
      doStop = True
      if ask:
          if tk.messagebox.askyesno("Stop?", "Are you sure you want to stop? If you do you will not be able to save this challenge."):
              doStop = True
          else:
              doStop = False

      if doStop:
          self.stopped = True
          self.startButton.configure(state=tk.NORMAL, bg="green")
          self.startStopText.set("Start")
          self.changeAssignmentButton.configure(state=tk.NORMAL)
          self.finishedButton.configure(state=tk.DISABLED)
      
  

  def startPressed(self, event):
      if self.stopped:
          self.start()
      else:
          self.stop()

  def finishedPressed(self, event):
      if not self.stopped:
          LeetData.makeDir(self.numberToDoVariable.get())
          LeetData.jsonData["completed"][self.prob.id] = {'frontend_id':self.prob.frontend_id, 'language_used':self.languageToUse.get(), 'elapsed':self.elapsed, 'start':self.startTime}
          with open(LeetData.SAVE_FILE_NAME, 'w') as saves:
              json.dump(LeetData.jsonData, saves)
              saves.close()
          self.stop(ask=False)

#Deal with close event
def on_closing(window):
    quit = True
    if(not window.stopped):
        if tk.messagebox.askyesno("Stop?", "Are you sure you want to stop? If you do you will not be able to save this challenge."):
            quit = True
            window.stop(ask=False)
        else:
            quit = False
    LeetcodeAPI.writeReadme(LeetData.jsonData)
    window.mw.destroy()