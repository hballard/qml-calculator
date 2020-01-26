# -*- mode: python ; coding: utf-8 -*-
import os


block_cipher = None

added_files = [("view", "view")]

excluded_binaries = [
    "QtWebEngineCore",
    "QtXmlPatterns",
    "QtVirtualKeyboard",
    "QtLocation",
    "QtCharts",
    "QtDataVisualization",
    "QtMulitmedia",
    "QtBluetooth",
    "QtRemoteObjects"
]

a = Analysis(
    ["main.py"],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

a.binaries = [x for x in a.binaries if not x[0].startswith("Qt3D")]
a.binaries = TOC([x for x in a.binaries if x[0] not in excluded_binaries])

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="Heath's QML Calculator",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="Heath's QML Calculator",
)
app = BUNDLE(
    coll,
    name="Heath's QML Calculator.app",
    info_plist={"NSHighResolutionCapable": "True"},
    icon=os.path.join("images", "program_icon.icns"),
    bundle_identifier=None,
)

