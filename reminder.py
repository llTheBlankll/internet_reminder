import os
import playsound
import requests


# * Clear Terminal
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def main():
    clear()
    # Ring 5x if connection succeeded
    success_con_ring_loop_count: int = 5

    # Retry Count refers to how many retries has been made.
    retry_count: int = 0

    # Infinite loop
    while True:
        print("Retry Count : %s" % retry_count)

        try:
            # Check for Connection
            r = requests.get("https://google.com")
            # If r.status_code is 200, play sound using playsound module
            if r.status_code == 200:
                print("SUCCESS CONNECTION!")
                # Ring 5x according to the value of variable success_con_ring_loop_count.
                for ring in range(success_con_ring_loop_count):
                    playsound.playsound("sound.mp3")
                # Stop the loop
                break
            else:
                # No internet.
                print("No Internet")
        except requests.ConnectionError:  # Other way to say no internet.
            print("Connection Error")
        except Exception as e:  # If unknown error occurred, print stacktrace.
            print(e)
        retry_count += 1  # Add count to retry count


if __name__ == '__main__':
    main()
