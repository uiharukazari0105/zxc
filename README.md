# <font color=pink>zxc<font>模块 帮助文档

### 编写目的 ###

* 有些简单的函数经常使用，整理成模块方便调用
* 复杂函数依赖库多，在模块中拆成多个小函数，部分整合成大函数有助于提升效率
* 自己写的第一个模块，了解模块制作并实践一下？
* 模块名称自然用了老婆名字的缩写哟

### 模块特征 ###

* 函数的命名以其存在的细分py文件为首，作用为尾，例：作用为y的函数来自x.py，则名称为x_y()

### 声明 ###

* 随包颁发麻省理工学院（MIT）许可证，为开源模块
* 代码中可能会存在很多不足之处，望理解与指出，精益求精是我对该模块的执着追求

### 特别感谢 ###

* borax
* datetime
* pyautogui
* pywin32
* pandas
* openpyxl
* opencv-python
* win32gui
* 特别感谢以上这些模块的作者，本模块离不开你们的贡献
* 以上排列不分先后

### 运行环境 ###

``` python
#!/usr/bin/env python3
```

### 使用编码 ###

``` python
# -*- coding: utf-8 -*-
``` 

### 模块目录结构 ###

  <br>zxc
  <br>│ LICENSE
  <br>│ README.md
  <br>│ setup.py
  <br>├─demos
  <br>└─zxc
  <br>  ├─csv.py
  <br>  ├─debug.py
  <br>  ├─file.py
  <br>  ├─img.py
  <br>  ├─keyboard.py
  <br>  ├─mouse.py
  <br>  ├─password.py
  <br>  ├─path.py
  <br>  ├─system.py
  <br>  ├─time.py
  <br>  ├─tool.py
  <br>  ├─window.py
  <br>  ├─xlsx.py
  <br>  └─__init__.py

### GitHub URL ###

[点击访问](https://github.com/uiharukazari0105/zxc)

### 更新、程序开发进度 ###

* 更新日志

    * 第一次大更新
        * 更新日期：2021/11/28
        * 从无到有，建立工程
        * 大致确定了制作与更新的方向
        * 对前代模块进行了BUG修复与整理

    * 第一次大更新补丁
        * 更新日期：2021/11/28
        * 连夜更新，为解决一个导入问题
    * 第二次大更新
        * 更新日期：2021/12/01
        * 建立了keyboard.py
        * 建立了window.py
        * 更新了mouse.py
        * 因为上面三条原因，多了一堆新函数
    * 第三次大更新[测试版本]
        * 更新日期：2021/12/28
        * 建立了img.py
        * 更新了path.py
        * 更新了time.py并修复time_now_get函数与time_change_stamp函数的月、日两项精度输出错误的BUG
        * 修复了mouse.py下错误的函数名"mouse_get_positon"改为"mouse_get_position"
    * 第三次大更新补丁1[测试版本]
        * 更新日期：2021/12/28
        * 修复了关于农历含时间精度函数无法返回中文时间的BUG
    * 第三次大更新补丁2[测试版本]
        * 更新日期：2021/12/29
        * 修复了关于window.py未导入win32gui库的错误
    * 第四次大更新[测试版本]
        * 更新日期：2021/12/31
        * 更新了debug.py
        * 排查了V2.0.2无法正常安装的原因，原因是win32gui在python3.7以上版本被整合入pywin32模块
        * 由于上述原因，我们将从setup.py中移除对win32gui的依赖指示，若仍在使用python3.7以下版本，请手动安装win32gui模块
    * 第四次大更新补丁
        * 更新日期：2021/12/31
        * 修复了关于window.py未导入win32con库的错误
        * 双旦将至，节日快乐
    * V1.0
        * 更新日期：2022/2/？？？？？？？
        * 新增密码服务password.py
        * 新增操作系统服务system.py
        * 新增常用工具tool.py
        * 更新许可证
### 函数功能详细介绍  ###

---        

            * debug_normal：普通调试
                * 功能
                    * 传入一个字符串，在其最前方加入[DEBUG]字样
                    * 这样做虽然需要给每个语句加入注释
                    * 但能方便找出具体错误位置和原因
                    * 也可做成日志系统
                * 用法
                    * debug_normal(调试提示信息)
                * 注意事项
                    * 调试提示信息必须是字符串

---

            * debug_with_time：带时间追踪的调试
                * 功能
                    * 传入一个字符串，在其最前方加入[DEBUG]字样
                    * 相比于debug_normal()，加入了时间戳
                    * 这样做虽然需要给每个语句加入注释
                    * 但能方便找出具体错误位置和原因
                    * 也可做成带时间记录的日志系统
                * 用法
                    * debug_with_time(调试提示信息,时间精度)
                * 注意事项
                    * 调试提示信息必须是字符串
                    * 时间精度必须是字符串，0或1

--- 

            * time_now_get：返回当前已格式化的时间
                * 功能
                    * 该函数提供日期
                    * 通过给定精度参数
                    * 精度表示可使用中文
                    * 返回当前的具体日期
                    * 最终日期数据通过变量now_time返回
                    * 若精度格式存在问题(TI00)会返回错误信息
                * 用法
                    * time_now_get(时间精度) 
                * 注意事项
                    * 时间精度必须是字符串，0或1
                    * 精度格式中文：年、月、日、时、分、秒、毫秒
                    * 精度英文格式：y,month,d,h,m,s,ms
                    * 中文可直接组合，例如：年月日时分秒
                    * 英文组合必须用"."分隔，例如：y,month,d,h,m,s
                    * 精度参数为"0"时相当于返回时分秒
                    * 精度参数为"1"时相当于返回时分秒毫秒                        

---                    

            * mouse_move
                * 功能
                    * 移动光标到指定坐标
                    * 给定三个参数，分别是目标坐标的横纵坐标值以及持续时间
                    * 持续时间可缺省，默认值为0
                * 用法
                    * mouse_move(目标横坐标,目标纵坐标,持续时间(可缺省，默认值为0))
                * 注意事项
                    * 无

---            

            * mouse_click_left
                * 功能
                    * 移动光标到指定坐标并左键单击
                    * 给定两个参数，分别是目标坐标的横纵坐标值
                * 用法
                    * mouse_click_left(目标横坐标,目标纵坐标)
                * 注意事项
                    * 可能需要系统较高权限才对某些程序有效

---            

            * mouse_click_right
                * 功能
                    * 移动光标到指定坐标并右键单击
                    * 给定两个参数，分别是目标坐标的横纵坐标值
                * 用法
                    * mouse_click_right(目标横坐标,目标纵坐标)
                * 注意事项
                    * 可能需要系统较高权限才对某些程序有效                                   

---            

            * mouse_get_position
                * 功能
                    * 返回目前光标的横纵坐标
                * 用法
                    * mouse_get_position()
                * 注意事项
                    * 无

---

            * mouse_drag
                * 功能
                    * 拖拽内容到指定位置
                    * 给定三个参数，分别是目标坐标的横纵坐标值以及持续时间
                    * 持续时间可缺省，默认值为0
                * 用法             
                    * mouse_drag(目标横坐标,目标纵坐标,持续时间(可缺省，默认值为0))
                * 注意事项
                    * 可能需要系统较高权限才对某些程序有效
                    * 拖拽起点为光标当前位置

---

            * mouse_scroll_up
                * 功能
                    * 向上滚动
                    * 给定一个参数，为滚动的像素值
                * 用法             
                    * mouse_scroll_up(滚动的像素值)
                * 注意事项
                    * 无

---

            * mouse_scroll_down
                * 功能
                    * 向下滚动
                    * 给定一个参数，为滚动的像素值
                * 用法             
                    * mouse_scroll_down(滚动的像素值)
                * 注意事项
                    * 无

---

            * path_desktop
                * 功能
                    * 在Windows操作系统下，返回桌面路径
                * 用法
                    * path_desktop(参数缺省)
                * 注意事项
                    * 这在其他操作系统上无法工作

---

            * file_select
                * 功能
                    * 在Windows操作系统下，给定一个主页路径
                    * 打开文件选择器浏览文件
                    * 若直接关闭文件选择器，将无法跳出循环
                * 用法
                    * file_select(文件选择器主页路径)
                * 注意事项
                    * 这在其他操作系统上无法工作

---

            * csv_read_column
                * 功能
                    * 读取csv的某列
                    * 将返回一个列表
                * 用法
                    * csv_read_column(csv文件路径, 要读取的列数,编码)
                * 注意事项
                    * 使用自然计数的列数
                    * 编码缺省则为UTF-8

---

            * time_change_stamp
                * 功能
                    * 将时间戳转换为格式化的时间
                * 用法
                    * time_change_stamp(时间戳, 精度)
                * 注意事项
                    * 时间戳应该为一个整数
                    * 精度格式见time_now_get
                    * 但注意，时间戳将不存在毫秒精度

---

            * file_folder_create_if_non_exist
                * 功能
                    * 检查目录是否存在
                    * 若不存在则创建
                * 用法
                    * file_folder_create_if_non_exist(目录路径)
                * 注意事项
                    * 无

---

            * file_file_create_if_non_exist
                * 功能
                    * 检查文件及其根目录是否存在
                    * 若不存在则创建
                    * 拓展名可缺省
                * 用法
                    * file_file_create_if_non_exist(根目录路径, 文件名, 文件拓展名)
                * 注意事项
                    * 无

---

            * file_list
                * 功能
                    * 给定路径以及文件拓展名
                    * 返回一个含有该目录下指定拓展名的文件的列表
                    * 当文件拓展名参数被缺省时
                    * 将返回一个含有该路径下所有的文件以及文件夹的列表
                * 用法
                    * file_list(路径)
                * 注意事项
                    * 无

---

            * file_file_exist
                * 功能
                    * 检查一个文件是否存在
                    * 若不存在则返回False
                    * 存在则返回True
                * 用法
                    * file_file_exist(文件路径)
                * 注意事项
                    * 无

---

            * xlsx_open
                * 功能
                    * 给定一个xlsx的路径将其打开
                    * 以一个变量返回该文件
                * 用法
                    * xlsx_open(文件路径)
                * 注意事项
                    * 无

---

            * xlsx_open_sheet
                * 功能
                    * 给定一个xlsx
                    * 打开其中的工作表
                    * 若参数sheetname(第二项)缺省，则列出可选内容
                * 用法
                    * xlsx_open_sheet(工作簿, 工作表名称(可缺省))
                * 注意事项
                    * 无

--- 

            * mouse_click_middle
                * 功能
                    * 移动光标到指定坐标并中键单击
                    * 给定两个参数，分别是目标坐标的横纵坐标值
                * 用法
                    * mouse_click_middle(目标横坐标,目标纵坐标)
                * 注意事项
                    * 可能需要系统较高权限才对某些程序有效

---

            * keyboard_type_string
                * 功能
                    * 给定一个字符串，模拟键盘输入
                    * 第二项参数是字符间时间间隔，单位为秒，缺省则默认为0
                * 用法
                    * keyboard_type_string(要模拟输入的字符串, 字符间时间间隔(可缺省，默认为0))
                * 注意事项
                    * 可能需要系统较高权限才对某些程序有效

---

            * keyboard_press
                * 功能
                    * 给定一个按键名或者包含多个按键名的列表
                    * 模拟键盘按键并自动松开
                * 用法
                    * keyboard_press(一个按键名或者包含多个按键名的列表)
                * 注意事项
                    * 可能需要系统较高权限才对某些程序有效
                    * 按键名称应遵循《键盘按键名称表》

---

            * keyboard_down
                * 功能
                    * 给定一个按键名
                    * 模拟键盘按下
                * 用法
                    * keyboard_down(一个按键名)
                * 注意事项
                    * 可能需要系统较高权限才对某些程序有效
                    * 按键名应在字符串内
                    * 按键名称应遵循《键盘按键名称表》

---

            * keyboard_up
                * 功能
                    * 给定一个按键名
                    * 模拟键盘松开
                * 用法
                    * keyboard_up(一个按键名)
                * 注意事项
                    * 可能需要系统较高权限才对某些程序有效
                    * 按键名应在字符串内
                    * 按键名称应遵循《键盘按键名称表》

---

            * keyboard_hotkey
                * 功能
                    * 给定按键名(不定项)，以半角逗号分隔
                    * 模拟键盘热键
                * 用法
                    * keyboard_hotkey(按键1,按键2,······,按键n)
                * 注意事项
                    * 可能需要系统较高权限才对某些程序有效
                    * 按键名应在字符串内
                    * 按键名称应遵循《键盘按键名称表》

---

            * 键盘按键名称表
                * \t, \n, \r,  , !, ", #, $, %, &, "", (, ), *, +, ,, -, .,
              /, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, :, ;, <, =, >, ?, @,
              [, \\, ], ^, _, `, a, b, c, d, e, f, g, h, i, j, k, l,
              m, n, o, p, q, r, s, t, u, v, w, x, y, z, {, |, }, ~,
              accept, add, alt, altleft, altright, apps, backspace, browserback,
              browserfavorites, browserforward, browserhome, browserrefresh, browsersearch,
              browserstop, capslock, clear, convert, ctrl, ctrlleft, ctrlright, decimal,
              del, delete, divide, down, end, enter, esc, escape, execute, f1, f10,
              f11, f12, f13, f14, f15, f16, f17, f18, f19, f2, f20, f21, f22,
              f23, f24, f3, f4, f5, f6, f7, f8, f9, final, fn, hanguel, hangul,
              hanja, help, home, insert, junja, kana, kanji, launchapp1, launchapp2,
              launchmail, launchmediaselect, left, modechange, multiply, nexttrack,
              nonconvert, num0, num1, num2, num3, num4, num5, num6, num7, num8, num9,
              numlock, pagedown, pageup, pause, pgdn, pgup, playpause, prevtrack, print,
              printscreen, prntscrn, prtsc, prtscr, return, right, scrolllock, select,
              separator, shift, shiftleft, shiftright, sleep, space, stop, subtract, tab,
              up, volumedown, volumemute, volumeup, win, winleft, winright, yen, command,
              option, optionleft, optionright

---

            * window_delete_button_close
                * 功能
                    * 删除本窗口的关闭按钮
                * 用法
                    * window_delete_button_close()
                * 注意事项
                    * 每次运行应只使用一次

---

            * window_delete_button_max
                * 功能
                    * 删除本窗口的最大化按钮
                * 用法
                    * window_delete_button_max()
                * 注意事项
                    * 每次运行应只使用一次

---

            * window_delete_button_min
                * 功能
                    * 删除本窗口的最小化按钮
                * 用法
                    * window_delete_button_min()
                * 注意事项
                    * 每次运行应只使用一次

---

            * window_delete_size
                * 功能
                    * 删除本窗口的大小拖动功能
                * 用法
                    * window_delete_size()
                * 注意事项
                    * 每次运行应只使用一次

---

            * window_set_title
                * 功能
                    * 设置本窗口的窗口标题
                * 用法
                    * window_set_title(要设置的窗口标题)
                * 注意事项
                    * 无

---

            * path_user
                * 功能
                    * 在Windows操作系统下，返回用户主目录路径
                * 用法
                    * path_user(参数缺省)
                * 注意事项
                    * 这在其他操作系统上无法工作

---

            * path_documents
                * 功能
                    * 在Windows操作系统下，返回用户文档目录路径
                * 用法
                    * path_documents(参数缺省)
                * 注意事项
                    * 这在其他操作系统上无法工作

---

            * path_downloads
                * 功能
                    * 在Windows操作系统下，返回用户下载目录路径
                * 用法
                    * path_downloads(参数缺省)
                * 注意事项
                    * 这在其他操作系统上无法工作

---

            * path_pictures
                * 功能
                    * 在Windows操作系统下，返回用户图片目录路径
                * 用法
                    * path_pictures(参数缺省)
                * 注意事项
                    * 这在其他操作系统上无法工作

---

            * path_videos
                * 功能
                    * 在Windows操作系统下，返回用户视频目录路径
                * 用法
                    * path_videos(参数缺省)
                * 注意事项
                    * 这在其他操作系统上无法工作

---

            * path_music
                * 功能
                    * 在Windows操作系统下，返回用户音乐目录路径
                * 用法
                    * path_music(参数缺省)
                * 注意事项
                    * 这在其他操作系统上无法工作

---

            * path_favorites
                * 功能
                    * 在Windows操作系统下，返回用户收藏目录路径
                * 用法
                    * path_favorites(参数缺省)
                * 注意事项
                    * 这在其他操作系统上无法工作

---

            * img_read
                * 功能
                    * 给定图片的路径，返回带有图片的变量
                * 用法
                    * img_read(图片路径)
                * 注意事项
                    * 图片路径必须不含中文字符

---

            * img_gray
                * 功能
                    * 给定一张图片，返回转化为灰度图片的该图的变量
                * 用法
                    * img_gray(图片变量)
                * 注意事项
                    * 无

---

            * img_display
                * 功能
                    * 给定一张图片，然后显示
                * 用法
                    * img_display(图片变量, 窗口的标题，缺省则为空, 等待键盘输入以关闭窗口的时间, 单位：秒，缺省则为0，意为无限等待, 执行完成后是否自动关闭窗口，默认为1，意为关闭，0则不关闭)
                * 注意事项
                    * 窗口标题必须不含中文字符

---

            * img_resize
                * 功能
                    * 给定一张图片，转换的目标宽高，返回改变长宽后的图片
                * 用法
                    * img_resize(图片变量, 目标宽度, 目标高度)
                * 注意事项
                    * 无

---

            * time_lunar_now_get
                * 功能
                    * 给定一个时间精度参数(形如:年月日)，若参数以“中”开头则返回中文日期
                    * 返回当前日期下的农历日期
                    * 精度参数缺省则为数字日期
                * 用法
                    * time_lunar_now_get(时间精度(缺省则返回数字日期))
                * 注意事项
                    * 仅支持公历范围1900-2100年

---

            * time_lunar_from_solar
                * 功能
                    * 给定一个时间精度参数(形如:年月日)，若精度参数以“中”开头则返回中文日期，以及公历年月日
                    * 返回给定的公历日期对应的农历日期
                    * 精度参数缺省则为数字日期
                * 用法
                    * time_lunar_from_solar(公历日期年份, 公历日期月份, 公历日期日, 时间精度(缺省则返回数字日期))
                * 注意事项
                    * 仅支持公历范围1900-2100年

---

            * time_lunar_now_get_animal
                * 功能
                    * 获取当前农历日期对应的的属相
                * 用法
                    * time_lunar_now_get_animal(参数缺省)
                * 注意事项
                    * 仅支持公历范围1900-2100年

---

            * time_lunar_from_solar_animal
                * 功能
                    * 给定一个公历日期，返回对应农历日期对应的的属相
                * 用法
                    * time_lunar_from_solar_animal(公历日期年份, 公历日期月份, 公历日期日)
                * 注意事项
                    * 仅支持公历范围1900-2100年

---

            * time_lunar_to_solar
                * 功能
                    * 给定一个农历日期，返回对应公历日期
                * 用法
                    * time_lunar_from_solar_animal(农历日期年份, 农历日期月份, 农历日期日)
                * 注意事项
                    * 仅支持公历范围1900-2100年

---

            * debug_error_notice
                * 功能
                    * 给定错误来源和错误提示内容，将给予相应提示
                    * 返回错误信息字符串，仅在印屏幕参数为0或2时生效
                * 用法
                    * debug_error_notice(错误来源,仅在passage参数不为空时允许缺省, 错误提示内容,仅在passage参数不为空时允许缺省, 错误提示的头部文字，若缺省则使用DEBUG功能的默认头部‍，且此时参数source、text不允许缺省, 是否输出为印屏幕，1为是，0为否，若缺省则印屏幕，2为印屏幕同时返回，否则返回为字符串)
                * 注意事项
                    * 无

---

            * password_get
                * 功能
                    * 给定一个提示信息，程序将提供密码输入栏
                    * 用户输入回车标定为密码输入完成
                    * 用户输入退格删除一个字符
                    * 用户输入Esc清空密码栏
                    * 返回用户确认完成的密码
                * 用法
                    * password_get(密码提示信息)
                * 注意事项
                    * 无

---

            * system_type_get
                * 功能
                    * 参数缺省
                    * 返回操作系统的类型
                    * 在Windows平台下返回"Windows"
                    * 在Linux平台下返回"Linux"
                    * 在MacOS平台下返回"MacOS"
                    * 在其他平台下返回"Other"
               * 用法
                   * system_type_get(参数缺省)
               * 注意事项
                   * 无

---

            * system_type_detail_get
                * 功能
                    * 参数缺省
                    * 返回具体操作系统的类型
               * 用法
                   * system_type_detail_get(参数缺省)
               * 注意事项
                   * 无

---

            * tool_shutdown_computer
                * 功能
                    * 给定一个时间，单位为分钟，将在该时间后关闭计算机，若缺省则为0
                    * 仅在遇到不支持的操作系统时返回提示信息
               * 用法
                   * tool_shutdown_computer(剩余关机时间，若缺省则为0)
               * 注意事项
                   * 目前仅支持Windows、Linux、MacOS

---
                         
<center>Copyright © zxc
2021-2022</center>