from PyQt5.QtMultimedia import QMediaRecorder,QAudioInput,QAudioProbe,QAudioBuffer,QAudioFormat,QMultimedia,QAudioEncoderSettings
from PyQt5.QtCore import QByteArray,QDataStream,QDir,QStandardPaths,QUrl,pyqtSignal,QFile,QCoreApplication,QIODevice,QTimer
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow
from Online_ASR import ASR
import threading

class Recorder(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Recorder, self).__init__()
        self.setupUi(self)
        self.output = QFile()
        self.audio = QAudioInput()

        self.th1 = threading.Thread(target=self.ASR)

        self.Pause_Button.clicked.connect(self.toggle_pause)
        self.Record_Button.clicked.connect(self.toggle_record)



    def toggle_record(self):
        if self.Record_Button.text()=="开始录音":
            self.statusbar.showMessage("开始录音")
            self.th1._stop()
            self.audio.start(self.output)
            self.Record_Button.setText("停止")
            self.Pause_Button.setText("暂停")
            self.Pause_Button.setEnabled(True)
        else:
            self.audio.stop()
            self.output.close()

            self.audio = QAudioInput()
            self.output = QFile()
            self.setup()

            self.Pause_Button.setText("暂停")
            self.Record_Button.setText("开始录音")
            self.statusbar.showMessage("正在使用百度智能云识别，请稍等")
            self.th1.start()

    def toggle_pause(self):
        if self.Pause_Button.text()=="暂停":
            self.Pause_Button.setText("继续")
            self.audio.suspend()

        else:
            self.Pause_Button.setText("暂停")
            self.audio.resume()

    def ASR(self):
        try:
            text = ASR().Baidu_ASR("record.pcm")
            print(text)
            if text['err_msg'] == 'success.':
                self.Text_plainTextEdit.setPlainText(text['result'][0])
                self.statusbar.showMessage("识别成功")
            else:
                self.statusbar.showMessage("识别失败,请再说一遍")
        except:
            self.statusbar.showMessage("网络故障，请检查网络设置以及百度智能云账号")








    def setup(self):
        self.output.setFileName("record.pcm")
        self.output.open(QIODevice.WriteOnly | QIODevice.Truncate)
        settings = QAudioFormat()
        settings.setCodec("audio/pcm");
        settings.setSampleRate(16000);
        settings.setSampleSize(16);
        settings.setChannelCount(1);
        settings.setByteOrder(QAudioFormat.LittleEndian);
        settings.setSampleType(QAudioFormat.SignedInt);
        self.audio = QAudioInput(settings)






if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    x = Recorder()
    x.show()

    sys.exit(app.exec_())

