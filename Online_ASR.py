from aip import AipSpeech


class ASR:
    def Baidu_ASR(self,file_path):
        APP_ID = '19501722'
        API_KEY = '9tqqWCAdr9GrSGNvwph8CHyq'
        SECRET_KEY = 'eEwRGkEKZzFxYIuQRleCgcRj9D0P8bpc'

        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

        def get_file_content(a):
            with open(a, 'rb') as fp:
                return fp.read()

        result = client.asr(get_file_content(file_path), 'pcm', 16000, {
            'dev_pid': 1537,  # 默认1537（普通话 输入法模型），dev_pid参数见本节开头的表格
        })

        return result

