package lab.eoc.fjoo.heranca;

public class Pessoa {

	// public, protected pode ser acessado na herança
	protected String nome;
	protected int idade;
	
	public void seApresentar() {
		
		System.out.println("Olá, eu sou o " + nome + ", e tenho " + idade + " anos!!!");
	}
 }
