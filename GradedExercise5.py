#file objects

with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

with open ('test_copy.txt', 'r') as rf2:
    result = rf2.read()
    print(result)
    
