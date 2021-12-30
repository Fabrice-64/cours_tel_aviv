import time


real_password = "9999"

def check_password(password):  # Don't change it
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.1)  # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    return True


def crack_password():
    for i in range(0, 10, 1):
        i = str(i)
        test1 = "".join([i, "000"])
        start = time.time()
        check_password(test1)
        end = time.time()
        if end - start >= 0.2:
            break
    for j in range(0, 10, 1):
        j = str(j)
        test2 = "".join([i, j, "00"])
        start = time.time()
        check_password(test2)
        end = time.time()
        if end - start >= 0.3:
            break
    
    for k in range(0, 10, 1):
        k = str(k)
        test3 = "".join([i, j, k, "0"])
        start = time.time()
        check_password(test3)
        end = time.time()
        if end - start >= 0.4:
            break
    
    for l in range(0, 10, 1):
        l = str(l)
        test4 = "".join([i, j, k, l])
        result = check_password(test4)
        if result:
            break
    result = check_password(test4)
    print(result, test4)


if __name__ == "__main__":
    start = time.time()
    crack_password()
    end = time.time()
    print(end-start)
