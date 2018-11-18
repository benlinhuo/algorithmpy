
#!/usr/bin/python3

# 鸡尾酒排序
def cocktailBubbleSore(arr):
     left = 0;
     right = len(arr) - 1;
     while(left < right):
         for i in range(left, right):
             if arr[i] > arr[i+1]:
                 (arr[i+1], arr[i]) = (arr[i], arr[i+1])
         right -= 1;
         # python range 方法从大到小，它默认不会自动减1，需要手动指定-1（第三个参数：间隔）
         for j in range(right, left, -1):
             if arr[j] < arr[j-1]:
                 (arr[j-1], arr[j]) = (arr[j], arr[j-1])
         left += 1;
     else:
         print("sort  end !!!!!")
     return arr;

retSort = cocktailBubbleSore([1, 5, 8, 10, 2, 4, 8, 0]);
print(retSort)

retSort1 = cocktailBubbleSore([1, 8, 10, 5, 4, 2, 4, 8, 0]);
print(retSort1)