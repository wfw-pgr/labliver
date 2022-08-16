! ====================================================== !
! === Gauss Jordan Method :: partial pivoting ver.   === !
! ====================================================== !
module gausJordaMod
contains

  ! ========================================================== !
  ! === Gauss Jordan Matrix Inversion                      === !
  ! ========================================================== !
  subroutine gaussJordan( Amat, Bmat, nSize )
    implicit none
    integer         , intent(in)  :: nSize
    double precision, intent(in)  :: Amat(nSize,nSize)
    double precision, intent(out) :: Bmat(nSize,nSize)
    integer                       :: i, j, k, ipivot
    double precision              :: Dinv, Dval, vpivot, buff
    double precision, parameter   :: eps = 1.d-10
    double precision, allocatable :: Umat(:,:)

    ! ----------------------------------------- !
    ! --- [1] Preparation                   --- !
    ! ----------------------------------------- !
    !  -- [1-1] allocate Umat               --  !
    allocate( Umat(nSize,nSize) )
    !  -- [1-2] Copy AMat & bvec            --  !
    do j=1, nSize
       do i=1, nSize
          Umat(i,j) = Amat(i,j)
       enddo
    enddo
    do j=1, nSize
       do i=1, nSize
          if ( i.eq.j ) then
             Bmat(i,j) = 1.d0
          else
             Bmat(i,j) = 0.d0
          endif
       enddo
    enddo
    
    ! ----------------------------------------- !
    ! --- [2] Upper Triangular Matrization  --- !
    ! ----------------------------------------- !
    do k=1, nSize
       !  -- [2-1] Partial pivot selection   -- !
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
          do j=1, nSize
             buff           = Bmat(ipivot,j)
             Bmat(ipivot,j) = Bmat(k     ,j)
             Bmat(k     ,j) = buff
          enddo
       end if
       !  -- [2-2] Singular Matrix Detection -- !
       if ( abs( Umat(k,k) ).lt.eps ) then
          write(6,*) '[gaussElimin] Amat :: Singular Matrix :: No Solution End :: @ k= ', k
          stop
       endif
       !  -- [2-3] For pivot row            --  !
       !  --      a'(k,:) = a(k,:) / a(k,k) --  !
       Dinv                = 1.d0 / Umat(k,k)
       Umat(k,k)           = 1.d0
       Umat(k,(k+1):nSize) = Dinv * Umat(k,(k+1):nSize)
       Bmat(k,    1:nSize) = Dinv * Bmat(k,    1:nSize)
       !  -- [2-4] For Non-pivot row        --  !
       !  --      a'(j,:) = a(j,:) - a(j,k) * a(k,:) --  !
       do j=1, nSize
          if ( j.ne.k ) then
             Dval            = Umat(j,k)
             Umat(j,k:nSize) = Umat(j,k:nSize) - Dval * Umat(k,k:nSize)
             Bmat(j,1:nSize) = Bmat(j,1:nSize) - Dval * Bmat(k,1:nSize)             
          endif
       enddo
    end do

    return
  end subroutine gaussJordan

end module gausJordaMod
