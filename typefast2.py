import time
import random
import sys


list = ['Hello, im David. Im 26 years old. Right now im working on a project named typing speed test. I hope u are having fun testing ur typing speed', 'This is my next sentence. if ur having fun yell hurayy', 'as im out of ideas what to write, i will just skip the 5th and 6th answer in this list.', 'Am 7. Dezember 2012 wurde die KEP in den Status des zweiten benannten Postbetreibers Kirgisistans erhoben. Dieser Status wird durch das Rundschreiben 83 des Universal Postal Union International Bureau vom 21. Mai 2013 offiziell bestätigt.']
Welcome = input('Hello user, welcome to this game. Are u ready to test ur typing speed? yes/no')
if Welcome.lower() == 'yes':
  print('alright, there will be issued a countdown of ur choice. Get ready!')

  # define the countdown func.
  def countdown(t):

      while t > 0:
          sys.stdout.write('\r {}'.format(t))
          t -= 1
          sys.stdout.flush()
          time.sleep(1)

      print("\n")

      print('LETS GO')
      random_sentence = random.choice(list)
      print(random.choice(list))
      start_time = time.time()
      user_input = input()
      end_time = time.time()
      time_difference = end_time - start_time
      print("Total time taken: ", round(time_difference, 2))


      error_count = 0
      for i in user_input.split(" "):
          if i not in random_sentence.split(" "):
              error_count += 1
      print("Total number of errors made: ", error_count)

      word_count = 0
      for i in user_input.split(" "):
          word_count += 1
      wpm = word_count / 5
      print("Words Per Minute (WPM): ", wpm)


  # input time in seconds
  t = input("Enter the time in seconds: ")

  # function call
  countdown(int(t))


else:
  print ("OK")
