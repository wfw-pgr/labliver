program main
  use RKGMethodMod, only : RungeKutta4th
  implicit none
  integer         , parameter :: cLen  = 300
  integer         , parameter :: nData = 21
  double precision, parameter :: xMin  = 0.d0
  double precision, parameter :: xMax  = 2.d0
  integer                     :: i
  double precision            :: xn(nData), yn(nData)
  character(cLen)             :: datFile='dat/out.dat'

  ! ------------------------------------------------------ !
  ! --- [1] preparation :: initial settings            --- !
  ! ------------------------------------------------------ !
  do i=1, nData
     xn(i) = ( xMax - xMin ) / dble( nData-1 ) * dble(i-1) + xMin
     yn(i) = 0.d0
  enddo
  yn(1) = 1.d0
  
  
  ! ------------------------------------------------------ !
  ! --- [2] Runge Kutta ( 4th-order )                  --- !
  ! ------------------------------------------------------ !
  call RungeKutta4th( xn, yn, nData )

  ! ------------------------------------------------------ !
  ! --- [3] output results                             --- !
  ! ------------------------------------------------------ !
  do i=1, nData
     write(6,*) i, xn(i), yn(i)
  enddo
  open( 50, file=trim(datFile), status='replace', form='formatted' )
  do i=1, nData
     write(50,*) i, xn(i), yn(i)
  enddo
  close(50)
  
  return
end program main
