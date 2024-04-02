package orientacaoAObjeto_parte2;

public class TesteJavaBean {

	public static void main(String[] args) {
		
		PessoaBean pessoa = new PessoaBean();
		
		pessoa.setNome("Sarah");
		pessoa.setIdade(5);
		
		System.out.println(pessoa.getNome() + " tem " + pessoa.getIdade() + " anos.");
	}

}
