import vt
import os

client = vt.Client("[virus total API key]")



# folder path
dir_path = r'/path/to/files'

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)


for i in res:
    with open(i, "rb") as f:
        print(i)
        analysis = client.scan_file(f, wait_for_completion=True)
        result =  analysis.to_dict() 
        print("Number of malicious matches")
	    print(result['malicious'])
        print("Number of undetected matches")
	    print(result['undetected'])
