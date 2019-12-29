a=[]
i=0
b=[]
ku=0
xd=0
gd=0
hg=0
gh=0
buble=0
hu=False
io=[]
print('введите количество чисел в массиве')
n=float(input())

while i < float(n) :
    a.append(float(input()))
    i+=1

n=n-1
print(a)
io=a.sort()
while buble < n:
    while gd < n-buble:
        if a[ku] > a[ku + 1]:
            xd = a[ku]
            a[ku] = a[ku + 1]
            a[ku + 1] = xd
        gd += 1
        ku += 1
        print(ku)

    buble+=1
    print('gh'+str(buble))
    ku=0
    gd=0

print(a)
a=b
a.sort()
if a == b:
    hu = True
    print('сортировка масива = '+ str(hu))

