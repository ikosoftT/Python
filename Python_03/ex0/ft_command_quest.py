import sys



def run() -> None:
    n1 = sys.argv[1]
    n2 = sys.argv[2]
    try:
        sum = int(n1) + int(n2)
    except ValueError:
        print("err bro , Enter Valid Inputs")
    else:
        print(f"Result = {sum}")


if len(sys.argv) < 3:
    print("Please Enter Args!!")
else:
    run()

