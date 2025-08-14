
#Algorithms Visuals
def bubble_sort(a):
  arr = a.copy()
for i in range(len(arr)-1):
  for j in range(len(arr) - i - 1):
    if arr[j] > arr[j+1]:
      arr[j], arr[j+1] = arr[j + 1], arr[j]
return arr
      
      

def insertion_sort(a):

def merge_sort(a):

def quick_sort():

if __name__ == "__main__":
  test_arr = [2, 5, 4, 7, 8, 3, 2]
  print("original_array:"，test_arr)
  sorted_arr = bubble_sort(test_arr)
  print("sorted array:", sorted_arr)
  # 1.primary sequence
  arr =[3, 1, 2, 5, 4]
  assert bubble_sort(arr) = sorted(arr)
  # 2.reverse sequence
  arr = [5,4,3,2,1]
  assert bubble_sort(arr) = sorted(arr)
  # 3. sequence with repeat element
  arr = [1,1,1,1,2]
  assert bubble_sort(arr) = sorted(arr)
  # Unchanged original array
  arr = [3,1,2,5,4]
  orig = arr.copy()
  bubble_sort(arr)
  assert arr == orig
