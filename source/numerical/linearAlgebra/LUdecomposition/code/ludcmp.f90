module recipes_LUDecomposit
contains
  SUBROUTINE ludcmp(a,n,np,indx,d)
    INTEGER n,np,indx(n)
    integer, parameter :: NMAX = 500
    real   , parameter :: tiny = 1.d-20
    REAL d
    double precision a(np, np)
    INTEGER i,imax,j,k
    REAL aamax,dum,sum,vv(NMAX)
    do i=1,n
       aamax=0.
       do j=1,n
          if (abs(a(i,j)).gt.aamax) aamax=abs(a(i,j))
       enddo
       if (aamax.eq.0.) then
          stop "singular matrix in ludcmp No nonzero largest element."
       endif
       vv(i)=1./aamax
    enddo
    do j=1,n
       do i=1,j-1
          sum=a(i,j)
          do k=1,i-1
             sum=sum-a(i,k)*a(k,j)
          enddo
          a(i,j)=sum
       enddo
       aamax=0.
       do i=j,n
          sum=a(i,j)
          do k=1,j-1
             sum=sum-a(i,k)*a(k,j)
          enddo
          a(i,j)=sum
          dum=vv(i)*abs(sum)
          if (dum.ge.aamax) then
             imax=i
             aamax=dum
          endif
       enddo
       if (j.ne.imax) then
          do k=1,n
             dum=a(imax,k)
             a(imax,k)=a(j,k)
             a(j,k)=dum
          enddo
          d=-d
          vv(imax)=vv(j)
       endif
       indx(j)=imax
       if(a(j,j).eq.0.) then
          a(j,j)=TINY
          if(j.ne.n) then
             dum=1./a(j,j)
             do i=j+1,n
                a(i,j)=a(i,j)*dum
             enddo
          endif
       end if
    end do
    return
  END SUBROUTINE ludcmp



  SUBROUTINE lubksb(a,n,np,indx,b)
    INTEGER n,np,indx(n)
    REAL a(np,np),b(n)
    INTEGER i,ii,j,ll REAL sum
    ii=0
    do i=1,n
       ll=indx(i)
       sum=b(ll)
       b(ll)=b(i)
       if (ii.ne.0)then
          do j=ii,i-1
             sum=sum-a(i,j)*b(j)
          enddo
       else if (sum.ne.0.) then
          ii=i
       endif
       b(i)=sum
    enddo
    do 14 i=n,1,-1 sum=b(i)
       do13 j=i+1,n
       sum=sum-a(i,j)*b(j)
    enddo
    b(i)=sum/a(i,i) enddo 14
    return
  END SUBROUTINE lubksb

end module recipes_LUDecomposit
