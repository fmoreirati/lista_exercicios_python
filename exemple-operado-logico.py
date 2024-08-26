password = "1111"
email = "fab@email"

isActive = True
isUser = email == "fab@email"
isPass = password == "1111"
print(isUser and isPass or isActive)