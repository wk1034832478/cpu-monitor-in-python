class Cpu:
    """
        Cpu类封装了系统运行时cpu的状态,可以通过该类来获取当前系统状态
    """

    # 当前用户cpu使用率
    __user_usage = 0
    # 系统cpu使用lv
    __sys_usage = 0
    # 总使用率
    __usage = 0

    def __init__(self, id = None, name = "未命名cpu"):
        # 私有属性__id, cpu的id
        self.__id = id
        self.__name = name
    
    @property
    def usage(self):
        if not self.__usage:
            return 0.0
        else:
            return self.__usage
    
    @usage.setter
    def usage(self, value):
        if not isinstance(value, float):
            raise ValueError('cpu使用率必须是float类型')
        if value > 1 and value < 0:
            raise ValueError('cpu使用率必须在0-1之间')
        self.__usage = value
    
    @property
    def user_usage(self):
        if not self.__user_usage:
            return None
        else:
            return self.__user_usage
    
    @user_usage.setter
    def user_usage(self, value):
        if not isinstance(value, float):
            raise ValueError('cpu使用率必须是float类型')
        if value > 1 and value < 0:
            raise ValueError('cpu使用率必须在0-1之间')
        self.__user_usage = value

    # 设置只读属性 getter
    @property
    def id(self):
        if self.__id:
            return self.__id
        else:
            None

    # 设置setter函数
    @id.setter
    def id(self, id):
        # 检查类型, 传入的id必须是整数类型
        if not isinstance(id, int):
            raise ValueError('传入的id必须是整数类型!')
        else:
            self.__id = id
    
    # 设置只读属性 getter
    @property
    def name(self):
        if self.__name:
            return self.__name
        else:
            None

    # 设置setter函数
    @name.setter
    def name(self, name):
        # 检查类型, 传入的name必须是字符串类型性
        if not isinstance(name, str):
            raise ValueError('传入的name必须是字符串类型类型!')
        else:
            self.__name = name