def plusOne(A):
    n=len(A)
    for i in range(n-1,-1,-1):
        if(A[i]<9):
            A[i]=A[i]+1
            for j in range(i):
                if(A[j]!=0):
                    return A[j:]
            return A
        else:
            A[i]=0

    a=1
    return [a]+A


def main():
	print("Enter the size of the array")
	n=int(input())
	arr=list()
	for i in range(n):
		t=int(input())
		arr.append(t)

	print(plusOne(arr))

if __name__ == '__main__':
	main()