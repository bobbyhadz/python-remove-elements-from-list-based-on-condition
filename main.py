# Remove elements from list based on a condition in Python

my_list = [22, 55, 99, 105, 155, 205]

new_list = [item for item in my_list if item > 100]
print(new_list)  # 👉️ [105, 155, 205]