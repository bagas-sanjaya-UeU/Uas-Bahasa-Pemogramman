def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)


n = int(input("Masukkan nilai n: "))
print("Nilai faktorial dari", n, "adalah", faktorial(n))
