# -*- mode: python -*-

block_cipher = None


a = Analysis(['SystemManagement.py'],
             pathex=['/home/tarcisio/Projects/Vectra-application'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.datas += [('assets/restart.png', 'assets/restart.png', 'DATA'), 
            ('assets/shutdown.png', 'assets/shutdown.png', 'DATA'),
            ('assets/terminal.png', 'assets/terminal.png', 'DATA')]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='SystemManagement',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
