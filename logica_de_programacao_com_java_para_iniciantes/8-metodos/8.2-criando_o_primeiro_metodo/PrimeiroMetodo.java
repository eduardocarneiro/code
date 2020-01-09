import java.util.Scanner;

public class PrimeiroMetodo {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		
		String[] cursosDisponiveis = new String[] {"Java B�sico", "Spring Suite", "Java OO avan�ado"};
		
		System.out.println("Curso dispon�veis:");
		ImprimirTraco();
		
		for (int i = 0; i < cursosDisponiveis.length; i++) {
			
			System.out.println("[" + i + "] - " + cursosDisponiveis[i]);
		}
		
		ImprimirTraco();
		System.out.println("");
		
		System.out.print("Digite a op��o para curso desejado: ");
		Integer cursoEscolhido = scanner.nextInt();
		
		// PAGAMENTO
		
		String[] formaDePagamento = new String[] {"Transfer�ncia Banc�ria", "Boleto", "Cart�o de D�bito", "Cart�o de cr�dito"};
		
		ImprimirTraco();
		System.out.println("");
				
		System.out.println("Formas de pagamento:");
		ImprimirTraco();
		
		for (int j = 0; j < formaDePagamento.length ; j++) {
			
			System.out.println("[" + j + "] - " + formaDePagamento[j]);
		}
		
		System.out.print("Escolha a op��o de pagamento: ");
		Integer opcaoDePagamento = scanner.nextInt();
		
				System.out.println("O curso escolhido foi: " + cursosDisponiveis[cursoEscolhido] + " e a forma de pagamento: " + formaDePagamento[opcaoDePagamento]);
				
		scanner.close();	
	}
	
	static void ImprimirTraco() {
		System.out.println("-----------------------");
	}
}
