def login(email, password):
    return str(email) + str(password)

def hashing(password, hash):
    password *= hash%253
    password += hash/232
    return password