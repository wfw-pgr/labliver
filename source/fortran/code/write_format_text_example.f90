program main
  implicit none
  double precision :: variable1 = 2.d-1
  character(100)   :: fmt = "('value',4x,'string',4x,(e12.5))"
  
  write(6,"(a,'')") "This is training of Fortran write format."
  write(6,*)
  write(6,"('value',4x,'string',4x,(e12.5))") variable1
  write(6,'("value",4x,"string",4x,(e12.5))') variable1
  write(6,fmt) variable1
  write(6,*)
  
end program main
