# -*- coding:utf-8 -*-

class Screen(object):

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,value):
        if not isinstance(value,(int,float)) or value<0:
            raise ValueError("Variable width must be float or int")
        self.__width==value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self,value):
        if not isinstance(value,(int,float)) or value<0:
            raise ValueError("Variable height must be float or int")
        self.__height=value

    @property
    def resolution(self):
        return self.__resolution
