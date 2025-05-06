##############################################################
PHITSからのデータの抜き出し
##############################################################

=========================================================
shell で抜き出す ( grep, sed )
=========================================================


.. code-block:: bash

   slines=($(grep -n '#\s*e-lower\s*e-upper\s*photon\s*r\.err\s*' ./out/fluence_energy.dat | cut -d: -f1 ) )
   nItems=${#slines[@]}

   for ik in `seq 0 $((nItems-1))`
   do
       n=$((ik+1))
       s=${slines[$ik]}
       e=$((s+100))
       expression="${s},${e}p"
       echo $n $s $e ${expression}
       sed -n ${expression} out/fluence_energy.dat > result/fluence_energy_${n}.dat
   done


