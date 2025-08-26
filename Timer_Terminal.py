import time

def countdown():
    t = input("Timer - Einstellung (mm:ss): ")
    try:
        mins, secs = map(int, t.split(':'))
        total_secs = mins * 60 + secs
        while total_secs:
            mins, secs = divmod(total_secs, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            total_secs -= 1
        print("\nZeit ist abgelaufen!")
    except ValueError:
        print("Bitte gib die Zeit im Format mm:ss ein.")
countdown()