package lab.eoc.fjoo.animal;

public class Cachorro {

	private String nome;

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}
	
	// modificador de acesso default do method, adicionar 'public'
	public void sentar() {
		System.out.println("Eu " + nome + ", vou sentar.");
	}
}
