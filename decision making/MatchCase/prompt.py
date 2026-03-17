prompt=input("Enter the prompt :")

match prompt:

    case "start":print("System starting")

    case "stop":print("Sytem stop working")

    case "restart":print("System restarting")

    case _:print("invalid prompt")
