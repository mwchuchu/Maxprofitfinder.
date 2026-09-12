list=[1,2,3,4,5,6,7,8,9]

key=6
index=0
sub_list=list[index:key]
max_profit=0
sum=0
month=6


while(len(sub_list) == key ):
  
  sum=0
  for sub in sub_list:
    sum=sub+sum
  if sum > max_profit:
    max_profit = sum

  index=index+1
  month=month+1
  sub_list=list[index:month]



print(max_profit)
