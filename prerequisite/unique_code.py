import hashlib


def unique_coding(email):
    m = hashlib.md5()
    m.update(email.encode("utf-8"))
    print(str(int(m.hexdigest(), 16))[0:6])


if __name__ == '__main__':
    address = "rgu10@sheffield.ac.uk"
    unique_coding(address)
