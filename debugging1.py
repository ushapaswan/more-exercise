def numbers_less_than_twenty(list):
  print(num_list)
  counter = 0
  while counter < len(list):
    item = list[counter]
    if item > 20:
      list.remove(item)
    else:
      counter += 1
  return list
num_list=[12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]
num_list_sub_20=numbers_less_than_twenty(num_list)

# print(num_list)
print(num_list_sub_20)

