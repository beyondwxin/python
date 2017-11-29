#!/usr/bin/env python3
'''单元测试'''
import unittest
import sys
import sql
sys.path.append("E:/vs_space/demo/aa/")
# from sql import User
# from sql import insertToDb

__author__ = 'KING'


class TestDb(unittest.TestCase):
    '''单元测试类'''

    def setUp(self):
        print('开始测试...')


    def test_insertDb(self):
        '''测试增加user'''
        newUser = sql.User('1', 'king')
        sql.insertToDb(newUser)

    def test_deleteDb(self):
        '''测试删除user'''
        # user = sql.User('1', 'king')
        sql.deleteToDb()

    def tearDown(self):
        print('测试结束...')


if __name__ == '__main__':
    unittest.main()