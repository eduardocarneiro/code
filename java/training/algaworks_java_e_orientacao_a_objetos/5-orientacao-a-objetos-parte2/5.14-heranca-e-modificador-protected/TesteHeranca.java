package lab.eoc.fjoo.heranca;

public class TesteHeranca {

	public static void main(String[] args) {
		
		Jogador j = new Jogador();
		j.nome = "Eduardo";
		j.idade = 38;
		
		System.out.println("O jogador " + j.nome + " tem " + j.idade + " anos");
		j.seApresentar();
		j.dizerSeAindaJoga();
		
	}

}
