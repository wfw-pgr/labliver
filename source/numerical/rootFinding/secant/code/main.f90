program main
  use secantSlvMod
  implicit none
  double precision, parameter :: xMin    = 0.d0
  double precision, parameter :: xMax    = 4.d0
  integer         , parameter :: nData   = 101
  integer         , parameter :: lun     = 50
  integer         , parameter :: iterMax = 100
  double precision, parameter :: crit    = 1.d-12
  integer                     :: i
  double precision            :: xi(nData), yi(nData)
  double precision            :: x1, x2
  
  ! ------------------------------------------------------ !
  ! --- [1] solve by secant Method                     --- !
  ! ------------------------------------------------------ !
  x1 = 0.d0
  x2 = 1.d0
  call secantMethod( x1, x2, iterMax, crit )
  write(6,*) "answer   :: x1 == ", x1
  write(6,*) "residual :: x2 == ", x2
  write(6,*) "y1 - theory    == ", analyticFunc( x1 )
  write(6,*) "theory L.H.S.  == ", sin(x1) + cos(x1) 
  write(6,*) "theory R.H.S.  == ", 0.707d0
  
  return
end program main
