
public class EstruturaIf01 {

	public static void main(String[] args) {
		
		Boolean movimentaMetadoDoValorDoEmprestimo = true;
		Boolean aContaTemTempoSuficienteDeAbertura = true;
		Boolean temNomeLimpoNoSPC = true;
		
		Boolean liberarEmprestimo = movimentaMetadoDoValorDoEmprestimo && aContaTemTempoSuficienteDeAbertura && temNomeLimpoNoSPC;
		
		if (!liberarEmprestimo) {
			System.out.println("Pode liberar o empr�stimo.");
		} else {
			System.out.println("N�o pode liberar o empr�stimo.");
		}
		
		// invertendo o de true para false (!liberarEmprestimo)
//		if (!liberarEmprestimo) {
//			System.out.println("Pode liberar o empr�stimo.");
//		} else {
//			System.out.println("N�o pode liberar o empr�stimo.");
//		}
	}
}
