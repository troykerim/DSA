class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        if 0 <= i < self.size:
            return self.arr[i]
        raise IndexError("Index out of bounds")

    def set(self, i: int, n: int) -> None:
        if 0 <= i < self.size:
            self.arr[i] = n
        else:
            raise IndexError("Index out of bounds")

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        if self.size == 0:
            raise IndexError("Array is empty")
        self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [0] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
    
    def printArray(self) -> None:
        print([self.arr[i] for i in range(self.size)])


def main():
    da = DynamicArray(2)  # start with small capacity for testing
    
    while True:
        print("\nSelect an operation:")
        print("1. Get value at i-th index")
        print("2. Set value at i-th index")
        print("3. Push value at the end")
        print("4. Pop last value")
        print("5. Get current size")
        print("6. Get capacity")
        print("7. Print array")
        print("q. Quit")

        sel = input("Enter choice: ").strip()

        if sel == '1':
            i = int(input("Enter index: "))
            try:
                print("Value:", da.get(i))
            except Exception as e:
                print(e)

        elif sel == '2':
            i = int(input("Enter index: "))
            val = int(input("Enter value: "))
            try:
                da.set(i, val)
            except Exception as e:
                print(e)

        elif sel == '3':
            val = int(input("Enter value: "))
            da.pushback(val)

        elif sel == '4':
            try:
                print("Popped:", da.popback())
            except Exception as e:
                print(e)

        elif sel == '5':
            print("Size:", da.getSize())

        elif sel == '6':
            print("Capacity:", da.getCapacity())

        elif sel == '7':
            da.printArray()

        elif sel == 'q':
            print("Exiting program!")
            break

        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
