def numOfPairs(nums,target):
    container, res = {}, 0
    tlen = len(target)
    for i in range(len(nums)):
        ilen = len(nums[i])
        if target[:ilen] == nums[i] and target[ilen:] in container:
            print('1st entry')
            res += container[target[ilen:]]
        if target[tlen - ilen:] == nums[i] and target[:tlen - ilen] in container:
            print('2nd entry')
            res += container[target[:tlen - ilen]]
        container[nums[i]] = container.get(nums[i], 0) + 1
        print('end')
    return res


print(numOfPairs(['777','7','77','77'],'7777'))