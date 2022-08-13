def getBinaryGap(N):
    b = bin(N).replace("0b", "")
    print(b)
    one_count = [pos for pos, char in enumerate(b) if char == '1']
    dif = [one_count[i+1]-one_count[i] for i in range(len(one_count)-1)] 

    return 0 if b.count('0') == 0 or b.count('1') == 1 else max(dif)-1

if __name__ == '__main__':
    print(getBinaryGap(574))
