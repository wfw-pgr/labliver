! ====================================================== !
! === gauss Elimination :: partial pivoting ver.     === !
! ====================================================== !
module gaussElimMod
contains

  ! ========================================================== !
  ! === Gauss Elimination Solver                           === !
  ! ========================================================== !
  subroutine gaussElimin( Amat, xvec, bvec, nSize )
    implicit none
    integer         , intent(in)  :: nSize
    double precision, intent(in)  :: Amat(nSize,nSize)
    double precision, intent(in)  :: bvec(nSize)
    double precision, intent(out) :: xvec(nSize)
    integer                       :: i, j, k, ipivot
    double precision              :: Dinv, buff, vpivot
    double precision, parameter   :: eps = 1.d-10
    double precision, allocatable :: Umat(:,:), vvec(:,:)

    ! ----------------------------------------- !
    ! --- [1] Preparation                   --- !
    ! ----------------------------------------- !
    !  -- [1-1] allocate Umat               --  !
    allocate( Umat(nSize,nSize) )
    !  -- [1-2] Copy AMat & bvec            --  !
    Umat(:,:) = Amat(:,:)
    xvec(:)   = bvec(:)
    
    ! ----------------------------------------- !
    ! --- [2] Forward Ellimination          --- !
    ! ----------------------------------------- !
    do k=1, nSize

       !  -- [2-1] Pivoting                 --  !
       vpivot = abs( Umat(k,k) )
       ipivot = k
       do j=k+1, nSize
          if ( abs( Umat(j,k) ).gt.vpivot ) then
             vpivot = abs( Umat(j,k) )
             ipivot = j
          endif
       end do
       if ( ipivot.ne.k ) then
          do j=k, nSize
             buff           = Umat(ipivot,j)
             Umat(ipivot,j) = Umat(k     ,j)
             Umat(k     ,j) = buff
          enddo
          buff         = xvec(ipivot)
          xvec(ipivot) = xvec(k)
          xvec(k)      = buff
       end if
       if ( abs( Umat(k,k) ).lt.eps ) then
          write(6,*) '[gaussElimin] Amat :: Singular Matrix :: No Solution End :: @ k= ', k
          stop
       endif
       !  -- [2-2] Diagonal Component       --  !
       Dinv      = 1.d0 / Umat(k,k)
       Umat(k,k) = 1.d0

       !  -- [2-3] Non-Diagonal Component   --  !
       if ( k.eq.nSize ) then
          ! -- [    Last Row :: k == nSize ] -- !
          xvec(k) = Dinv * xvec(k)
       else
          ! -- [Not Last Row :: k != nSize ] -- !
          !  - Division    -  !
          Umat(k,k+1:nSize) = Dinv * Umat(k,k+1:nSize)
          xvec(k)           = Dinv * xvec(k)
          !  - subtraction -  !
          do j=k+1,nSize
             Umat(j,k+1:nSize) = Umat(j,k+1:nSize) - Umat(j,k) * Umat(k,k+1:nSize)
             xvec(j)           = xvec(j)           - Umat(j,k) * xvec(k)
             Umat(j,k)         = 0.d0
          enddo
       endif
       
    end do

    ! ----------------------------------------- !
    ! --- [3] Backward Substituition        --- !
    ! ----------------------------------------- !
    do k=nSize-1, 1, -1
       do i=nSize, k+1, -1
          xvec(k) = xvec(k) - Umat(k,i)*xvec(i)
       enddo
    enddo

    return
  end subroutine gaussElimin

end module gaussElimMod
