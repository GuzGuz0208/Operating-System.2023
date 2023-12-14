import cv2
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QFileDialog
from PyQt5.QtCore import Qt, QRect, QPropertyAnimation, QAbstractAnimation
from PyQt5.QtGui import QPixmap


class VideoPlayer(QWidget):
    def __init__(self, parent=None):
        super(VideoPlayer, self).__init__(parent)

        self.parent = parent

        self.initUI()

    def initUI(self):
        self.labelVideo = QLabel(self)
        self.labelVideo.setAlignment(Qt.AlignCenter)
        self.labelVideo.setGeometry(0, 0, 640, 480)

        self.buttonCargarVideo = QPushButton("Cargar video", self)
        self.buttonCargarVideo.setCursor(Qt.PointingHandCursor)
        self.buttonCargarVideo.setFixedSize(325, 30)
        self.buttonCargarVideo.move(10, 519)

        self.buttonEliminarVideo = QPushButton("Detener video", self)
        self.buttonEliminarVideo.setCursor(Qt.PointingHandCursor)
        self.buttonEliminarVideo.setFixedSize(255, 30)
        self.buttonEliminarVideo.move(345, 519)

        self.buttonCargarVideo.clicked.connect(self.cargarVideo)
        self.buttonEliminarVideo.clicked.connect(self.detenerVideo)

        self.videoCapture = None

    def bloquearBotones(self, bool):
        self.buttonCargarVideo.setEnabled(bool)
        self.buttonEliminarVideo.setEnabled(bool)

    def cargarVideo(self):
        nombreVideo, _ = QFileDialog.getOpenFileName(self, "Seleccionar video",
                                                      "", "Archivos de video (*.mp4 *.avi)")

        if nombreVideo:
            self.bloquearBotones(False)

            self.videoCapture = cv2.VideoCapture(nombreVideo)
            self.mostrarVideo()

    def detenerVideo(self):
        if self.videoCapture:
            self.videoCapture.release()
            self.labelVideo.clear()
            self.bloquearBotones(True)

    def mostrarVideo(self):
        ret, frame = self.videoCapture.read()
        if ret:
            height, width, channel = frame.shape
            bytesPerLine = 3 * width
            qImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
            self.labelVideo.setPixmap(QPixmap.fromImage(qImg))
            self.labelVideo.repaint()
            self.mostrarVideo()
        else:
            self.detenerVideo()

class VisorVideos(QMainWindow):
    def __init__(self, parent=None):
        super(VisorVideos, self).__init__(parent)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Visor de videos")
        self.setFixedSize(682, 573)

        self.videoPlayer = VideoPlayer(self)
        self.setCentralWidget(self.videoPlayer)

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    mainWindow = VisorVideos()
    mainWindow.show()
    sys.exit(app.exec_())
