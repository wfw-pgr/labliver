#include <cstdio>
#include <cmath>

const int    iterMax = 10000000;
const int    i_write = 100;
const double dt      = 0.05;
const double      mp = 1.0;
const double      kh = 1.0;
const char*  posFile = "dat/position.dat";
const char*  engFile = "dat/energy.dat";

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

double calcEnergy( struct particleType *particle )
{
  double energy = 0.5 / mp * particle->pv*particle->pv 	\
    +             0.5 * kh * particle->qv*particle->qv;
  return energy;
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

void classical__euler( struct particleType *particle )
{
  // Hamiltonian :: H(q,p)
  //    ... dq/dt =   dH/dp
  //    ... dp/dt = - dH/dq
  double dq    =   dHdp_HO( particle->pv, particle->qv ) * dt;
  double dp    = - dHdq_HO( particle->pv, particle->qv ) * dt;
  particle->qv = particle->qv + dq;
  particle->pv = particle->pv + dp;
  return;
}

void runge_kutta__2nd( struct particleType *particle )
{
  // Hamiltonian :: H(q,p)
  //    ... dq/dt =   dH/dp
  //    ... dp/dt = - dH/dq
  double kp1   =   dHdp_HO( particle->pv, particle->qv );
  double kq1   =   dHdq_HO( particle->pv, particle->qv );
  double pvm   =   particle->pv - kq1*dt;
  double qvm   =   particle->qv + kp1*dt;
  double kp2   =   dHdp_HO( pvm, qvm );
  double kq2   =   dHdq_HO( pvm, qvm );
  particle->qv = particle->qv + 0.5*( kp1 + kp2 )*dt;
  particle->pv = particle->pv - 0.5*( kq1 + kq2 )*dt;
  return;
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
  struct particleType *particle1;
  struct particleType *particle2;
  struct particleType *particle3;
  double time    = 0.0;
  double eng1, eng2, eng3;
  FILE   *fp, *fe;

  // ------------------------------------------------------ //
  // ---  [2]  Preparation                              --- //
  // ------------------------------------------------------ //
  // -- [2-1]  Definition of Particles                   -- //
  printf( "[practice.cpp] Output File ==>  %s\n", posFile );
  printf( "[practice.cpp] Output File ==>  %s\n", engFile );
  particle1 = new particleType;
  particle2 = new particleType;
  particle3 = new particleType;
  initialize_particle( particle1 );
  initialize_particle( particle2 );
  initialize_particle( particle3 );
  // -- [2-2]  output preparation                        -- //
  printf( "[practice.cpp] Begin tracking a particle.\n" );
  fp = fopen( posFile, "w" );
  fe = fopen( engFile, "w" );
  fprintf( fp, "# time q1 p1 q2 p2 q3 p3\n" );
  fprintf( fe, "# time energy1 energy2 energy3\n" );
  
  // ------------------------------------------------------ //
  // ---  [3] Main Loop of Euler type Integration       --- //
  // ------------------------------------------------------ //
  time = 0.0;
  for ( int i=1; i <=iterMax; i++ ){
    time = time + dt;
    classical__euler( particle1 );
    runge_kutta__2nd( particle2 );
    symplectic_euler( particle3 );
    eng1 = calcEnergy( particle1 );
    eng2 = calcEnergy( particle2 );
    eng3 = calcEnergy( particle3 );
    if ( i%i_write == 0 ){
      fprintf( fp, "%12.5e %12.5e %12.5e %12.5e %12.5e %12.5e %12.5e\n", time, \
	       particle1->qv, particle1->pv,				\
	       particle2->qv, particle2->pv,				\
	       particle3->qv, particle3->pv );
      fprintf( fe, "%12.5e %12.5e %12.5e %12.5e\n", time, eng1, eng2, eng3 );
    }
  }

  // ------------------------------------------------------ //
  // ---  [4] Post Process                              --- //
  // ------------------------------------------------------ //
  fclose( fp );
  return 0;

}
