package orientacaoAObjeto_parte2;

public class TesteEncapsulamento {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Arcondicionado ar = new Arcondicionado(); // 17 - 25
		
		ar.trocarTemperatura(21);
		System.out.println("Temperatura do ar: " + ar.obterTemperatura() + "º");
		
		ar.trocarTemperatura(10);
		System.out.println("Temperatura do ar: " + ar.obterTemperatura() + "º");
		
		
	}

}
