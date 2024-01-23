#python标识符的命名规范
    #模块名尽量短小，并且全部使用小写字母，可以使用下划线分割多个字母。例如：grame_main
    #包名尽量短小，并且全部使用小写字母，不推荐使用下划线。例如：com.fanballpython
    #类名采用单词首字母大写形式(Pascal风格)。例如：MyClass
    #模块内部的类采用“_”+Pascal风格的类名组成。例如：在MyClass中的内部类_InnerMyClass
    #函数、类的属性和方法的命名，全部使用小写字母，多个字母之间使用下划线分割
    #常量命名时采用全部大写写字母，可以使用下划线
    #使用单下划线“_”开头的模块变量或函数是受保护的，在使用“from xxx import *”语句从模块中导入时，这些模块变量或函数不能被导入
    #使用双下划线“_”开头的实例变量或方法是类私有的
    #以双下划线开头和结尾的是python的专用标识。例如：__init__()表示初始化函数