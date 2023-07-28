country = input("Enter your country Name : ")
country = country.strip()

match country:
    case "USA":
        print("Hello")
    case "India":
        print("Namaste")
    case "Germany":
        print("Hallo")
    case _:
        print("invalid")

