def any_lowercase5(s):
     for c in s:
          if not c.islower():
               return False
     return True

verify = any_lowercase5('v123a')
print(verify)
