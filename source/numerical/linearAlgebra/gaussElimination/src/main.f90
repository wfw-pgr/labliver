! ====================================================== !
! === Gauss Elimination Example                      === !
! ====================================================== !
program main
  use gaussElimMod, only : gaussElimin
  implicit none
  integer         , parameter   :: nSize    = 3
  character(100)  , parameter   :: FileName = 'dat/eq.inp'
  double precision, allocatable :: Amat(:,:), bvec(:), xvec(:), res(:)
  integer                       :: i, j
  double precision              :: avg, std

  ! ------------------------------------- !
  ! --- [1] Data Load                 --- !
  ! ------------------------------------- !
  !  -- [1-1] Load from file          --  !
  allocate( Amat(nSize,nSize), bvec(nSize), xvec(nSize) )
  open(50,file=trim(FileName),status='old',form='formatted')
  do i=1, nSize
     read(50,*) Amat(i,:), bvec(i)
  enddo
  close(50)
  !  -- [1-2] input comfirmation      --  !
  write(6,*) 'input matrix | L.H.S. vector'
  do i=1, nSize
     write(6,*) Amat(i,:), '|', bvec(i)
  enddo
  write(6,*)

  ! ------------------------------------- !
  ! --- [2] Gauss Elimination         --- !
  ! ------------------------------------- !
  call gaussElimin( Amat, xvec, bvec, nSize )

  ! ------------------------------------- !
  ! --- [3] Answer Check              --- !
  ! ------------------------------------- !
  !  -- [3-1] calculate residual      --  !
  allocate( res(nSize) )
  do i=1, nSize
     res(i) = 0.d0
     do j=1, nSize
        res(i) = res(i) + Amat(i,j) * xvec(j)
     enddo
  enddo
  res(:) = bvec(:) - res(:)
  !  -- [3-2] output answer/residual  --  !
  write(6,*) 'answer :: x | residual '
  do i=1, nSize
     write(6,*) xvec(i), ' | ', res(i)
  enddo
  !  -- [3-3] statistical values      --  !
  avg = 0.d0
  std = 0.d0
  do i=1, nSize
     avg = avg + res(i)
     std = std + res(i)**2
  enddo
  avg = avg / dble( nSize )
  std = std / dble( nSize )
  std = sqrt( std - avg**2 )
  write(6,*) 'avg :: ', avg, 'std :: ', std
  
  return
end program main
