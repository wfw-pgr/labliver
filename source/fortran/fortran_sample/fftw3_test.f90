
program main



  implicit none

  integer, parameter :: N=256
  double precision, parameter :: pi   = 4.d0 * atan( 1.d0 )
  double precision, parameter :: xmax = 2.d0 * pi, xmin = 0.d0
  double precision, parameter :: amp  = 1.d0
  double precision, parameter :: k    = 2.d0

  integer(8) :: plan

  integer :: i, j
  double precision :: dx
  double precision :: x(N)
  complex(kind(0d0)) :: y(N), fft(N)
  double precision :: power(N), theta(N)

  ! data preparation

  include 'fftw3.f'

  do i=1, N
     dx = ( xmax - xmin ) / dble(N)
     x(i) = dx * dble( i - 1 )
     y(i) = amp * sin( k * x(i) )
  enddo

  open( 50, file='x.dat', form='formatted' )
  do i=1, N
     write(50,*) x(i), y(i)
  enddo
  close(50)

  ! FFT

  call dfftw_plan_dft_1d( plan, N, y, fft, FFTW_FORWARD, FFTW_ESTIMATE )
  call dfftw_execute_dft( plan, y, fft )
  call dfftw_destroy_plan( plan )

  power = abs( fft ) / dble(N)
  theta = atan2( aimag(fft), real(fft) )

  ! write

  open( 50, file='fft.dat', form='formatted' )
  do i=1, N
     write(50,*) i, power(i), theta(i)
  enddo
  close(50)


end program main
