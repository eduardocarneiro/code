import java.util.Scanner;

public class Exercicio02 {
	
	static final Integer BONUS = 80;
	
	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("Meta do faturamento: ");
		Double metaFaturamento = scanner.nextDouble();
		
		System.out.print("Faturamento da empresa: ");
		Double faturamentoDaEmpresa = scanner.nextDouble();
		
		System.out.print("M�dia Salarial: ");
		Double mediaSalarial = scanner.nextDouble();
		
		Double calculoOitentaPorCentoDaMeta = (faturamentoDaEmpresa * 100) / metaFaturamento;
		Double calculoOitetaPorCentoDaMediaSalarial = (mediaSalarial * BONUS) / 100;
				
		Boolean calculoDeFaturamento = faturamentoDaEmpresa >= metaFaturamento;
		Boolean calculoDeFaturamentoOitentaPorCento = (faturamentoDaEmpresa < metaFaturamento) && (calculoOitentaPorCentoDaMeta >= BONUS);
		
		if (calculoDeFaturamento) {
			System.out.println("Faturamento maior que meta, funcion�rios iram receber 1 sal�rio de b�nus: " + mediaSalarial);
		} else if (calculoDeFaturamentoOitentaPorCento) {
			System.out.println("Faturamento menor que meta e maior que 80% da meta, funcion�rios iram receber 80% de 1 sal�rio de b�nus: " + calculoOitetaPorCentoDaMediaSalarial);
		}
		
		scanner.close();
	}
}
