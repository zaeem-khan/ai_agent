from functions.write_file_content import write_file

print("Test 1")
result_one = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print(result_one)

print("Test 2")
result_two = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print(result_two)

print("Test 3")
result_three = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print(result_three)


