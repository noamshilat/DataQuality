def israeli_tz_validation(tz):
    digits_after_multiplication = []
    tz = str(tz)
    if tz.isnumeric() is True:
        if len(tz) < 9:
            tz = tz.zfill(9)   
        check_digit = tz[-1]
        tz = tz[:-1]
        for index,digit in enumerate(tz):
            if index % 2 == 0:
                var = 1 * int(tz[index])
                digits_after_multiplication.append(int(var))
            else:
                var = 2 * int(tz[index])
                if int(var) > 9:
                    to_sum = []
                    for digit in str(var):
                        to_sum.append(int(digit))
                    digits_after_multiplication.append(sum(to_sum))
                else:
                    digits_after_multiplication.append(var)
        summarized_digits = sum(digits_after_multiplication)
        if (summarized_digits + int(check_digit)) % 10 == 0:
            return True
        else:
            return False
    else: 
        return False
