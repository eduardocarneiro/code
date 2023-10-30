public class ConversaoTiposPrimitivos {

	public static void main (String[] args) {
		// Convers�o de tipos primitivos
		// � poss�vel converter os tipos primitivos utilizando "casting"
		/* � poss�vel converter os tipos primitivos SEM utilizar o "casting" 
		   seguindo a seguinte ordem:
		   byte -> short \
			     |    -> int -> long -> float -> double
			   char  /
		*/

		// O "casting" � utilizando na ordem invertida da apresentada a cima.
		// n�o � recomendado fazer esta convers�o inversa, caso n�o tenha certeza que o valor da vari�vel convertida do tipo 64bits caiba em uma vari�vel tipo 32bits
		// exemplos
		
	       // casting que funciona
		long a = 10;
		int b = (int) a;
		System.out.println(b);

		//casting que N�O funciona
		long c = 123456789000L;
		int d = (int) c;
		System.out.println(d);
		// valor real de vari�vel c
		System.out.println("valor real de c: " + c);

	}
}
