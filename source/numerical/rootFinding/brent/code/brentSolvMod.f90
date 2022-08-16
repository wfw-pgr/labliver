module brentSolvMod
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
  ! === brent Solver for Root Finding                  === !
  ! ====================================================== !
  subroutine brentSolver( x1, x2, iterMax, crit )
    implicit none
    integer         , intent(in)    :: iterMax
    double precision, intent(in)    :: crit
    double precision, intent(inout) :: x1, x2
    integer                         :: iter
    double precision                :: xa, xb, xc, xd, xe, xm
    double precision                :: fa, fb, fc
    double precision                :: sval, pval, qval, rval
    double precision                :: epsilon, tolerance, judge1, judge2

    ! ------------------------------------------------------ !
    ! --- [1] Preparation before Main Loop               --- !
    ! ------------------------------------------------------ !
    epsilon = crit
    xa      = x1
    xb      = x2
    xc      = xb
    xe      = 0.d0
    fa      = analyticFunc( xa )
    fb      = analyticFunc( xb )
    fc      = fb
    if ( fa*fb.gt.0.d0 ) then
       write(6,*) '[brentSolver] ERROR!! x1 and x2 must be bracketed... '
       write(6,*) '[brentSolver]   i.e. ( f(x1)<0<f(x2) ) or ( f(x2)<0<f(x1) ) '
       stop
    endif
    ! ------------------------------------------------------ !
    ! --- [2] Main Loop                                  --- !
    ! ------------------------------------------------------ !
    do iter=1, iterMax
       if ( fb*fc.gt.0.d0 ) then
          xc = xa
          fc = fa
          xd = xb-xa
          xe = xd
       endif
       if ( abs(fc).lt.abs(fb) ) then
          xa = xb
          xb = xc
          xc = xa
          fa = fb
          fb = fc
          fc = fa
       endif
       ! -- convergence check   -- !
       tolerance = 2.d0*epsilon*abs( xb ) + 0.5d0*crit
       xm        = 0.5d0 * ( xc-xb )
       if ( ( abs(xm).le.tolerance ).or.( fb.eq.0.d0 ) ) exit
       ! -- solution candidates -- !
       if ( ( abs(xe).ge.tolerance ).and.( abs(fa).gt.abs(fb) ) ) then
          ! -- Attempts inverse uadratic interpolation -- !
          sval = fb / fa
          if ( xa.eq.xc ) then
             pval = 2.d0 * xm * sval
             qval = 1.d0 - sval
          else
             qval = fa / fc
             rval = fb / fc
             pval = sval * ( 2.d0*xm*qval*( qval-rval ) - ( xb-xa )*( rval-1.d0 ) )
             qval = ( qval-1.d0 )*( rval-1.d0 )*( sval-1.d0 )
          endif
          ! -- check wheter in bounds -- !
          if ( pval.gt.0.d0 ) qval = -qval
          pval   = abs(pval)
          judge1 = 2.d0*pval
          judge2 = min( 3.d0*xm*qval-abs( tolerance*qval ), abs( xe*qval ) )
          if ( judge1.lt.judge2 ) then
             ! -- Accept interpolation -- !
             xe = xd
             xd = pval / qval
          else
             ! -- Decline, use bisection -- !
             xd = xm
             xe = xd
          endif
       else
          ! -- Bounds decreasing too slowly, use bisection method -- !
          xd = xm
          xe = xd
       endif
       ! -- move last best guess to a -- !
       xa = xb
       fa = fb
       if ( abs(xd).gt.tolerance ) then
          xb = xb + xd
       else
          xb = xb + sign( tolerance, xm )
       endif
       fb = analyticFunc( xb )
    enddo
    ! ------------------------------------------------------ !
    ! --- [3] return x1 and x2                           --- !
    ! ------------------------------------------------------ !
    x1 = xb
    x2 = fb
    
    return
  end subroutine brentSolver

end module brentSolvMod
