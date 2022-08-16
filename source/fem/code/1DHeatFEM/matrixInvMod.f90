module matrixInvMod
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
    integer                       :: i, j, k
    double precision              :: Dinv
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
    ! --- [2] Upper Triangular Matrization  --- !
    ! ----------------------------------------- !
    do k=1, nSize

       !  -- [2-1] Diagonal Component       --  !
       if ( abs( Umat(k,k) ).lt.eps ) then
          write(6,*) '[gaussElimin] Amat != Regular Matrix :: No Solution End :: @ k= ', k
          stop
       endif
       Dinv      = 1.d0 / Umat(k,k)
       Umat(k,k) = 1.d0

       !  -- [2-2] Non-Diagonal Component   --  !
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

end module matrixInvMod
