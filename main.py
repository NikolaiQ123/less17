from function_add.funcion_add import add as a_dd


def main():
    '''
    start our project

    '''

    assert a_dd(1, 2) == 3
    assert a_dd(3, 2) == 5
    assert a_dd(2, 2) == 4

    a, b = map(int, input('Eneter your a & b: ').split())
    print(a_dd(a, b))


if __name__ == '__main__':
    main()
