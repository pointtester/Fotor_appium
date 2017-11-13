__author__ = 'py'
from common.public import mytest
from common.handle.sidebar.sidebarhandle1 import intosidebar
#from common.public.log import Log
#logger=Log()

class TestLogin(mytest.MyTest):

     #点击侧边栏展开
    def test_sidebar(self):
        expandsidebar = intosidebar(self.dr)
        expandsidebar.click_sidebar()



