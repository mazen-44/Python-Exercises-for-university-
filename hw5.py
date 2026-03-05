main_list = [10,20]
ref_list = main_list
ref_list.append(30)
print("After appending :")
print("main list : ",main_list)
print("reference list : ",ref_list)
copy_list = main_list.copy()
copy_list.append(40)
print("After copying :")
print("main list : ",main_list)
print("reference list : ",copy_list)