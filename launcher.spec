# -*- mode: python ; coding: utf-8 -*-

import sys
from PyInstaller.utils.hooks import collect_data_files

source_folder = 'D:/EpohaHub/launcher-main'

a = Analysis(
    ['main.py'],
    pathex=[source_folder],
    binaries=[],
    datas=[
        (f'{source_folder}/favicon.ico', '.'),
        (f'{source_folder}/help.css', 'static'),
        (f'{source_folder}/help.html', 'static'),
        (f'{source_folder}/help.js', 'static'),
        (f'{source_folder}/index.css', 'static'),
        (f'{source_folder}/index.html', 'static'),
        (f'{source_folder}/index.js', 'static'),
        (f'{source_folder}/instances.css', 'static'),
        (f'{source_folder}/instances.html', 'static'),
        (f'{source_folder}/instances.js', 'static'),
        (f'{source_folder}/LICENSE', '.'),
        (f'{source_folder}/settings.css', 'static'),
        (f'{source_folder}/settings.html', 'static'),
        (f'{source_folder}/settings.js', 'static'),
        (f'{source_folder}/assets', 'assets'),
    ],
    hiddenimports=[
        'portablemc',
        'GPUtil',
        'humanize',
        'psutil',
        'wmi',
        'webview'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='MetaCube Launcher',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=True,
    cipher=None,
    icon=f'{source_folder}/favicon.ico',
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    cipher=None,
    clean=True,
    name='MetaCube Launcher'
)