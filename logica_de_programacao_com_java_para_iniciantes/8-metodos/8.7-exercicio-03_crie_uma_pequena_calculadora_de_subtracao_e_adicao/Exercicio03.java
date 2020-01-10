import java.util.Scanner;

public class Exercicio03 {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		
		String[] operacaoMatematica = new String[] {"Soma", "Subtra��o", "Divis�o", "Multiplica��o"}; 
		
		System.out.print("Digite o primeiro n�mero: ");
		Integer primeiroNumero = scanner.nextInt();
		
		System.out.print("Digite o segundo n�mero: ");
		Integer segundoNumero = scanner.nextInt();
		
		System.out.println("");
		System.out.println("---------------------------------------");
		
		for (int i = 0; i < operacaoMatematica.length; i++) {
			System.out.println("[" + i + "]" + " - " + operacaoMatematica[i]);	
		}
		
		System.out.print("Digite a opera��o matem�tica desejada: ");
		Integer opcaoMatematica = scanner.nextInt();
		
		switch(opcaoMatematica) {
		
		case 0:
			//System.out.println("Op��o: " + opcaoMatematica);
			Integer resultadoSoma = soma(primeiroNumero, segundoNumero); 
			System.out.println("Resultado: " + primeiroNumero + " + " + segundoNumero + " = " + resultadoSoma);
			break;
			
		case 1:
			
			//System.out.println("Op��o: " + opcaoMatematica);
			Integer resultadoSubtracao = subtracao(primeiroNumero, segundoNumero); 
			System.out.println("Resultado: " + primeiroNumero + " - " + segundoNumero + " = " + resultadoSubtracao);
			break;
			
		case 2:
			
			//System.out.println("Op��o: " + opcaoMatematica);
			Integer resultadoDivisao = divisao(primeiroNumero, segundoNumero); 
			System.out.println("Resultado: " + primeiroNumero + " / " + segundoNumero + " = " + resultadoDivisao);
			break;
			
		case 3:
			
			//System.out.println("Op��o: " + opcaoMatematica);
			Integer resultadoMultiplicacao = multiplicacao(primeiroNumero, segundoNumero); 
			System.out.println("Resultado: " + primeiroNumero + " * " + segundoNumero + " = " + resultadoMultiplicacao);
			break;
		
		default: 
			System.err.println("Op��o Inv�lida.");
			break;
				
		}
		
		scanner.close();
	}
	
	static Integer soma(Integer recebePrimeiroValor, Integer recebeSegundoValor) {
		
		Integer calculoSoma = recebePrimeiroValor + recebeSegundoValor;
		return calculoSoma;
	}
	
	static Integer subtracao(Integer recebePrimeiroValor, Integer recebeSegundoValor) {
		
		Integer calculoSubtracao = recebePrimeiroValor - recebeSegundoValor;
		return calculoSubtracao;
	}
	
	static Integer divisao(Integer recebePrimeiroValor, Integer recebeSegundoValor) {
	
		Integer calculaDivisao = recebePrimeiroValor / recebeSegundoValor;
		return calculaDivisao;
	}

	static Integer multiplicacao(Integer recebePrimeiroValor, Integer recebeSegundoValor) {
		
		Integer CalculaMultiplicacao = recebePrimeiroValor * recebeSegundoValor;
		return CalculaMultiplicacao;
	}
	
}
