program main
  use brentSolvMod
  implicit none
  double precision, parameter :: xMin    = 0.d0
  double precision, parameter :: xMax    = 4.d0
  integer         , parameter :: iterMax = 100
  double precision, parameter :: crit    = 1.d-12
  double precision            :: x1, x2
  
  ! ------------------------------------------------------ !
  ! --- [1] solve by bisection Method                  --- !
  ! ------------------------------------------------------ !
  x1 = 0.5d0
  x2 = 1.2d0
  call brentSolver( x1, x2, iterMax, crit )
  write(6,*) "[Main@brentSolver] x1, x2, res, sin(x)"
  write(6,*) x1, x2, analyticFunc( x1 )
  write(6,*) "[Main@brentSolver] Answer should be..."
  write(6,*) sin(x1), 0.707d0
  
  return
end program main
