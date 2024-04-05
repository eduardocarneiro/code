package lab.eoc.fjoo.sobreposicao;

import java.util.Date;

public class ProdutoPerecivel extends Produto {

	protected Date dataValidade;
	
	public void identificar() {
		super.identificar();
		System.out.println("Minha de data de validade é: " + dataValidade);
	}
	
}
