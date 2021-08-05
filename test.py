# -*- coding: utf-8 -*-
import re
import subprocess
import os
import sys  # 导入sys模块


class ApkInfo:
    def __init__(self, apk_path):
        self.apkPath = apk_path
        self.aapt_path = self.get_aapt()

    @staticmethod
    def get_aapt():
        if "ANDROID_HOME" in os.environ:
            root_dir = os.path.join(os.environ["ANDROID_HOME"], "build-tools")
            for path, subdir, files in os.walk(root_dir):
                if "aapt.exe" in files:
                    return os.path.join(path, "aapt.exe")
        else:
            return "ANDROID_HOME not exist"

    def get_apk_base_info(self):
        p = subprocess.Popen(self.aapt_path + " dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        match = re.compile("package: name='(\S+)'").match(output.decode())
        if not match:
            raise Exception("can't get packageinfo")
        package_name = match.group(1)
        return package_name

    def get_apk_activity(self):
        p = subprocess.Popen(self.aapt_path + " dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        match = re.compile("launchable-activity: name='(\S+)'").search(output.decode())
        if match is not None:
            return match.group(1)

    def get_apk_sdkVersion(self):
        p = subprocess.Popen(self.aapt_path + " dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        match = re.compile("sdkVersion:'(\S+)'").search(output.decode())
        return match.group(1)

    def get_apk_targetSdkVersion(self):
        p = subprocess.Popen(self.aapt_path + " dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        match = re.compile("targetSdkVersion:'(\S+)'").search(output.decode())
        return match.group(1)


if __name__ == '__main__':
    apk_info = ApkInfo(sys.argv[1])  # 直接将cmd中给的参数引用至此
    print("Activity:%s" % apk_info.get_apk_activity())
    print("apkName:%s" % apk_info.get_apk_base_info())
    print("sdkVersion:%s" % apk_info.get_apk_sdkVersion())
    print("targetSdkVersion:%s" % apk_info.get_apk_targetSdkVersion())
