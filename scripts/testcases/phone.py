#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d

class PhoneTest(unittest.TestCase):
    def setUp(self):
        super(PhoneTest, self).setUp()
        d.wakeup()
        #d.start_activity(action='android.intent.action.DIAL', data='tel:13581739891', flags=0x04000000)
        d.press('back')\
         .press('back')\
         .press('home')

    def tearDown(self):
        super(PhoneTest, self).tearDown()
        d.press('back')\
         .press('back')\
         .press('back')\
         .press('home')

    def testCall(self):
        assert d.exists(text='Phone') , 'Phone app not appear on home screen'
        #assert d.exists(text='Apps')
        d(text='Phone').click.wait()
        d(description='one').click()
        d(description='zero').click()
        d(description='zero').click()
        d(description='eight').click()
        d(description='six').click()
        assert d.exists(text="10086")
        if d.exists(description='dial'):
            d(description='dial').click.wait()
        assert d(text="Dialing").wait.exists(timeout=10000), 'call not connected in 10 secs'
        assert d(text="0:10").wait.exists(timeout=20000), 'call duration should be 10 secs'
        d(className='android.widget.Button', index=1).click.wait()
        assert d(description='dial').wait.exists(timeout=3000)
            


