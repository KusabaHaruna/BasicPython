#a = input("aの値を入力: ")
#b = input("bの値を入力: ")

# TODO
#prime_numbersという関数を定義
def prime_numbers(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "は素数ではありません。")
                break
        else:
            print(num, "は素数です。")
    else:
        print(num, "は素数ではありません。")

num = int(input("aの値を入力してください:"))

#prime_numbers関数を呼び出す
prime_numbers(num)



#prime_numbersという関数を定義
def prime_numbers(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "は素数ではありません。")
                break
        else:
            print(num, "は素数です。")
    else:
        print(num, "は素数ではありません。")


num = int(input("bの値を入力してください:"))


#prime_numbers関数を呼び出す
prime_numbers(num)