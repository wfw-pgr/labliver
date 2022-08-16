module RKGMethodMod
contains

  
  ! ====================================================== !
  ! === Runge-Kutta ( 4th-order )                      === !
  ! ====================================================== !
  subroutine RungeKutta4th( xn, yn, nData )
    implicit none
    integer         , intent(in)    :: nData
    double precision, intent(inout) :: xn(nData), yn(nData)
    integer                         :: i
    double precision                :: k1, k2, k3, k4, dx, hdx
    double precision, parameter     :: onesixth = 1.d0 / 6.d0

    do i=1, nData-1
       dx      = xn(i+1) - xn(i)
       hdx     = 0.5d0*dx
       k1      = rhs( xn(i)    , yn(i)        )
       k2      = rhs( xn(i)+hdx, yn(i)+hdx*k1 )
       k3      = rhs( xn(i)+hdx, yn(i)+hdx*k2 )
       k4      = rhs( xn(i)+ dx, yn(i)+ dx*k3 )
       yn(i+1) = yn(i) + onesixth*dx*( k1 + 2.d0*k2 + 2.d0*k3 + k4 )
    enddo
       
    return
  end subroutine RungeKutta4th


  ! ====================================================== !
  ! === evaluate R.H.S.                                === !
  ! ====================================================== !
  function rhs( x, y )
    implicit none
    double precision, intent(in) :: x, y
    double precision             :: rhs
    rhs = y
    return
  end function rhs

  
end module RKGMethodMod
