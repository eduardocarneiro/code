
public class FolhaDePagamento {

	// Assinatura do m�todo;
	// quando vc tem um m�todo que passa-se argumentos, vc pode dizer que a assinatura do m�todo �:
	// double calcularSalario(int, int, double, double)
	// }

	double calularSalario (int horasNormal, int horasExtra, double valorHoraNormal, double valorHoraExtra) {
		
		double valorHorasNormais = horasNormal * valorHoraNormal;
		double valorHorasExtras = horasExtra * valorHoraExtra;
			
		return valorHorasNormais + valorHorasExtras;
		
		}
	
	}