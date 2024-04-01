import java.util.Scanner;

public class DescobreAnoBissexto2 {
    
    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);
        System.out.print("Digite um ano: ");
        int ano = entrada.nextInt();

        // validando se o ano eh bissexto

        if (ano % 400 == 0 ) { // todos multiplos de 400 soa bissextos
            System.out.println("O ano \"" + ano + "\" eh um ano bissexto");
        } else if (ano % 4 == 0){
            if (ano % 100 != 0) {
                System.out.println("O ano \"" + ano + "\" eh um ano bissexto");
            } else {
                System.out.println("O ano \"" + ano + "\" NAO eh um ano bissexto");
            }
        } else {
            System.out.println("O ano \"" + ano + "\" nao eh um ano bissexto");
        }
    }
}
