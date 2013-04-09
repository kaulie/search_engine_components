#-*- coding: utf8 -*-

'''
Created on 2013-4-9

@author: gl
'''
from apps.model.exchangemodel import ExchangeActivitie

class Finite_State_Machine():
    '''
        有限状态机
    '''
    
    def __init__(self,obj_type,entrance_state,exit_state,state_pool):
        self._obj_type = obj_type
        assert isinstance(entrance_state,State)
        assert isinstance(exit_state,State)
        self._entrance_state = entrance_state
        self._exit_state = exit_state
        self._state_flows = []
        self._state_pool = state_pool
        
    def _check(self):
        '''
            校验是否合理
            规则1:exit_state 生命周期结束
            规则2：不能有dead loop，从一个状态出发，必须能找到一条路径到达exit_state
        '''
        pass
    
        
    def append_state_flow(self,state_flow):
        assert isinstance(state_flow,State_Flow)
        assert state_flow._obj_type == self._obj_type
        self._state_flows.append(state_flow)
        

class State():
    
    def __init__(self,name,value='',comment=''):
        self.name = name
        self.value = value if value else name
        self.comment = comment

class State_Flow(object):
    '''
        代表了事物一个从状态到另一个状态的变化过程
    '''
    def __init__(self,obj_type,keyname,state_in,state_out,fn_callback=None):
        '''
            obj_type:对象的类型
            keyname:关键字，用来标识操作行为
            state_in:进入状态
            state_out:出去状态
        '''
        assert isinstance(state_in,State)
        assert isinstance(state_out,State)
        assert keyname != None
        assert state_in.value != state_out.value
        self._obj_type = obj_type
        self.keyname = keyname
        self.state_in = state_in
        self.state_out = state_out
        self.fn_callback = fn_callback
        
    def _check_on_turn(self):
        '''
            状态转变时的校验
        '''
        pass


class Base_Finite_State_Object(object):
    '''
        状态变换对象的基类
    '''
    
    pass
