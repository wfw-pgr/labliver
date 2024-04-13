##############################################################
時間測定
##############################################################

=========================================================
時間測定、 その一
=========================================================

time.time() 関数を使用する．::

  import time

  stime    = time.time()
  etime    = time.time()
  duration = etime - stime


=========================================================
時間測定、 その二
=========================================================

time.perf_counter() 関数を使用する．::

  import time

  stime    = time.perf_counter()
  etime    = time.perf_counter()
  duration = etime - stime



=========================================================
分、時間に変換
=========================================================

愚直に計算する．::

  import time

  stime    = time.perf_counter()
  etime    = time.perf_counter()
  duration = etime - stime

  hour     =   int( duration ) // 3600
  min      = ( int( duration ) - 3600*hour ) // 60
  sec      = ( int( duration ) - 3600*hour - 60*min )
  print( " elapssed time :: {0:02}:{1:02}:{2:02}".format( hour, min, sec ) )


=========================================================
もっとかんたん
=========================================================

かんたんな表記のver.::

  import time
  stime    = time.perf_counter()
  duration = time.perf_counter() - stime
  h,m,s    = int(duration)//3600, (int(duration)%3600)//60, int(duration)%60
  print( " elapssed time :: {0:02}:{1:02}:{2:02}".format( h,m,s ) )


=========================================================
Reference
=========================================================

* 時間計測 ( https://yumarublog.com/python/func-speed/ )
