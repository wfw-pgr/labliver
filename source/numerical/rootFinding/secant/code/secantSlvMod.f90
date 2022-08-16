module secantSlvMod
contains

  
  ! ====================================================== !
  ! === analyticFunc                                   === !
  ! ====================================================== !
  function analyticFunc( xv )
    implicit none
    double precision, intent(in)  :: xv
    double precision              :: analyticFunc
    
    analyticFunc = sin( xv ) + cos( xv ) - 0.707d0
    return
  end function analyticFunc
  
  
  ! ====================================================== !
  ! === secantMethod                                   === !
  ! ====================================================== !
  subroutine secantMethod( x1, x2, iterMax, crit )
    implicit none
    integer         , intent(in)    :: iterMax
    double precision, intent(in)    :: crit
    double precision, intent(inout) :: x1, x2
    integer                         :: iter
    double precision                :: y1, y2, fpInv
    
    ! ------------------------------------------------------ !
    ! --- [1] Solve Main Iteration                       --- !
    ! ------------------------------------------------------ !
    y1 = analyticFunc( x1 )
    y2 = analyticFunc( x2 )
    do iter=1, iterMax
       fpInv = ( x2 - x1 ) / ( y2 - y1 )
       x1    = x2
       y1    = y2
       x2    = x2 - y2 * fpInv
       y2    = analyticFunc( x2 )
       if ( abs(y2).lt.crit ) exit
    enddo
    ! ------------------------------------------------------ !
    ! --- [2] return variables                           --- !
    ! ------------------------------------------------------ !
    x1 = x2
    x2 = y2
    
    return
  end subroutine secantMethod
  
end module secantSlvMod
