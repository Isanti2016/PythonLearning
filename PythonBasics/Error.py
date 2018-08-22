# -*- coding:utf-8 -*-
import logging

def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2

def main(s):
    try:
        print('try...')
        bar(s)
        print('bar:')
    except ValueError as e:
        print('ValueError:',e)
    except ZeroDivisionError as e:
        print('ZeroDivisionError:',e)
        logging.exception(e)
    else:
        print('no error!')
    finally:
        print('finally...')


if __name__=='__main__':
    main(2)
    main(0)
    print('end')
