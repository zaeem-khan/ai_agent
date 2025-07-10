from functions.get_file_content import get_file_content

print("Test 1")
result_one = get_file_content("calculator", "main.py")
print(result_one)

print("Test 2")
result_two = get_file_content("calculator", "pkg/calculator.py")
print(result_two)

print("Test 3")
result_three = get_file_content("calculator", "/bin/cat")
print(result_three)


