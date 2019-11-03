public class PromocaoAritmetica {

	public static void main (String[] args) {
		
		/* � poss�vel promover uma vari�vel utilizando "casting" ou utilizando um outro tipo de vari�vel,
		 * e sempre � necess�rio seguir o modelo abaixo da esquerda para a direita. 
		 * byte -> short \
		 *                |--> int -> long -> float -> double
		 *         char  /
		 */

		int a = 10;
		long b = 5;
		long c = a + b;
		System.out.println(c);

		// Utilizando Casting

		int d = 5;
		int e = 3;
		float f =  d / (float) e;
		System.out.println(f);
	}
}
