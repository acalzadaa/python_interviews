
def tribonacci(signature, n):

    # check signature:
    if(signature[0] <= signature[1] <= signature[2] and n > 0):
        if n < 3:
            return signature[0:n-1]
        if n == 3:
            return signature
        else:
            sums = signature[len(signature)-1] + signature[len(signature)-2] + signature[len(signature)-3]
            signature.append(sums)
            return tribonacci(signature, n-1)
    else:
        return []
