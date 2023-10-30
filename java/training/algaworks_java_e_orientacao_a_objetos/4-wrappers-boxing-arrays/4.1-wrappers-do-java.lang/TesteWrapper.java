
public class TesteWrapper {

	public static void main(String[] args) {
		// byte, short, int,     long, float, double e char (tipos primitivos)
		// Byte, Short, Integer, Long, Float, Double e Character (classe wrappers)
		
		int x = 5;
		Integer i = new Integer(5);
		
		byte y = i.byteValue();
		// xxxValue();
		
		String valor = "15.5";
		Float v = new Float(valor);
		System.out.println(v + 3);
		
		int idade = Integer.parseInt("34"); //parseXXX
		System.out.println("Daqui a 5 anos voc� ter�: " + (idade + 5) + " anos.");
		
		try { 
			double custo = Double.parseDouble("10 reais");
			System.out.println("Custo total: " + custo);
		} catch (NumberFormatException e) {
			System.err.println("numero invalido");
		}
	}
}
