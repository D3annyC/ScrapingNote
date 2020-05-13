# %%
import json

fn = "login.json"

try:
    with open(fn) as fnobj:
        login = json.loads(fnobj)
except Exception:
    login = input("Enter ID: ")
    with open(fn, 'w') as fnobj:
        json.dump(login, fnobj)
        print("System has already record your ID")
else:
    print("%s Welcome back!" % login)


# %%
