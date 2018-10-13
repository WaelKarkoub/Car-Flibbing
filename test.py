import pickle

# try:
#     with open(ranges, 'rb') as f:
#         k = pickle.load(ranges)
#         print('file found')

#     finalRange = list(range(max(k)+1,300000))
#     listRange = k + finalRange
# except Exception as e:
#     listRange = list(range(93000,300000))
#     print('file not found')

ranges = 'idList.txt'

with open(ranges, 'rb') as f:
    k = pickle.load(f)
    print('file found')