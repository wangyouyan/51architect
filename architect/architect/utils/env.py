# _Author_  "wangyy32"
# -*- coding: utf-8 -*-

import lark_common.utils as lark_utils


class EnvConfig(lark_utils.Singleton):
    def __init__(self):
        __app_name = '51architect'

        config = lark_utils.Config(__app_name + ".ini")

        # Common Section
        self.logger_level = config.get("common", "logger_level")
        self.logger = lark_utils.Logger(name=__app_name, level=self.logger_level).get_logger()

        # MySQL Database Section
        self.db_user = config.get("database", "db_user")
        self.db_password = config.get("database", "db_password")
        self.db_port = config.get("database", "db_port")
        self.db_name = config.get("database", "db_name")

        # SMS interface for nofication
        self.auth_url = config.get("sms_gateway", "auth_url")
        self.appkey = config.get("sms_gateway", "appkey")
        self.appsecret = config.get("sms_gateway", "appsecret")
        self.appcode = config.get("sms_gateway", "appcode")
