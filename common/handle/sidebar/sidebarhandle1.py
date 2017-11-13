from common.pages.sidebar.sidebarpage1 import sidebarpage1

class intosidebar(sidebarpage1):

    #点击侧边栏
    def click_sidebar(self):
        return self.p.click(self.siedbar)

