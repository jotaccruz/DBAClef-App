# -*- mode: python -*-

block_cipher = None


a = Analysis(['moldmydb.py'],
             pathex=['C:\\CarlosCross-GitRepositories\\moldmydb'],
             binaries=[('./files/moldmydb.png', 'files')],
             datas=[('./scripts/StatusTree1_0.sql', 'scripts'), ('./scripts/StatusTree2_0.sql', 'scripts'), ('./scripts/StatusTree2_1.sql', 'scripts'), ('./scripts/StatusTree3_0.sql', 'scripts'), ('./scripts/StatusTree4_0.sql', 'scripts'), ('./scripts/serverNbTab1Tree1_0.sql', 'scripts'), ('./scripts/serverNbTab4Tree1_0.sql', 'scripts'), ('./scripts/serverNbTab4Tree1_1.sql', 'scripts'), ('./scripts/serverNbTab4Tree1_2.sql', 'scripts'), ('./scripts/serverNbTab4Tree1_3.sql', 'scripts'), ('./scripts/serverNbTab5Tree1_0.sql', 'scripts'), ('./scripts/serverNbTab5Tree2_0.sql', 'scripts'), ('./scripts/serverNbTab5Tree2_1.sql', 'scripts'), ('./scripts/serverNbTab5Tree3_0.sql', 'scripts'), ('./scripts/serverNbTab6Tree1_0.sql', 'scripts'), ('./scripts/serverNbTab6Tree1_1.sql', 'scripts'), ('./scripts/serverNbTab6Tree2_0.sql', 'scripts'), ('./scripts/serverNbTab6Tree3_0.sql', 'scripts'), ('./scripts/serverNbTab6Tree4_0.sql', 'scripts'), ('./scripts/serverNbTab6Tree5_0.sql', 'scripts'), ('./scripts/serverNbTab6Tree6_0.sql', 'scripts'), ('./scripts/serverNbTab6Tree6_1.sql', 'scripts'), ('./scripts/serverNbTab6Tree7_0.sql', 'scripts'), ('./scripts/serverNbTab6Tree7_1.sql', 'scripts'), ('./scripts/serverNbTab6Tree8_0.sql', 'scripts'), ('./scripts/serverNbTab7Tree1_0.sql', 'scripts'), ('./scripts/serverNbTab7Tree2_0.sql', 'scripts'), ('./scripts/serverNbTab7Tree3_0.sql', 'scripts'), ('./scripts/serverNbTab7Tree3_1.sql', 'scripts'), ('./scripts/serverNbTab8Tree1_0.sql', 'scripts'), ('./scripts/serverNbTab8Tree1_1.sql', 'scripts'), ('./scripts/serverNbTab9Tree1_0.sql', 'scripts'), ('./scripts/serverNbTab9Tree2_0.sql', 'scripts'), ('./scripts/serverNbTab9Tree3_0.sql', 'scripts'), ('./scripts/serverNbTab9Tree4_0.sql', 'scripts'), ('./scripts/serverNbTab9Tree4_1.sql', 'scripts'), ('./scripts/serverNbTab10Tree1_0.sql', 'scripts'), ('./scripts/serverNbTab11Tree1_0.sql', 'scripts'), ('./scripts/serverNbTab11Tree1_1.sql', 'scripts'), ('./scripts/serverNbTab12Tree1_0.sql', 'scripts'), ('./scripts/serverNbTab12Tree1_1.sql', 'scripts'), ('./scripts/serverNbTab12Tree2_0.sql', 'scripts'), ('./scripts/serverNbTab12Tree2_1.sql', 'scripts'), ('./scripts/serverNbTab12Tree2_2.sql', 'scripts'), ('./scripts/serverNbTab12Tree2_3.sql', 'scripts'), ('./scripts/serverNbTab13Tree1_0.sql', 'scripts'), ('./scripts/serverNbTab13Tree1_1.sql', 'scripts'), ('./scripts/serverNbTab13Tree1_2.sql', 'scripts'), ('./scripts/serverNbTab13Tree1_3.sql', 'scripts'), ('./scripts/serverNbTab13Tree1_4.sql', 'scripts'), ('./scripts/ServiceButton_0.sql', 'scripts'), ('./scripts/ServiceButton_1.sql', 'scripts'), ('./scripts/spButton_0.sql', 'scripts'), ('./scripts/spButton_1.sql', 'scripts'), ('./scripts/StandardLoginsButton_0.sql', 'scripts'), ('./scripts/saButton_0.sql', 'scripts'), ('./scripts/AlertsButton_0.sql', 'scripts'), ('./scripts/mailButton_0.sql', 'scripts'), ('./scripts/genchkButton_0.sql', 'scripts'), ('./scripts/ifiButton_0.sql', 'scripts'), ('./scripts/ifiButton_1.sql', 'scripts'), ('./scripts/ifiButton_2.sql', 'scripts'), ('./scripts/ifiButton_3.sql', 'scripts'), ('./scripts/ifiButton_4.sql', 'scripts'), ('./scripts/ifiButton_5.sql', 'scripts')],
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
          name='moldmydb',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='files\\moldmydb.ico')
