#manual garbage collection
import sys, gc
def test():
    list = [18, 19, 20,34,78]
    list.append(list)
def main():
    print("Garbage Creation")
    for i in range(5):
        test()
print("Collecting..")
n = gc.collect()
print("Unreachable objects collected by GC:", n)
print("Uncollectable garbage list:", gc.garbage)
if __name__ == "__main__":
    main()
    sys.exit()