#!/usr/bin/python3
import sys
def print_args():
    num_args = len(sys.argv) - 1
    if num_args == 0:
       print("Number of argument(s): 0.")
    elif num_args == 1:
         print(f"Number of argument(s): {num_args} argument: {sys.argv[1]}")
         else:
                                                        print(f"Number of argument(s): {num_args} arguments: {', '.join(sys.argv[1:])}")
                                                            
                                                                for i, arg in enumerate(sys.argv[1:], start=1):
                                                                            print(f"{i}: {arg}")

                                                                            if __name__ == "__main__":
                                                                                    print_args()


