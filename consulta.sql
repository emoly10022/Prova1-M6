
SELECT c.nome, p.nomeProduto, p.valorInvestimento, p.taxaRendimento
FROM usuario c
JOIN ProdutoFinanceiro p ON c.idCliente = p.idCliente
WHERE c.id_usuario = ? AND p.id_produto = ?;
