using System.Collections.Generic;

public class Utils{

	public List<T> ListShuffle<T>(List<T> lista){
		int n = lista.Count;  
		T palavra;
		while (n > 1) {  
			n--;  
			System.Random rand = new System.Random();
			int rng = rand.Next(0,n-1);
			palavra = lista[rng];  
			lista[rng] = lista[n];  
			lista[n] = palavra;  
		}  
		return lista;
	}

}
