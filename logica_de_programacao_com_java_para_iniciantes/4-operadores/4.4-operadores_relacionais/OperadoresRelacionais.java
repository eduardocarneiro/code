
public class OperadoresRelacionais {

	public static void main(String[] args) {
		
		System.out.println("Operadores relacionais");
		System.out.println("----------------------");
		System.out.println("");
		System.out.println("[Operador]    [Tipo]           [Descri��o]");
		System.out.println("> e >=        RELACIONAL       Maior que e maior ou igual a");
		System.out.println("< e <=        RELACIONAL       Menor que e menor ou igual a");
		System.out.println("== e !=       RELACIONAL       Igual e diferente");
		
		System.out.println("-----------------------------------------------------------");
		System.out.println("");
		
		// Operador relacional MAIOR ">";
		Boolean tresMaiorQueDois = 3 > 2;
		System.out.println("3 > 2? " + tresMaiorQueDois );
		
		// Operador relacional MAIOR OU IGUAL ">=";
		Boolean tresMaiorOuIgualATres = 3 >= 3;
		System.out.println("3 >= 3? " + tresMaiorOuIgualATres);
		
		// Operador relacional MENOR "<";
		Boolean tresMenorQueDois = 3 < 2 ;
		System.out.println("3 < 2? " + tresMenorQueDois);
		
		// Operador relacional MENOR OU IGUAL "<=";
		Boolean tresMenorOuIgualADois = 3 <= 2;
		System.out.println("3 <= 2? " + tresMenorOuIgualADois);
		
		// Operador relacional IGUAL "==";
		Boolean tresIgualATres = 3 == 3;
		System.out.println("3 == 3? " + tresIgualATres);
		
		// Operador relacional DIFERENTE "!=";
		Boolean tresEDiferenteDeTres = 3 != 3;
		System.out.println("3 != 3? " + tresEDiferenteDeTres);
		
		System.out.println("-------------");
		System.out.println("");
		System.out.println("Particularidade do \'==\' e o m�todo \'equals\'");
		System.out.println("A op��o de compara��o \'equals\' � dispon�vel para os tipos normais \' Integer, Double, Float e etc.");
		System.out.println("� ness�rio utilizar a op��o \'equals\' para fazer compara��o de igualdade, quando utilizado os Tipos normais");
		System.out.println("Por que, o operador \'==\', s� aceita at� o valor 127.");
		
		System.out.println("");
		System.out.println("Exemplo");
		System.out.println("-------");
		
		// Exemplo
		Integer centoEVinteOito01 = 128;
		Integer centoEVinteOito02 = 128;
		
		Boolean centoEVinteOitoEIgualACentoEVinteOito01 = centoEVinteOito01 == centoEVinteOito02;
		System.out.println("centoEVinteOito01 == centoEVinteOito02? " + centoEVinteOitoEIgualACentoEVinteOito01);
		
		Boolean centoEVinteOitoEIgualACentoEVinteOito02 = centoEVinteOito01.equals(centoEVinteOito02);
		System.out.println("centoEVinteOito01.equals(centoEVinteOito02)? " + centoEVinteOitoEIgualACentoEVinteOito02);
		
	}
}
