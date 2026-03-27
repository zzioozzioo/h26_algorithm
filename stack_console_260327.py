def push_data(top):
    data = int(input('> 데이터 입력 : '))
    if not isFull(top):
        stack.append(data)
        top += 1

def pop_data(top):
    if not isEmpty(): 
        top -= 1
        print(f'> 가져온 데이터 : {stack.pop()}')
        return

def peek_data():
    if not isEmpty():
        print(f'> 가져올 데이터 : {stack[top]}')

def isFull(top):
    if top == 4:
        print('> Stack이 차 있어서 더 이상 추가할 수 없습니다.')
        return True
    return False

def isEmpty():
    if len(stack) == 0:
        print('> Stack이 비어 있습니다.')
        return True
    return False

def exit_program():
    print('----------[ 정수형 스택 연산 실습 종료]---')


stack = []
top = -1

print('--------[ 정수형 스택 연산 실습 (용량 5)]')
while True:
    
    # 메뉴 선택
    print('========================================')
    print(' 1. Push   2. Pop    3. Peek   0. Exit')
    print('========================================')
    menu = int(input('> 메뉴 선택 : '))

    # push
    if menu == 1:
        push_data(top)
        print(f'> 현재 스택 상태  {stack}')
        print()

    # pop
    elif menu == 2:
        pop_data(top)
        print(f'> 현재 스택 상태  {stack}')
        print()

    # peek
    elif menu == 3:
        peek_data()
        print(f'> 현재 스택 상태  {stack}')
        print()

    # exit
    elif menu == 0:
        exit_program()
        break