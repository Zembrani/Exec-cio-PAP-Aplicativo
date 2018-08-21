#include<iostream>

void QuickSort(parada registro){
	int   i, j, pivo, aux, fim;
	fim = registro.size();
   	i = 0;
   	j = fim;
   	pivo = registro(i + j) / 2]
      	while(i < j){
       	    while (registro[i] < pivo)
       	    	i++;
       	    
       	    while (registro[j] > pivo)
       	    	j;
       	    
       	    if (i < j){
       	    	aux  = registro[i];
       	    	registro[i] = registro[j];
       	    	registroj] = aux;
       	    	i++;
       	    	j--;
       	    }
       	}
       	if (0 < j)
       		QuickSort(registro, 0, j);
       
       	if (i < fim)
       		QuickSort(registro, i, fim);
}