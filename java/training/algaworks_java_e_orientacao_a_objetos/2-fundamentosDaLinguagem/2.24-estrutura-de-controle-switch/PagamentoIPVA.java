import java.util.Scanner;

public class PagamentoIPVA {
    
    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);
        
        System.out.print("Digite o final da placa: ");
        int finalPlaca = entrada.nextInt();

        switch ( finalPlaca) {
            case 1:
                System.out.println("Vencimento dia 11 de Janeiro");
                break;
            case 2: 
                System.out.println("Vencimento dia 12 de Janeiro");
                break;
            default:
                System.out.println("N/A");
                break;
        }

    }
}
