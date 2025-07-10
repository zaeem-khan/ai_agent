from functions.run_python import run_python_file

print("Test 1")
result_one = run_python_file("calculator", "main.py")
print(result_one)

print("Test 2")
result_two = run_python_file("calculator", "tests.py")
print(result_two)

print("Test 3")
result_three = run_python_file("calculator", "../main.py")
print(result_three)

print("Test 4")
result_four = run_python_file("calculator", "nonexistent.py")
print(result_four)


