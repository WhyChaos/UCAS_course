import os
import json

class Local:
    def __init__(self):
        self.file_name = 'UCAScouse.history'
        self.data = {}
        # 检查文件是否存在
        if not os.path.exists(self.file_name):
            # 如果文件不存在，创建一个新的JSON文件并写入一些示例数据
            with open(self.file_name, "w") as json_file:
                json.dump(self.data, json_file, indent=4)
        else:
            with open(self.file_name, "r") as json_file:
                self.data = json.load(json_file)
                
    def get_sepuser(self):
        try:
            return self.data['sepuser']
        except:
            return ''
        
    def get_JSESSIONID(self):
        try:
            return self.data['JSESSIONID']
        except:
            return ''
        
    def get_courseCode(self):
        try:
            return self.data['courseCode']
        except:
            return ''
    
    def get_courseName(self):
        try:
            return self.data['courseName']
        except:
            return ''
        
    def get_interval(self):
        try:
            return string(self.data['interval'])
        except:
            return ''
        
    def get_username(self):
        try:
            return self.data['username']
        except:
            return ''
        
    def get_wechat_path(self):
        try:
            return self.data['wechat_path']
        except:
            return ''
    
    def get_receiver_email(self):
        try:
            return self.data['receiver_email']
        except:
            return ''
    
        
    def save(self, dd):
        for key, value in dd.items():
            self.data[key] = value
        with open(self.file_name, "w") as json_file:
            json.dump(self.data, json_file, indent=4)
            
