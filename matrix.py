mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
new_list=[]
for i in range(len(mat)):
  for j in range(len(mat[i])):
      if len(mat[j])<=len(mat[i]):
          new_list.append(mat[i][j])
          print(new_list)
          
   

