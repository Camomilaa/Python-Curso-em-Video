def maior(* num):
    mai = 0
    for c, n in enumerate(num):
        if c == 0:
            mai = n
        else:
            if n > mai:
                mai = n
    print(f'O maior número é {mai}')
maior(2,4,5)
maior(3,7,9,4)
maior(100,99,200)