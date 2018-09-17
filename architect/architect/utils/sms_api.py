# _Author_  "wangyy32"
# -*- coding: utf-8 -*-


from architect.utils.env import EnvConfig
import requests
import urllib2

class SmsHandler(object):
    def __init__(self):
        env_config = EnvConfig()
        self.logger = env_config.logger
        self.auth_url = env_config.auth_url
        self.app_key = env_config.appkey
        self.app_secret = env_config.appsecret
        self.appcode = env_config.appcode

    def verify_code(self, verify_code, mobile):
        http_response = None
        template_content = "【51架构师网】验证码为：%s,欢迎51架构师网！" % verify_code
        template_data = "Template=None&content=%s&mobile=%s" % (urllib2.quote(template_content), mobile)
        sms_url = self.auth_url.encode('utf-8') + '?' + template_data
        headers = {"content-type": "application/json", "Authorization": "APPCODE " + self.appcode}
        try:
            http_response = requests.post(url=sms_url, headers=headers, data={})
        except Exception as sms_error:
            self.logger.debug("Use sms gateway encounters error: %s" % sms_error)
        finally:
            if http_response.status_code == 200:
                self.logger.debug("短信发送成功，短信内容为: %s" % template_content)
            else:
                self.logger.debug("短信发送失败， 请调查失败原因......")
