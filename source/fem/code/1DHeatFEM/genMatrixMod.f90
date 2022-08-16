module genMatrixMod
contains

  ! ===================================== !
  ! === generate [K] Matrix           === !
  ! ===================================== !
  subroutine gen_Kmatrix
    use variablesMod
    implicit none
    integer          :: i
    double precision :: coef

    ! ------------------------------------- !
    ! --- [1] Prepartion                --- !
    ! ------------------------------------- !
    coef = lambda * Area / Lelem
    
    ! ------------------------------------- !
    ! --- [2] k-Matrix Generation       --- !
    ! ------------------------------------- !
    ! -- [2-1] k-Matrix initialize      --  !
    Kmat(:,:) = 0.d0
    ! -- [2-2] row=1     (Left Edge  )  --  !
    Kmat(1,1) = + 1.d0
    Kmat(1,2) = - 1.d0
    ! -- [2-3] intermedite Region       --  !
    do i=2, nNode-1
       Kmat(i,i-1) = -1.d0
       Kmat(i,i  ) = +2.d0
       Kmat(i,i+1) = -1.d0
    enddo
    ! -- [2-4] row=nElem (Right Edge )  --  !
    Kmat(nNode,nNode-1) = - 1.d0
    Kmat(nNode,nNode  ) = + 1.d0
    ! -- [2-5] coefficient              --  !
    Kmat(:,:) = coef * Kmat(:,:)
    
    ! ------------------------------------- !
    ! --- [3] Boundary Condition        --- !
    ! ------------------------------------- !
    !  -- [3-1] Dirichlet Boundary      --  !
    Kmat(1,1)       = 1.d0
    Kmat(1,2:nNode) = 0.d0

    return
  end subroutine gen_Kmatrix


  ! ===================================== !
  ! === generate {F} vector           === !
  ! ===================================== !
  subroutine gen_Fvector
    use variablesMod
    implicit none
    integer          :: i
    double precision :: coefS, coefV

    ! ------------------------------------- !
    ! --- [1] Preparation               --- !
    ! ------------------------------------- !
    coefV     = 0.5d0 * dQdt * Area * Lelem
    coefS     = qedge * Area
    Fvec_S(:) = 0.d0
    Fvec_V(:) = 0.d0
    Fvec(:)   = 0.d0

    ! ------------------------------------- !
    ! --- [2] {F}(surface) term         --- !
    ! ------------------------------------- !
    !  -- [2-1] @ Free Boundary Cond.   --  !
    Fvec_S(nNode) = 1.d0
    !  -- [2-2] coefficient             --  !
    Fvec_S(:)     = coefS * Fvec_S(:)
    
    ! ------------------------------------- !
    ! --- [3] {F}(volume)  term         --- !
    ! ------------------------------------- !
    !  -- [2-1] @ Free Boundary Cond.   --  !
    Fvec_V(    1) = 1.d0
    do i=2, nNode-1
       Fvec_V(i) = 2.d0
    enddo
    Fvec_V(nNode) = 1.d0
    !  -- [2-2] coefficient             --  !
    Fvec_V(:)     = coefV * Fvec_V(:)

    ! ------------------------------------- !
    ! --- [4] total R.H.S.              --- !
    ! ------------------------------------- !
    Fvec(:) = Fvec_S(:) + Fvec_V(:)

    ! ------------------------------------- !
    ! --- [5] Boundary Condition        --- !
    ! ------------------------------------- !
    !  -- [5-1] Dirichlet Boundary      --  !
    Fvec(1) = Tedge
    
    return
  end subroutine gen_Fvector

  
end module genMatrixMod
