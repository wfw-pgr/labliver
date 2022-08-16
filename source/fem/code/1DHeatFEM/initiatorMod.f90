module initiatorMod
contains

  ! ===================================== !
  ! === Initiatialize Variables       === !
  ! ===================================== !
  subroutine initProblem
    use variablesMod
    implicit none

    ! ------------------------------------- !
    ! --- [1] Allocate & Initialize     --- !
    ! ------------------------------------- !
    allocate( phi(nNode), Fvec(nNode), Fvec_S(nNode), Fvec_V(nNode) )
    allocate( Kmat(nNode,nNode) )
    phi(:)    = 0.d0
    Fvec(:)   = 0.d0
    Fvec_S(:) = 0.d0
    Fvec_V(:) = 0.d0
    Kmat(:,:) = 0.d0
    
    return
  end subroutine initProblem

end module initiatorMod
