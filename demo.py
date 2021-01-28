import wx


class LoginPage(wx.Frame):
    """ 登录页面 """

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500, 400))

        self.SetMaxSize((500, 400))
        self.SetMinSize((500, 400))
        self.panel = None
        self.text_user = None
        self.text_pwd = None
        self.text_keyword = None
        self.init_ui()
        self.Show(True)

    def init_ui(self):
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour((255, 255, 255))
        self.panel.Refresh()

        # 账户、密码输入框
        title = wx.StaticText(self.panel, label="请输入用户名和密码", pos=(140, 55))
        title.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT,
                              wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        wx.StaticText(self.panel, label="用户名", pos=(120, 125))
        self.text_user = wx.TextCtrl(self.panel, pos=(180, 120), size=(200, 25), style=wx.TE_LEFT)
        wx.StaticText(self.panel, label="密码", pos=(120, 160))
        self.text_pwd = wx.TextCtrl(self.panel, pos=(180, 155), size=(200, 25), style=wx.TE_PASSWORD)
        wx.StaticText(self.panel, label="关键字", pos=(120, 195))
        self.text_keyword = wx.TextCtrl(self.panel, pos=(180, 190), size=(200, 25), style=wx.TE_LEFT)

        # 设置按钮
        bt_confirm = wx.Button(self.panel, label='确定', pos=(120, 250), style=wx.NO_BORDER)
        bt_confirm.Bind(wx.EVT_BUTTON, self.onclick_submit)
        bt_confirm.SetBackgroundColour("Blue")
        bt_confirm.SetForegroundColour("White")
        bt_cancel = wx.Button(self.panel, label='取消', pos=(213, 250), style=wx.NO_BORDER)
        bt_cancel.Bind(wx.EVT_BUTTON, self.onclick_cancel)
        bt_registered = wx.Button(self.panel, label='注册', pos=(305, 250), style=wx.NO_BORDER)
        bt_registered.Bind(wx.EVT_BUTTON, self.onclick_registered)

    def onclick_submit(self, event):
        """ 点击登录页面确认按钮 """
        username = self.text_user.GetValue()
        password = self.text_pwd.GetValue()
        keyword = self.text_keyword.GetValue()

        if username == "" or password == "":
            message = "用户名或密码不能为空"
            # 此处需要链接数据库，判断用户名密码是否有匹配，是否正确
        elif keyword == "":
            message = "请输入查询关键字"
        else:
            message = "登陆成功！正在查询"

        wx.MessageBox(message)
        if message == "登陆成功！正在查询":
            self.successfullyLogin()

    def onclick_cancel(self, event):
        """ 点击登录页面取消按钮 """
        self.Close()

    def onclick_registered(self, event):
        """ 点击登录页面注册按钮 """
        frame = wx.Frame(None, -1, "注册")
        frame.Show(True)

    def successfullyLogin(self):
        """ 成功登录 """
        self.Close()
        # 跳出另一个窗口
        MainPage(None, "查询")


class MainPage(wx.Frame):
    """ 登陆成功后的主页面 """

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500, 400))

        self.SetMaxSize((500, 400))
        self.SetMinSize((500, 400))
        self.panel = None
        self.text1 = None
        self.text2 = None
        self.text3 = None
        self.text4 = None
        self.text5 = None
        self.info_num = 0
        self.info_count = 0
        self.package_num = 0
        self.rest_time = 0
        self.updated = False
        self.timer = None
        self.init_ui()
        self.Show(True)

    def init_ui(self):
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour((255, 255, 255))
        self.panel.Refresh()

        # timer
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update, self.timer)
        self.timer.Start(100)

        # Font
        font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

        # 第一行文本
        message1 = "需要更新 " + str(self.info_num) + " 条信息"
        self.text1 = wx.StaticText(self.panel, label=message1, pos=(140, 85))
        self.text1.SetFont(font)

        # 第二行文本
        message2 = "更新第 " + str(self.info_count) + " 条信息"
        self.text2 = wx.StaticText(self.panel, label=message2, pos=(140, 115))
        self.text2.SetFont(font)

        # 第三行文本
        self.text3 = wx.StaticText(self.panel, label="项目信息", pos=(140, 145))
        self.text3.SetFont(font)

        # 第四行文本
        message4 = "分报个数：" + str(self.package_num)
        self.text4 = wx.StaticText(self.panel, label=message4, pos=(140, 175))
        self.text4.SetFont(font)

        # 第五行文本
        message5 = "休息 " + str(self.rest_time) + "s"
        self.text5 = wx.StaticText(self.panel, label=message5, pos=(140, 205))
        self.text5.SetFont(font)

    def update(self, event):
        # 调用函数，更新数据
        self.info_num = 100
        self.info_count += 1
        self.package_num = 1
        self.rest_time += 1

        # 更新文本
        message1 = "需要更新 " + str(self.info_num) + " 条信息"
        message2 = "更新第 " + str(self.info_count) + " 条信息"
        message4 = "分报个数：" + str(self.package_num)
        message5 = "休息 " + str(self.rest_time) + "s"
        self.text1.SetLabel(message1)
        self.text2.SetLabel(message2)
        self.text4.SetLabel(message4)
        self.text5.SetLabel(message5)

        if self.info_count == self.info_num:
            self.timer.Stop()

            # 调用函数判断最后一条是否更新完毕
            self.updated = True

        if self.updated:
            wx.MessageBox("成功！")


def main():
    app = wx.App(False)

    frame = LoginPage(None, "招标采购平台")

    # MainPage(None, "招标采购平台")

    app.MainLoop()


if __name__ == "__main__":
    main()
