import java.util.Scanner;

public class EstruturaDeControle1 {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        System.out.print("Nome: ");
        String nome = entrada.nextLine();
        
        System.out.print("Peso: ");
        int peso = entrada.nextInt();

        System.out.print("Altura: ");
        double altura = entrada.nextDouble();

        // Calculo do IMC
        double imc = peso / (altura * altura);

        System.out.println("IMC de " + nome + ": " + imc);

        // Validar IMC
        if (imc < 18.5) {
            System.out.println("Abaixo do peso Ideal.");
        } else if (imc < 25) {
            System.out.println("Peso Ideal");
        } else if (imc < 30) {
            System.out.println("Acima do peso");
        } else if (imc < 40) {
            System.out.println("Obesidade grau 1 ou 2");
        } else {
            System.out.println("Obesidade grau 3");
            System.out.println("Muito cuidado com seu peso!!!");
        }
    }
}