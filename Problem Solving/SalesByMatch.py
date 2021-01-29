# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    a = set(ar)
    cnt = int(0)
    siz = len(a)
    for i in range (0,siz):
        c = ar.count(a.pop())
        cnt = cnt + int(c/2)
    return cnt 
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
