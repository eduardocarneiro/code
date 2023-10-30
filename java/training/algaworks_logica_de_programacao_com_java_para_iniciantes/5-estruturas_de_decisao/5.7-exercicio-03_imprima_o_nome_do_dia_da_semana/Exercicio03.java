import java.util.Scanner;

public class Exercicio03 {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("Digite o n�mero do dia da semana: ");
		Integer numeroDiaDaSemana = scanner.nextInt();
		
		String diaDaSemana = "";
		
		switch (numeroDiaDaSemana) {
		
		case 1: 
			diaDaSemana = "Domingo";
			break;
		case 2: 
			diaDaSemana = "Segunda-Feira";
			break;
		case 3: 
			diaDaSemana = "Ter�a-Feira";
			break;
		case 4: 
			diaDaSemana = "Quarta-Feira";
			break;
		case 5: 
			diaDaSemana = "Quinta-Feira";
			break;
		case 6: 
			diaDaSemana = "Sexta-Feira";
			break;
		case 7: 
			diaDaSemana = "S�bado";
			break;
		default: 
			System.err.println("N�mero inv�lido");
			System.exit(1);
		}
		
		System.out.println("O dia da semana �: " + diaDaSemana);
		scanner.close();
	}
}