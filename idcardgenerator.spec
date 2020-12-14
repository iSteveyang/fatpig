# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['idcardgenerator.py'],
             pathex=['/Users/isteveyang/Downloads/fatPig'],
             binaries=[],
             datas=[('./usedres', './usedres')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='idcardgenerator',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='usedres/ico.icns')
app = BUNDLE(exe,
             name='idcardgenerator.app',
             icon='usedres/ico.icns',
             bundle_identifier=None)
