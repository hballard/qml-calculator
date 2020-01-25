import os
import sys

import PySide2.QtQml
from PySide2.QtGui import QGuiApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl

from controller import CalculatorController

current_dir = os.path.dirname(os.path.realpath(__file__))

os.environ["QT_QUICK_CONTROLS_CONF"] = os.path.join(
    current_dir, "view", "qtquickcontrols2.conf"
)
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

app = QGuiApplication(sys.argv)
view = QQuickView()
view.setResizeMode(QQuickView.SizeRootObjectToView)

import_path = os.path.join(current_dir, "view", "imports")
view.engine().addImportPath(import_path)

controller = CalculatorController()

view.rootContext().setContextProperty("controller", controller)

filename = os.path.join(current_dir, "view", "Main.qml")
url = QUrl.fromLocalFile(filename)
view.setSource(url)

if view.status() == QQuickView.Error:
    sys.exit(-1)
view.show()
res = app.exec_()

del view

sys.exit(res)
