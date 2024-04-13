##############################################################
WSLにおけるsshサーバの設定
##############################################################

=========================================================
WSLがsshを許容する
=========================================================

* WSL1,2ともに、WSLに対してssh接続できるようになっている．
* 1と2でネットワーク構成が少し違うため、やり方が異なる．
* 1は、WSLのipアドレスがWindowsと共通、2は、WSLのipアドレスは仮想のアドレスが新規に割り当てられている．
* 2は、ポートフォワーディングが追加で必要になる．
  
=========================================================
導入
=========================================================

---------------------------------------------------------
sshd のインストール
---------------------------------------------------------

* デフォルトで入っているはず．


---------------------------------------------------------
/etc/ssh/sshd_configの設定
---------------------------------------------------------

以下をコメント外したり、yesにしたりして、有効化する．

* Port 22
* AddressFamily any
* PubkeyAuthentification yes
* PasswordAuthentification yes

変更後、再起動する． ::

  $ sudo service ssh restart


---------------------------------------------------------
ファイアウォールのポート開放
---------------------------------------------------------

* Powershellにて、以下を実効::
   
   $ New-NetFireWallRule -DisplayName 'WSL 2 Firewall Unlock' -Direction Outbound -LocalPort 22 -Action Allow -Protocol TCP
   $ New-NetFireWallRule -DisplayName 'WSL 2 Firewall Unlock' -Direction Inbound -LocalPort 22 -Action Allow -Protocol TCP

* 確認 ::
    
   $ Get-NetFirewallRule -DisplayName 'WSL 2 Firewall Unlock' | Get-NetFirewallPortFilter | Format-Table

---------------------------------------------------------
ポートフォワーディング（WSL2）
---------------------------------------------------------

* command / PowerShell にて ( 192.168.100.200はWSLのipアドレス=ifconfigで調べる ) ::

  $ netsh.exe interface portproxy add v4tov4 listenport=22 connectaddress=192.168.100.200
  $ sc.exe config iphlpsvc start=auto
  $ sc.exe start  iphlpsvc

  
* 確認コマンド ::
  
  $ netsh.exe interface portproxy show v4tov4



  
=========================================================
References
=========================================================

* https://qiita.com/yabeenico/items/15532c703974dc40a7f5
* https://mulberrytassel.com/wsl-ssh1/
