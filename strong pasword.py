password=input("enter the pasword")
if len(password)>=6 and len(password)<16:
    if "$" in password:
        if "2" in password or "8" in password:
                if "A" in password or "Z" in passwpord:
                        print("strong password")
else:
        print("try again")