! ====================================================== !
! === Gauss Jordan Inverting Example                 === !
! ====================================================== !
program main
  use LU_DecompMod, only : LU_Decomposition, LU_BackSubstitution, LU_MatrixInverse
  implicit none
  character(100)  , parameter   :: AmatFile = 'dat/Amat.dat'
  character(100)  , parameter   :: LmatFile = 'dat/Lmat.dat'
  character(100)  , parameter   :: UmatFile = 'dat/Umat.dat'
  character(100)  , parameter   :: bvecFile = 'dat/bvec.dat'
  double precision, allocatable :: Amat(:,:), Lmat(:,:), Umat(:,:)
  double precision, allocatable :: Bmat(:,:), Ainv(:,:)
  double precision, allocatable :: bvec(:), xvec(:), avec(:)
  integer         , allocatable :: indx(:)
  integer                       :: i, j, nSize, nSize_
  integer         , parameter   :: lun = 50
  
  ! ------------------------------------- !
  ! --- [1] Data Load                 --- !
  ! ------------------------------------- !
  open(lun,file=trim(AmatFile),status='old',form='formatted')
  read(lun,*) nSize, nSize
  allocate( Amat(nSize,nSize), Lmat(nSize,nSize), Umat(nSize,nSize) )
  allocate( Bmat(nSize,nSize), Ainv(nSize,nSize) )
  allocate( indx(nSize) )
  Amat(:,:) = 0.d0
  Lmat(:,:) = 0.d0
  Umat(:,:) = 0.d0
  Bmat(:,:) = 0.d0
  do i=1, nSize
     read(lun,*) Amat(i,:)
  enddo
  close(lun)
  open(lun,file=trim(bvecFile),status='old',form='formatted')
  read(lun,*) nSize_
  if ( nSize.ne.nSize_ ) stop '[main] incompatible size Amat vs. bvec ERROR !!!'
  allocate( bvec(nSize), xvec(nSize), avec(nSize) )
  do i=1, nSize
     read(lun,*) bvec(i)
  enddo
  close(lun)
  
  ! ------------------------------------- !
  ! --- [2] LU Decomposition & solve  --- !
  ! ------------------------------------- !
  call LU_Decomposition   ( Amat, Lmat, Umat, indx, nSize )
  call LU_BackSubstitution( Lmat, Umat, bvec, xvec, indx, nSize )
  call LU_MatrixInverse   ( Amat, Ainv, nSize )
  
  ! ------------------------------------- !
  ! --- [3] save Results              --- !
  ! ------------------------------------- !
  open(lun,file=trim(LmatFile),status='replace',form='formatted')
  write(lun,*) nSize
  do i=1, nSize
     write(lun,*) Lmat(i,:)
  enddo
  open(lun,file=trim(UmatFile),status='replace',form='formatted')
  write(lun,*) nSize
  do i=1, nSize
     write(lun,*) Umat(i,:)
  enddo
  close(lun)
  ! ------------------------------------- !
  ! --- [4] confirm results           --- !
  ! ------------------------------------- !
  !  -- [4-1] input Amatrix           --  !
  write(6,*)
  write(6,*) 'Amat (input) '
  do i=1, nSize
     write(6,*) Amat(i,:)
  enddo
  !  -- [4-2] LU Decomposition        --  !
  write(6,*)
  write(6,*) 'Lmat | Umat (decomposed results) '
  do i=1, nSize
     write(6,*) Lmat(i,:), ' | ', Umat(i,:)
  enddo
  write(6,*)
  write(6,*) 'LU ( multiplied matrix )'
  Bmat = matmul( Lmat, Umat )
  do i=1, nSize
     write(6,*) Bmat(i,:)
  enddo
  write(6,*)
  write(6,*) 'A* ( permutated A matrix )  must be LU'
  do i=1, nSize
     write(6,*) Amat(indx(i),:)
  enddo
  write(6,*)
  write(6,*) 'permutation index ( i-th row ==> indx(i) )'
  do i=1, nSize
     write(6,*) i, indx(i)
  enddo
  !  -- [4-3] solve eqs.             --  !
  write(6,*)
  write(6,*) 'b ( L.H.S. )'
  do i=1, nSize
     write(6,*) bvec(i)
  enddo
  write(6,*)
  write(6,*) 'x ( Numerical Solution )'
  do i=1, nSize
     write(6,*) xvec(i)
  enddo
  avec(:) = matmul( Amat, xvec )
  write(6,*)
  write(6,*) 'residual of the solution  ( for  A-Matrix )'
  do i=1, nSize
     write(6,*) avec(i)
  enddo
  avec(:) = matmul( Bmat, xvec )
  write(6,*)
  write(6,*) 'residual of the solution  ( for LU-matrix )'
  do i=1, nSize
     write(6,*) avec(i)
  enddo
  !  -- [4-4] inverted Amat :: Ainv   --  !
  write(6,*) 'A^-1 ( inverted A matrix )'
  do i=1, nSize
     write(6,*) Ainv(i,:)
  enddo
  write(6,*)
  write(6,*) 'A^-1 A must be unit matrix'
  Bmat(:,:) = matmul( Ainv, Amat )
  do i=1, nSize
     write(6,*) Bmat(i,:)
  enddo
  write(6,*)
  write(6,*) 'A A^-1 must be unit matrix'
  Bmat(:,:) = matmul( Amat, Ainv )
  do i=1, nSize
     write(6,*) Bmat(i,:)
  enddo
  write(6,*)
  
  return
end program main
