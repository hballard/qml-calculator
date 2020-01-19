import os

from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl

current_dir = os.path.dirname(os.path.realpath(__file__))

os.environ["QT_QUICK_CONTROLS_CONF"] = os.path.join(
    current_dir, "view", "qtquickcontrols2.conf"
)
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"


app = QApplication([])
view = QQuickView()
import_path = os.path.join(current_dir, "view", "imports")
view.engine().addImportPath(import_path)
filename = os.path.join(current_dir, "view", "Main.qml")
url = QUrl.fromLocalFile(filename)

view.setSource(url)
view.show()
app.exec_()
