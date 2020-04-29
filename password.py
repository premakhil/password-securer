# import requests
# import hashlib
# import sys

# def api_requests(password):
#     url = 'https://api.pwnedpasswords.com/range/' + password
#     res = requests.get(url)
#     if res.status_code != 200:
#         raise RuntimeError(f'Error fetching {res.status_code}. Check the API and try again. ')
#     return res


# def hashing_func(password):
#     sha1p = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
#     get_5 = sha1p[:5]
#     tail = sha1p[5:]
#     response = api_requests(get_5)
#     return match_func(response,tail)
    
    
# def match_func(hashes, hash_tail):
#     hashes = (line.split(':') for line in hashes.text.splitlines())
#     for i, count in hashes:
#         if i == hash_tail:
#             return count
#     return 0
   

# def main(password):
#     for j in password:
#         count = hashing_func(j)
#         if count:
#             print(f'{j} was hacked {count} number of times. Please try a different one. ')

#         else:
#             print(f'{j} was never hacked. Go ahead! ')



# main(sys.argv[1:])

a = 'hello'
b = 'hell'
if a == b:
    print('yes')

else:
    print('no')