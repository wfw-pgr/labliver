module ioUtilityMod
contains

  ! ===================================== !
  ! === write out Result :: phi       === !
  ! ===================================== !
  subroutine writeResult( FileName )
    use variablesMod
    implicit none
    integer                  :: i, lun
    double precision         :: dx
    character(*), intent(in) :: FileName
    
    ! ------------------------------------- !
    ! --- [1] Preparation / Open File   --- !
    ! ------------------------------------- !
    if ( Flag__writeFile ) then
       lun = 50
       open(lun,file=trim(FileName),status='replace',form='formatted')
    else
       lun = 6
    endif
    dx = xMax / dble( nNode-1 ) + xMin
    ! ------------------------------------- !
    ! --- [2] write out                 --- !
    ! ------------------------------------- !
    do i=1, nNode
       write(lun,*) dx*dble(i-1)+xMin, phi(i)
    enddo
    ! ------------------------------------- !
    ! --- [3] Open File                 --- !
    ! ------------------------------------- !
    if ( Flag__writeFile ) close(lun)

    return
  end subroutine writeResult


  subroutine writeMatrix( Amat, xvec, bvec, nSize, MtrxFile )
    implicit none
    integer         , intent(in) :: nSize
    double precision, intent(in) :: Amat(nSize,nSize), xvec(nSize), bvec(nSize)
    character(*)    , intent(in) :: MtrxFile
    integer                      :: i, j
    integer                      :: lun = 50
    character(30)                :: fmt = '(f8.4,1x)'

    open(lun,file=trim(MtrxFile),status='replace',form='formatted')
    do i=1, nSize
       do j=1, nSize
          write(lun,trim(fmt),advance='no') Amat(i,j)
       enddo
       write(lun,trim(fmt),advance='yes') bvec(i)
    enddo
    close(lun)
    return
  end subroutine writeMatrix

  
end module ioUtilityMod
