import sys
print(type(sys.argv))
print(sys.argv)     # Arguments are string by default

fileName = sys.argv[0]
occ = fileName.split("/")
print("File Name: {}".format(occ[len(occ)-1]))