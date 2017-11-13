from common.pages.sidebar.sidebarpage2 import sidebarpage2

class sidebarpage3 (sidebarpage2):

    #注册页面账号输入框
    emailaddress = "xpath->//android.widget.RelativeLayout[@resource-id=\"com.everimaging.photoeffectstudio:id/account_login_email\"]/android.widget.EditText[1]"

    #注册页面密码输入框
    password = "xpath->//android.widget.RelativeLayout[@resource-id=\"com.everimaging.photoeffectstudio:id/account_login_password\"]/android.widget.EditText[1]"

    #确定按钮
    signup = "id->com.everimaging.photoeffectstudio:id/btnLoginSignUp"

    #切换到登录
    login = "xpath->//android.widget.TextView[@text=\"Log in\"]"

    #FB登录
    Login_with_facebook = "id->com.everimaging.photoeffectstudio:id/accounts_sign_up_with_facebook"

    #Google登录
    Login_with_google = "id->com.everimaging.photoeffectstudio:id/accounts_sign_up_with_google"

    #服务条款勾选按钮
    CheckTheTermofService = "id->com.everimaging.photoeffectstudio:id/accounts_agree_policy"

    #查看服务条款
    TermofService = "id->com.everimaging.photoeffectstudio:id/login_terms_of_service_link"
