module bisectionMod
contains

  
  ! ====================================================== !
  ! === analyticFunc                                   === !
  ! ====================================================== !
  function analyticFunc( xv )
    implicit none
    double precision, intent(in)  :: xv
    double precision              :: analyticFunc
    
    analyticFunc = sin( xv ) - 0.707d0
    return
  end function analyticFunc
  
  
  ! ====================================================== !
  ! === bisectionMethod                                === !
  ! ====================================================== !
  subroutine bisectionMethod( x1, x2, iterMax, crit )
    implicit none
    integer         , intent(in)    :: iterMax
    double precision, intent(in)    :: crit
    double precision, intent(inout) :: x1, x2
    integer                         :: iter
    double precision                :: xmid, ymid
    double precision                :: sign1, sign2, signm

    ! ------------------------------------------------------ !
    ! --- [1] sign1 / sign2                              --- !
    ! ------------------------------------------------------ !
    sign1 = sign( 1.d0, analyticFunc( x1 ) )
    sign2 = sign( 1.d0, analyticFunc( x2 ) )
    if ( sign1.eq.sign2 ) then
       write(6,*) '[bisectionMethod]  x1 & x2 :: 2 variables have same sign.'
       stop
    endif
    ! ------------------------------------------------------ !
    ! --- [2] Solve Main Iteration                       --- !
    ! ------------------------------------------------------ !
    do iter=1, iterMax
       xmid  = 0.5d0 * ( x1 + x2 )
       ymid  = analyticFunc( xmid )
       signm = sign( 1.d0, ymid  )
       if      ( signm.eq.sign1 ) then
          x1    = xmid
       else if ( signm.eq.sign2 ) then
          x2    = xmid
       endif
       if ( abs(ymid).lt.crit ) exit
    enddo
    ! ------------------------------------------------------ !
    ! --- [3] return variables                           --- !
    ! ------------------------------------------------------ !
    x1 = xmid
    x2 = ymid
    
    return
  end subroutine bisectionMethod

  
end module bisectionMod
