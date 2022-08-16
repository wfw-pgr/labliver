#include <cstdio>
#include <cmath>

const int    iterMax = 100000;
const int    i_write = 10;
const double      mp = 1.0;
const double      kh = 1.0;
const double      dt = 0.0005;
const  char* posFile = "dat/position.dat";

struct particleType
{
  double qv;
  double pv;
};

void initialize_particle( struct particleType *particle )
{
  particle->qv = 0.01;
  particle->pv = 0.00;
}

double dHdq_HO( double pv, double qv )
{
  // Hamltonian H(q,p) = 1/2m p^2 + 1/2 k q^2
  //            dH/dq  = kq
  return  kh * qv;
}

double dHdp_HO( double pv, double qv )
{
  // Hamltonian H(q,p) = 1/2m p^2 + 1/2 k q^2
  //            dH/dp  = p / m
  return  pv / mp;
}

void symplectic_euler( struct particleType *particle )
{
  // Hamiltonian :: H(q,p)
  //    ... dq/dt =   dH/dp
  //    ... dp/dt = - dH/dq
  double dp    = - dHdq_HO( particle->pv, particle->qv ) * dt;
  particle->pv = particle->pv + dp;
  double dq    =   dHdp_HO( particle->pv, particle->qv ) * dt;
  particle->qv = particle->qv + dq;
  return;
}

int main(void)
{
  
  // ------------------------------------------------------ //
  // ---  [1]  Variable Definitions                     --- //
  // ------------------------------------------------------ //
  struct particleType *particle;
  double         time    = 0.0;
  FILE           *fp;

  // ------------------------------------------------------ //
  // ---  [2]  Preparation                              --- //
  // ------------------------------------------------------ //
  // -- [2-1]  Definition of Particles                   -- //
  printf( "[practice.cpp] Output File ==>  %s\n", posFile );
  particle = new particleType;
  initialize_particle( particle );
  // -- [2-2]  output preparation                        -- //
  printf( "[practice.cpp] Begin tracking a particle.\n" );
  fp = fopen( posFile, "w" );
  fprintf( fp, "# time q p\n" );
  
  // ------------------------------------------------------ //
  // ---  [3] Main Loop of Euler type Integration       --- //
  // ------------------------------------------------------ //
  time = 0.0;
  for ( int i=1; i <=iterMax; i++ ){
    time = time + dt;
    symplectic_euler( particle );
    if ( i%i_write == 0 ){
      fprintf( fp, "%12.5e %12.5e %12.5e\n", time, particle->qv, particle->pv );
    }
  }

  // ------------------------------------------------------ //
  // ---  [4] Post Process                              --- //
  // ------------------------------------------------------ //
  fclose( fp );  
  return 0;

}
