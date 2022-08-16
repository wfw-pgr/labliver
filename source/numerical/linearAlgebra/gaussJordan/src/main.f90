! ====================================================== !
! === Gauss Jordan Inverting Example                 === !
! ====================================================== !
program main
  use gausJordaMod, only : gaussJordan
  implicit none
  character(100)  , parameter   :: AmatFile = 'dat/Amat.dat'
  character(100)  , parameter   :: BmatFile = 'dat/Bmat.dat'
  double precision, allocatable :: Amat(:,:), Bmat(:,:), Cmat(:,:)
  integer                       :: i, j, nSize
  integer         , parameter   :: lun = 50

  ! ------------------------------------- !
  ! --- [1] Data Load                 --- !
  ! ------------------------------------- !
  open(lun,file=trim(AmatFile),status='old',form='formatted')
  read(lun,*) nSize, nSize
  allocate( Amat(nSize,nSize), Bmat(nSize,nSize), Cmat(nSize,nSize) )
  Amat(:,:) = 0.d0
  Bmat(:,:) = 0.d0
  Cmat(:,:) = 0.d0
  do i=1, nSize
     read(lun,*) Amat(i,:)
  enddo
  close(lun)

  ! ------------------------------------- !
  ! --- [2] Gauss Elimination         --- !
  ! ------------------------------------- !
  call gaussJordan( Amat, Bmat, nSize )
  
  ! ------------------------------------- !
  ! --- [3] save Results              --- !
  ! ------------------------------------- !
  open(lun,file=trim(BmatFile),status='replace',form='formatted')
  write(lun,*) nSize
  do i=1, nSize
     write(lun,*) Bmat(i,:)
  enddo
  close(lun)
  ! ------------------------------------- !
  ! --- [4] confirm results           --- !
  ! ------------------------------------- !
  do i=1, nSize
     write(6,*) Amat(i,:), ' | ', Bmat(i,:)
  enddo
  Cmat = matmul( Amat, Bmat )
  do i=1, nSize
     write(6,*) Cmat(i,:)
  enddo
  
  return
end program main
