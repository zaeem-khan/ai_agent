from functions.get_files_info import get_files_info
print("Test 1")
result_one = get_files_info("calculator", ".")
print(result_one)

print("Test 2")
result_two = get_files_info("calculator", "pkg")
print(result_two)

print("Test 3")
result_three = get_files_info("calculator", "/bin")
print(result_three)

print("Test 4")
result_four = get_files_info("calculator", "../")
print(result_four)

