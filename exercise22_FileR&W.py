with open('TEST_FILE.txt','r') as f:
    print(f.read())
    print(f.tell())
    
    f.seek(0)

    print(f.readlines())
    print(f.tell())

with open('TEST_FILE.txt','a') as f:
    f.write('\nAdditional content')

with open('TEST_FILE.txt','r') as f:
    print(f.read())
