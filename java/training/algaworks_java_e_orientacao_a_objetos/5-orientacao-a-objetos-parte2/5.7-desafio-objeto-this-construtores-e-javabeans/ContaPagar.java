package orientacaoAObjeto_parte2;

public class ContaPagar {
	
	private String descricao;
	private Double valor;
	private String dataVencimento;
	
	// Fornecedor 
	private Fornecedor fornecedor;
	
	// getters and setters
	public String getDescricao() {
		return descricao;
	}

	public void setDescricao(String descricao) {
		this.descricao = descricao;
	}

	public Double getValor() {
		return valor;
	}

	public void setValor(Double valor) {
		this.valor = valor;
	}

	public String getDataVencimento() {
		return dataVencimento;
	}

	public void setDataVencimento(String dataVencimento) {
		this.dataVencimento = dataVencimento;
	}

	public Fornecedor getFornecedor() {
		return this.fornecedor;
	}

	public void setFornecedor(Fornecedor fornecedor) {
		this.fornecedor = fornecedor;
	}

	// constructor default
	ContaPagar() {
		
	}
	
	// constructor ContaPagar
	ContaPagar(Fornecedor fornecedor, String descricao, Double valor, String dataVencimento) {
		this.fornecedor = fornecedor;
		this.descricao = descricao;
		this.valor = valor;
		this.dataVencimento = dataVencimento;
	}

	// method pagar
	public void pagar() {
		System.out.println("Pagando conta " + this.getDescricao() + " no valor de " 
			+ this.getValor() + " e vencimento em " + this.getDataVencimento() 
			+ " do fornecedor " + this.getFornecedor().getNome() + ".");
	}
}
