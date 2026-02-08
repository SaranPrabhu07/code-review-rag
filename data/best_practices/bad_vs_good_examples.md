Bad:
for i in range(len(arr)):
    if arr[i] == target:
        return True

Better:
if target in arr:
    return True
