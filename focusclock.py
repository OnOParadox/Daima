import time

def focus_timer(duration):
    start_time = time.time()
    end_time = start_time + duration * 60  

    while time.time() < end_time:
        remaining_time = end_time - time.time()
        minutes = int(remaining_time // 60)
        seconds = int(remaining_time % 60)
        time_str = f"{minutes:02d}:{seconds:02d}"
        print(f"Remaining time: {time_str}", end="\r")
        time.sleep(1)  

    print("\nTime's up! Stay focused!")


focus_timer(25)
