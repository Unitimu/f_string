def multi_table(n):
    x=''
    for y in range(1,11):
        x += f'{y} * {n} = {y*n}\n'

    return x.strip('\n')
        
def multi_table(n):
    return '\n'.join(f'{i} * {n} = {i * n}' for i in range(1, 11))
