def result(lst):
    if len(lst) == 0: return 0
    max_index = lst.index(max(lst)) + 1
    return max(lst) * max_index + result(lst[max_index:])
 
def main():
    n = int(input())
    lst = [int(x) for x in input().split()]
    print(result(lst))
 
main()