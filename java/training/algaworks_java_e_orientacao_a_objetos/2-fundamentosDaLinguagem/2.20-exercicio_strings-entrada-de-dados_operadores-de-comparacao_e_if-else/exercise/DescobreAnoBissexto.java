import java.util.Scanner;

public class DescobreAnoBissexto {

	public static void main (String[] args) {
	
	Scanner entrada = new Scanner(System.in);

	// Solicitar ao usu�rio o ano para a verificacao
	System.out.print("Ano: ");
	int ano = entrada.nextInt();

	if ( ano % 400 == 0) {
		System.out.println("O ano " + ano + " � um ano bissexto");
	
	} else if (ano % 4 == 0) {
		if ( ano % 100 != 0) {
			System.out.println("O ano " + ano + " � un ano bissexto");
		}
	} else {
		System.out.println("O ano " + ano + " n�o � um ano bissexto");
	}

	}
}
