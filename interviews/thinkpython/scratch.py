# # recusrsion
def countdown(n):
    if n<0:
        print('Boom...')
    else:
        print(n)
        countdown(n-1)

num = int(input('Enter your countdown number'))
countdown(num)
