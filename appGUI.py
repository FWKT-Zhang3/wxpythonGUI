import wx


class MainFrame(wx.Frame):
    """ 主Frame，登录页面 """

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500, 300))

        self.SetMaxSize((500, 300))
        self.SetMinSize((500, 300))
        self.panel = None
        self.text_user = None
        self.text_pwd = None
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

        # 设置按钮
        bt_confirm = wx.Button(self.panel, label='确定', pos=(120, 200), style=wx.NO_BORDER)
        bt_confirm.Bind(wx.EVT_BUTTON, self.onclick_submit)
        bt_confirm.SetBackgroundColour("Blue")
        bt_confirm.SetForegroundColour("White")
        bt_cancel = wx.Button(self.panel, label='取消', pos=(213, 200), style=wx.NO_BORDER)
        bt_cancel.Bind(wx.EVT_BUTTON, self.onclick_cancel)
        bt_registered = wx.Button(self.panel, label='注册', pos=(305, 200), style=wx.NO_BORDER)
        bt_registered.Bind(wx.EVT_BUTTON, self.onclick_registered)

    def onclick_submit(self, event):
        """ 点击登录页面确认按钮 """
        username = self.text_user.GetValue()
        password = self.text_pwd.GetValue()

        if username == "" or password == "":
            message = "用户名或密码不能为空"
            # 此处需要链接数据库，判断用户名密码是否有匹配，是否正确
        else:
            message = "登陆成功！"

        wx.MessageBox(message)
        if message == "登陆成功！":
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
        UserInterface(None, "招标采购平台")


class UserInterface(wx.Frame):
    """ 用户界面，主界面 """

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(900, 700))
        self.panel = None
        self.text_website = None
        self.text_platform = None
        self.init_ui()
        self.SetMinSize((650, 400))
        self.Show(True)

    def init_ui(self):
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour((255, 255, 255))
        self.panel.Refresh()
        mystyle = wx.EXPAND | wx.ALL

        # 第一行：网站
        box1 = wx.BoxSizer()
        label_website = wx.StaticText(self.panel, label="网站")
        label_website.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT,
                                      wx.FONTSTYLE_NORMAL, wx.NORMAL))
        self.text_website = wx.TextCtrl(self.panel, size=(300, 25), style=wx.TE_LEFT)
        box1.Add(label_website, 0, mystyle, border=10)
        box1.Add(self.text_website, 0, mystyle, border=10)

        # 第二行：平台
        box2 = wx.BoxSizer()
        label_platform = wx.StaticText(self.panel, label="平台")
        label_platform.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT,
                                       wx.FONTSTYLE_NORMAL, wx.NORMAL))
        self.text_platform = wx.TextCtrl(self.panel, size=(300, 25), style=wx.TE_LEFT)
        box2.Add(label_platform, 0, mystyle, border=10)
        box2.Add(self.text_platform, 0, mystyle, border=10)

        # 第三行：按钮
        box3 = wx.BoxSizer()
        bt_cancel = wx.Button(self.panel, label='取消', style=wx.NO_BORDER)
        bt_cancel.Bind(wx.EVT_BUTTON, self.onclick_cancel)
        bt_confirm = wx.Button(self.panel, label='确定', style=wx.NO_BORDER)
        bt_confirm.Bind(wx.EVT_BUTTON, self.onclick_submit)
        bt_confirm.SetBackgroundColour("Blue")
        bt_confirm.SetForegroundColour("White")
        box3.Add(bt_confirm, 1, mystyle, border=10)
        box3.Add(bt_cancel, 1, mystyle, border=10)

        # input Sizer
        input_sizer = wx.BoxSizer(wx.VERTICAL)
        input_sizer.Add(box1, 0, mystyle, border=10)
        input_sizer.Add(box2, 0, mystyle, border=10)
        input_sizer.Add(box3, 0, mystyle, border=10)

        # main Sizer
        inner_box = wx.BoxSizer()
        inner_box.AddSpacer(100)
        inner_box.Add(input_sizer, 0, wx.CENTER)
        inner_box.AddSpacer(100)

        hbox = wx.BoxSizer()
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        hbox.Add(inner_box, 0, wx.ALIGN_CENTER)
        main_sizer.Add(hbox, 1, wx.ALIGN_CENTER)

        self.panel.SetSizer(main_sizer)

    def onclick_cancel(self, event):
        self.text_website.SetValue("")
        self.text_platform.SetValue("")

    def onclick_submit(self, event):
        website = self.text_website.GetValue()
        platform = self.text_platform.GetValue()

        flag = True

        if website == "":
            message = "请填写网站！"
            flag = False
        elif platform == "":
            message = "请填写平台！"
            flag = False
        else:
            message = "提交成功"

        wx.MessageBox(message)

        if flag:
            self.Close()
            QueryInfo(None, "信息检索")


class QueryInfo(wx.Frame):
    """ 用户界面，主界面 """

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(900, 700))
        self.panel = None
        self.text_time = None
        self.text_frequency = None
        self.text_content = None
        self.init_ui()
        self.SetMinSize((650, 400))
        self.Show(True)

    def init_ui(self):
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour((255, 255, 255))
        self.panel.Refresh()
        mystyle = wx.EXPAND | wx.ALL

        # 第一行：时间
        box1 = wx.BoxSizer()
        label_time = wx.StaticText(self.panel, label="时间")
        label_time.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT,
                                   wx.FONTSTYLE_NORMAL, wx.NORMAL))
        self.text_time = wx.TextCtrl(self.panel, size=(300, 25), style=wx.TE_LEFT)
        box1.Add(label_time, 0, mystyle, border=10)
        box1.Add(self.text_time, 0, mystyle, border=10)

        # 第二行：频率
        box2 = wx.BoxSizer()
        label_frequency = wx.StaticText(self.panel, label="频率")
        label_frequency.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT,
                                        wx.FONTSTYLE_NORMAL, wx.NORMAL))
        self.text_frequency = wx.TextCtrl(self.panel, size=(300, 25), style=wx.TE_LEFT)
        box2.Add(label_frequency, 0, mystyle, border=10)
        box2.Add(self.text_frequency, 0, mystyle, border=10)

        # 第三行：检索内容
        box3 = wx.BoxSizer()
        label_content = wx.StaticText(self.panel, label="检索内容")
        label_content.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT,
                                      wx.FONTSTYLE_NORMAL, wx.NORMAL))
        self.text_content = wx.TextCtrl(self.panel, size=(262, 25), style=wx.TE_LEFT)
        box3.Add(label_content, 0, mystyle, border=10)
        box3.Add(self.text_content, 0, mystyle, border=10)

        # 第四行：按钮
        box4 = wx.BoxSizer()
        bt_cancel = wx.Button(self.panel, label='取消', style=wx.NO_BORDER)
        bt_cancel.Bind(wx.EVT_BUTTON, self.onclick_cancel)
        bt_confirm = wx.Button(self.panel, label='确定', style=wx.NO_BORDER)
        bt_confirm.Bind(wx.EVT_BUTTON, self.onclick_submit)
        bt_confirm.SetBackgroundColour("Blue")
        bt_confirm.SetForegroundColour("White")
        box4.Add(bt_confirm, 1, mystyle, border=10)
        box4.Add(bt_cancel, 1, mystyle, border=10)

        # input Sizer
        input_sizer = wx.BoxSizer(wx.VERTICAL)
        input_sizer.Add(box1, 0, mystyle, border=10)
        input_sizer.Add(box2, 0, mystyle, border=10)
        input_sizer.Add(box3, 0, mystyle, border=10)
        input_sizer.Add(box4, 0, mystyle, border=10)

        # inner Sizer
        inner_box = wx.BoxSizer()
        inner_box.AddSpacer(100)
        inner_box.Add(input_sizer, 0, wx.CENTER)
        inner_box.AddSpacer(100)

        hbox = wx.BoxSizer()
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        hbox.Add(inner_box, 0, wx.ALIGN_CENTER)
        main_sizer.Add(hbox, 1, wx.ALIGN_CENTER)

        self.panel.SetSizer(main_sizer)

    def onclick_cancel(self, event):
        self.text_time.SetValue("")
        self.text_frequency.SetValue("")
        self.text_content.SetValue("")

    def onclick_submit(self, event):
        time = self.text_time.GetValue()
        frequency = self.text_frequency.GetValue()
        content = self.text_content.GetValue()

        flag = True

        if time == "":
            message = "请填写时间！"
            flag = False
        elif frequency == "":
            message = "请填写频率！"
            flag = False
        elif content == "":
            message = "请填写内容！"
            flag = False
        else:
            message = "提交成功"

        wx.MessageBox(message)

        if flag:
            self.Close()


def main():
    app = wx.App(False)

    frame = MainFrame(None, "招标采购平台")

    # QueryInfo(None, "信息检索")

    app.MainLoop()


if __name__ == "__main__":
    main()
