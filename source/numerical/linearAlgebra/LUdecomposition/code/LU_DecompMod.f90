module LU_DecompMod
contains

  ! ====================================================== !
  ! === LU Decomposition Routines                      === !
  ! ====================================================== !
  subroutine LU_Decomposition( Amat, Lmat, Umat, indx, nSize )
    implicit none
    integer         , intent(in)    :: nSize
    double precision, intent(in)    :: Amat(nSize,nSize)
    double precision, intent(out)   :: Lmat(nSize,nSize), Umat(nSize,nSize)
    integer         , intent(out)   :: indx(nSize)
    integer                         :: i, j, k, iMax, ibuff
    double precision, allocatable   :: Bmat(:,:), vv(:)
    double precision                :: BBMax, dbuff, sum
    double precision, parameter     :: eps = 1.d-20
    ! ------------------------------------------------------ !
    ! --  indx(nSize) :: permutation index.               -- !
    ! --                   to avoid Numerical error       -- !
    ! --                           ( == pivot selection)  -- !
    ! --      LU(i,:) = A( indx(i),: )                    -- !
    ! ------------------------------------------------------ !
    
    ! ------------------------------------------------------ !
    ! --- [1] Singular Matrix Detection & vv Info        --- !
    ! ------------------------------------------------------ !
    !  -- [1-1] prepare index / Bmat                     --  !
    allocate( Bmat(nSize,nSize), vv(nSize) )
    do i=1, nSize
       indx(i) = i
    enddo
    do j=1, nSize
       do i=1, nSize
          Bmat(i,j) = Amat(i,j)
       enddo
    enddo
    !  -- [1-2] large value check for permutation        --  !
    do i=1, nSize
       BBMax = 0.d0
       do j=1, nSize
          if ( abs( Bmat(i,j) ).gt.BBMax ) BBMax = abs( Bmat(i,j) )
       enddo
       if ( BBmax.eq.0.d0 ) then
          write(6,*) "[LU_Decomposition] Singular Matrix !!! ERROR !!!"
       endif
       vv(i) = 1.d0 / BBMax
    enddo
    ! ------------------------------------------------------ !
    ! --- [2] Main Loop of the LU Decomposition          --- !
    ! ------------------------------------------------------ !
    do j=1, nSize  ! -- main loop -- !
       !  -- [2-1] col-wise ( horizontal scan )          --  !
       do i=1, j-1
          sum = Bmat(i,j)
          do k=1, i-1
             sum = sum - Bmat(i,k)*Bmat(k,j)
          enddo
          Bmat(i,j) = sum
       enddo
       BBMax = 0.d0
       !  -- [2-2] row-wise ( vertical scan )            --  !
       do i=j, nSize
          sum = Bmat(i,j)
          do k=1, j-1
             sum = sum - Bmat(i,k)*Bmat(k,j)
          enddo
          Bmat(i,j) = sum
          dbuff     = vv(i) * abs(sum)
          if ( dbuff.ge.BBMax ) then
             iMax  = i
             BBMax = dbuff
          endif
       enddo
       !  -- [2-3] permutation :: exchange Bmat & indx   --  !
       if ( j.ne.iMax ) then
          do k=1, nSize
             dbuff        = Bmat(iMax,k)
             Bmat(iMax,k) = Bmat(j,k)
             Bmat(j,k)    = dbuff
          enddo
          vv(iMax)   = vv(j)
          ibuff      = indx(j)
          indx(j)    = indx(iMax)
          indx(iMax) = ibuff
       endif
       !  -- [2-4] singular matrix :: mild prescription  --  !
       if ( Bmat(j,j).eq.0.d0 ) then
          Bmat(j,j) = eps
       endif
       !  -- [2-5] Diagonal component 1 / D              --  !
       if ( j.ne.nSize ) then
          dbuff = 1.d0 / Bmat(j,j)
          do i=j+1, nSize
             Bmat(i,j) = Bmat(i,j) * dbuff
          enddo
       endif
    enddo  ! -- main loop end -- !
    ! ------------------------------------------------------ !
    ! --- [3] store Lmat & Umat for easy use             --- !
    ! ------------------------------------------------------ !
    do i=1, nSize
       !  -- [3-1] B( i, j=1~i-1   ) ==> Lmat            --  !
       do j=1, i-1
          Lmat(i,j) = Bmat(i,j)
       enddo
       !  -- [3-2] Diagonal Component of Lmat == 1       --  !
       Lmat(i,i) = 1.d0
       !  -- [3-3] B( i, j=i~nSize ) ==> Umat            --  !
       do j=i, nSize
          Umat(i,j) = Bmat(i,j)
       enddo
    enddo
    return
  end subroutine LU_Decomposition


  ! ====================================================== !
  ! === Backward Substitution Method                   === !
  ! ====================================================== !
  subroutine LU_BackSubstitution( Lmat, Umat, bvec, xvec, indx, nSize )
    implicit none
    integer         , intent(in)  :: nSize
    integer         , intent(in)  :: indx(nSize)
    double precision, intent(in)  :: bvec(nSize)
    double precision, intent(in)  :: Lmat(nSize,nSize), Umat(nSize,nSize)
    double precision, intent(out) :: xvec(nSize)
    integer                       :: i, j, ii, ll
    double precision              :: sum

    ! ------------------------------------------------------ !
    ! --- [1] prepare for back substition                --- !
    ! ------------------------------------------------------ !
    do i=1, nSize
       xvec(i) = bvec(indx(i))
    enddo
    ! ------------------------------------------------------ !
    ! --- [2] solve Ly = b    ( Ax = LUx = Ly = b )      --- !
    ! ------------------------------------------------------ !
    ii=0
    do i=1, nSize
       sum = xvec(i)
       if ( ii.ne.0 ) then
          do j=ii,i-1
             sum = sum - Lmat(i,j) * xvec(j)
          enddo
       else if ( sum.ne.0 ) then
          ii = i
       endif
       xvec(i)  = sum
    enddo
    ! ------------------------------------------------------ !
    ! --- [3] solve Ux = y  using above y                --- !
    ! ------------------------------------------------------ !
    do i=nSize, 1, -1
       sum = xvec(i)
       do j=i+1, nSize
          sum = sum - Umat(i,j) * xvec(j)
       end do
       xvec(i) = sum / Umat(i,i)
    enddo
    
    return
  end subroutine LU_BackSubstitution


  ! ====================================================== !
  ! === LU_MatrixInverse                               === !
  ! ====================================================== !
  subroutine LU_MatrixInverse( Amat, Ainv, nSize )
    implicit none
    integer         , intent(in)  :: nSize
    double precision, intent(in)  :: Amat(nSize,nSize)
    double precision, intent(out) :: Ainv(nSize,nSize)
    integer                       :: i, j
    integer         , allocatable :: indx(:)
    double precision, allocatable :: Lmat(:,:), Umat(:,:), xvec(:), bvec(:)

    ! ------------------------------------------------------ !
    ! --- [1] preparation of matrix & indx               --- !
    ! ------------------------------------------------------ !
    allocate( Lmat(nSize,nSize), Umat(nSize,nSize), indx(nSize) )
    allocate( xvec(nSize), bvec(nSize) )
    do j=1, nSize
       do i=1, nSize
          Ainv(i,j) = 0.d0
       enddo
       Ainv(j,j) = 1.d0
    enddo
    ! ------------------------------------------------------ !
    ! --- [2] LU Decomposition                           --- !
    ! ------------------------------------------------------ !
    call LU_Decomposition( Amat, Lmat, Umat, indx, nSize  )
    ! ------------------------------------------------------ !
    ! --- [3] matrix Inversion by back-substitution      --- !
    ! ------------------------------------------------------ !
    do j=1, nSize
       do i=1, nSize
          xvec(i)   = 0.d0
          bvec(i)   = Ainv(i,j)
       enddo
       call LU_BackSubstitution( Lmat, Umat, bvec, xvec, indx, nSize )
       do i=1, nSize
          Ainv(i,j) = xvec(i)
       enddo
    enddo

    return
  end subroutine LU_MatrixInverse


end module LU_DecompMod
