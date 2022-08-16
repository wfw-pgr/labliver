program main
  use bisectionMod
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
  ! --- [1] solve by bisection Method                  --- !
  ! ------------------------------------------------------ !
  x1 = 0.d0
  x2 = 1.d0
  call bisectionMethod( x1, x2, iterMax, crit )
  write(6,*) x1, x2, analyticFunc( x1 ), sin(x1)
  
  return
end program main
