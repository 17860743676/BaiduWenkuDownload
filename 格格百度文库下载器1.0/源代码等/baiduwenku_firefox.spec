# -*- mode: python -*-

block_cipher = None


a = Analysis(['baiduwenku_firefox.py'],
             pathex=['D:\\Code\\GeGeWenkuDownload\\格格百度文库下载器1.0\\源代码等'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='baiduwenku_firefox',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='gege.ico')
