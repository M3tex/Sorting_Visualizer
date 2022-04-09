# A sorting algorithm visualizer
from tkinter import Tk, Frame, BOTH, TOP, BOTTOM, HORIZONTAL, Canvas, Button, Scale
from random import randrange, shuffle
from time import sleep


WIDTH = 1080
HEIGHT = 720


class Visualizer(Frame):
    """Handles all UI related methods"""

    def __init__(self, master):
        """Initializes the visualizer"""
        self.master = master
        self.array = self.__initArray__()
        self.selectedFunc = self.quickSort
        Frame.__init__(self, master)
        self.__initUI__()
    

    def __initUI__(self):
        self.master.title("Sorting Algorithm Visualizer")
        self.pack(fill=BOTH, expand=1)
        self.master.resizable(width=False, height=False)
        

        self.canvas = Canvas(self, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack(fill=BOTH, side=TOP)

        # Buttons
        visualize_button = Button(self, text="Visualize", command=self.__visualize)
        visualize_button.pack(fill=BOTH, side=BOTTOM, expand=True)

        reset_button = Button(self, text="Reset", command=self.__reset)
        reset_button.pack(fill=BOTH, side=BOTTOM, expand=True)

        self.w = Scale(self, from_=30, to=300, orient=HORIZONTAL)
        self.w.set(165)
        self.w.pack(fill=BOTH, side=BOTTOM, expand=True)

        # Show informations on screen
        self.__drawArray__(self.array)


    def __initArray__(self, N=165):
        """Initializes the array"""
        result = []
        for i in range(N):
            result.append(i)
        shuffle(result)
        return result


    def __drawArray__(self, arr):
        """Draws the array"""
        self.canvas.delete("all")
        maxW = WIDTH / len(arr)
        maxH = HEIGHT / self.w.get()

        for i in range(len(arr)):
            self.canvas.create_rectangle(i*maxW, HEIGHT + 1, (i+1)*maxW, 5 + maxH * arr[i], fill="white")
        self.canvas.update()


    def __visualize(self):
        """Visualizes the algorithm"""
        self.selectedFunc(self.array, 0, len(self.array)-1)
        pass

    
    def __reset(self):
        """Reset the UI"""
        self.array = self.__initArray__(self.w.get())
        self.__drawArray__(self.array)
        pass

    
    def bubbleSort(self, arr, low, high):
        """Bubble Sort implementation (low and high are not used, just to avoid errors)"""
        n = len(arr)
    
        for i in range(n-1):
            for j in range(0, n-i-1):
                if arr[j] > arr[j + 1] :
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    self.__drawArray__(arr)
    

    def selectionSort(self, arr, low, high):
        """Selection Sort implementation (low and high are not used, just to avoid errors)"""
        for i in range(len(arr)):
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            self.__drawArray__(arr)
    

    def insertionSort(self, arr, low, high):
        """Insertion Sort implementation (low and high are not used, just to avoid errors)"""
        for i in range(1, len(arr)):
    
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j] :
                    arr[j + 1] = arr[j]
                    self.__drawArray__(arr)
                    j -= 1
            arr[j + 1] = key


    def mergeSort(self, arr, low, high):
        """Merge Sort implementation (low and high are not used, just to avoid errors)"""
        # WARNING: Currently not working
        if len(arr) > 1:
            # Finding the mid of the array
            mid = len(arr)//2
    
            # Dividing the array elements
            L = arr[:mid]
    
            # into 2 halves
            R = arr[mid:]
    
            # Sorting the first half
            self.mergeSort(L)
    
            # Sorting the second half
            self.mergeSort(R)
            i = j = k = 0
    
            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
    
            # Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
    
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
    

    def partition(self, arr, low, high):
        """A helper function for quickSort"""
        i = (low-1)         # index of smaller element
        pivot = arr[high]     # pivot
    
        for j in range(low, high):
    
            # If current element is smaller than or
            # equal to pivot
            if arr[j] <= pivot:
    
                # increment index of smaller element
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
                self.__drawArray__(arr)
    
        arr[i+1], arr[high] = arr[high], arr[i+1]
        self.__drawArray__(arr)
        return (i+1)
    
    
    def quickSort(self, arr, low, high):
        """Quick Sort implementation"""
        if len(arr) == 1:
            return arr
        if low < high:
    
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.partition(arr, low, high)
    
            # Separately sort elements before
            # partition and after partition
            self.quickSort(arr, low, pi-1)
            self.quickSort(arr, pi+1, high)
            #self.__drawArray__(arr)


root = Tk()

Visualizer(root)
root.mainloop()