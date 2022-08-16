module variablesMod
  implicit none
  integer         , parameter   :: nNode  = 5
  integer         , parameter   :: nElem  = nNode-1
  double precision, parameter   :: lambda = 1.d0
  double precision, parameter   :: Area   = 1.d0
  double precision, parameter   :: xMin   = 0.d0
  double precision, parameter   :: xMax   = 1.d0
  double precision, parameter   :: Lelem  = ( xMax-xMin ) / nElem
  double precision, parameter   :: dQdt   = 2.d0
  double precision, parameter   :: qedge  = 0.d0
  double precision, parameter   :: Tedge  = 0.d0
  double precision, allocatable :: phi(:), Kmat(:,:), Fvec(:)
  double precision, allocatable :: Fvec_S(:), Fvec_V(:)
  character(100)  , parameter   :: MtrxFile = 'dat/matrix.dat'
  character(100)  , parameter   :: RsltFile = 'dat/result.dat'
  logical         , parameter   :: Flag__writeFile = .true.
  
end module variablesMod
