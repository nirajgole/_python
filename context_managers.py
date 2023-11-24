#python context managers
# usage: file management, database sessions

class MyContextManger():
    """creating custom context manager"""
    # def __init__(self) -> None:
    #     print('Inside init method.')

    def __enter__(self):
        print('Inside enter method.')

    def __exit__(self,exc_type,exc_value,exc_traceback):
        print('Inside exit method.')

with MyContextManger() as mcm:
    print('Inside my context manager.')
