program main
  use variablesMod, only : Kmat, phi, Fvec, nNode, MtrxFile, RsltFile
  use initiatorMod, only : initProblem
  use genMatrixMod, only : gen_Kmatrix, gen_Fvector
  use matrixInvMod, only : gaussElimin
  use ioUtilityMod, only : writeResult, writeMatrix
  implicit none

  call initProblem
  call gen_KMatrix
  call gen_fVector
  call writeMatrix( Kmat, phi, Fvec, nNode, trim(MtrxFile) )
  call gaussElimin( Kmat, phi, Fvec, nNode )
  call writeResult( trim(RsltFile) )
  
end program main
