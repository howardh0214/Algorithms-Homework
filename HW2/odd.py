def main():
    while True:
        try:
		        x = int(input())
        except EOFError:
		        break
        height = (x + 1) / 2
        nth = (x + 1) * height / 2
        num = 2 * nth - 1
        sum = 3 * num - 6
        print(int(sum))

if __name__ == '__main__':
	main()