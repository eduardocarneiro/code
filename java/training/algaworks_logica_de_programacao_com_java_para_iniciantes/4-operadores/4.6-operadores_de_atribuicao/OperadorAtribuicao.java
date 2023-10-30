
public class OperadorAtribuicao {

	public static void main(String[] args) {
		
		System.out.println("[Operador]    [Tipo]           [Descri��o]");
		System.out.println("=             ATRIBUI��O       Atribui algum valor para a vari�vel");
		System.out.println("+= e -=       ATRIBUI��O       Faz a opera��o - adi��o ou subtra��o - e, depois, a atribui��o");
		System.out.println("*= e /=       ATRIBUI��O       Faz a opera��o - multiplica��o ou divis�o - e, depois, a atribui��o");
		System.out.println("%=            ATRIBUI��O       Faz a opera��o - m�dulo - e, depois, a atribui��o");
		
		System.out.println("");
		System.out.println("Exemplos:");
		System.out.println("-----------");
		
		// Operador de atribui��o de valor
		Integer numero1 = 1;
		System.out.println("numero1 = 1: " + numero1);
		
		// Operador de adi��o
		Integer numero2 = 1;
		numero2 += 1;
		System.out.println("numero2 += 1: " + numero2);
		
		// Operador de subtra��o
		Integer numero3 = 1;
		numero3 -= 1;
		System.out.println("numero3 -= 1: " + numero3);
		
		// Operador de multiplica��o
		Integer numero4 = 2;
		numero4 *= 2;
		System.out.println("numero4 *= 2: " + numero4);
		
		// Operador de divis�o
		Integer numero5 = 2;
		numero5 /= 2;
		System.out.println("numero5 /= 2: " + numero5);

		// Operador de module (resto)
		Double numero6 = 7.0;
		numero6 %= 4;
		System.out.println("numero6 %= 4: " + numero6);
		
		
	}
}
