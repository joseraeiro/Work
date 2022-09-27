import vt
import os

client = vt.Client("[VirusTotal API key]")

dir_path = r'path/to/files'

res = []

for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)

for i in res:
    with open(i, "rb") as f:
        print(i)
        analysis = client.scan_file(f, wait_for_completion=True)
        result =  analysis.to_dict()
        filtered_list = ['malicious', 'undetected']
        def seek_keys(d, key_list):
            for k, v in d.items():
                if k in key_list:
                    if isinstance(v, dict):
                        print(k + ": " + list(v.keys())[0])
                    else:
                        print(k + ": " + str(v))
                if isinstance(v, dict):
                    seek_keys(v, key_list)

    (seek_keys(result, filtered_list))
