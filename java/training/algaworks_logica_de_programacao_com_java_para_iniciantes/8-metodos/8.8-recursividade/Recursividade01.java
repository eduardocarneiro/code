
public class Recursividade01 {

	public static void main(String[] args) {
		// Recursividade � quando voc� tem um m�todo chamando o pr�prio m�todo.
		
		ImprimirNumero(0);
		
	}
	
	static void ImprimirNumero(Integer numero) {
		
		if (numero <= 10) {
			System.out.println(numero);
			ImprimirNumero(++numero);
		}
	}
}
