import java.util.Scanner;

public class PrimeiroMetodo3 {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		
		String[] cursosDisponiveis = new String[] {"Java B�sico", "Spring Suite", "Java OO avan�ado"};
		
		System.out.println("Curso dispon�veis:");
		ImprimirTraco();
		
		// realiza o for da itera��o. EXERCICIO de passagem de paramentro para o metodo
		IteracaoFor(cursosDisponiveis);
		
		// Imprimi o tra�o e o espa�o.
		ImprimirTraco();
		ImprimirEspaco();
		
		System.out.print("Digite a op��o para curso desejado: ");
		Integer cursoEscolhido = scanner.nextInt();
		
		ImprimirEspaco();
		System.out.println(cursosDisponiveis[cursoEscolhido]);
		
		scanner.close();
	}	
	
	static void ImprimirTraco() {
		System.out.println("-----------------------");
	}
	
	static void ImprimirEspaco() {
		System.out.println("");
	}
	
	static void IteracaoFor(String[] vetor) {
		for (int i = 0; i < vetor.length; i++) {
			System.out.println("[" + i + "] - " + vetor[i]);
		}
	}
}
