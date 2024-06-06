# Cadastro de Usuário

## Dados do Usuário
- [ ] **Nome:** Completo, com no mínimo duas palavras.
- [ ] **Email:** Endereço de e-mail válido.
- [ ] **Senha:** Deve seguir os critérios de segurança detalhados abaixo.
- [ ] **CPF ou CNPJ:** Documento válido conforme o tipo de usuário (pessoa física ou jurídica).
- [ ] **Sexo:** Genero do usuario.
- [ ] **Data de Nascimento:** Formato DD/MM/AAAA.
- [ ] **WhatsApp:** Número de telefone com código de país.
- [ ] **Data de Cadastro:** Data automática do registro do usuário.
- [ ] **Foto de Perfil:** Anexo da imagem
- [ ] **Status:** Situação do Usuário
- [ ] **Data do Ultimo Login:** Data automática da última sessão iniciada pelo usuário.

## Validações

### Nome
- [ ] **Tamanho Mínimo:** O nome deve ter no mínimo 8 caracteres.
- [ ] **Quantidade de Palavras:** O nome deve conter pelo menos 2 palavras.

### Email
- [ ] **Formato Válido:** O email deve seguir um formato válido (ex: usuario@dominio.com).
- [ ] **Unico:** Não pode ter emails repetidos.

### Senha
- [ ] **Tamanho Mínimo:** A senha deve ter no mínimo 8 caracteres.
- [ ] **Complexidade:** Deve conter ao menos uma letra maiúscula, uma minúscula, um número e um caractere especial.
- [ ] **Validação Adicional:** Não deve conter sequências comuns ou repetições (ex: 1234, abcd, 1111).
- [ ] **Criptografia:** A senha deve ser encriptografa antes de ser gravada no banco.

### CPF/CNPJ
- [ ] **Validação:** O documento deve ser validado para garantir que é um número registrado e válido.

### WhatsApp
- [ ] **Formato Válido:** O número deve incluir código de país e área, e ser válido para WhatsApp.

### Sexo
- [ ] **Opções Válidas:** Deve ser uma das opções pré-definidas (Masculino, Feminino, Outro).

### Data de Nascimento
- [ ] **Formato Válido:** A data deve estar no formato correto (DD/MM/AAAA).

### Data de Cadastro
- [ ] **Automação:** A data deve ser automaticamente configurada para a data atual no momento do cadastro.

### Status
- [ ] **Automação:** Deverá ser ativo na efetivação do cadastro, inativa por tempo de 60 dias desde o ultimo login, suspensa por qualquer violação das regras.

### Foto de Perfil
- [ ] **Formato:** Foto deverá ser nos formatos: jpg/jpeg/png/webP.
- [ ] **Redimensionamento:** Deixer a imagem com 256x256 pixels.
- [ ] **Compressão da Imagem:** Compressão de 75% da imagem.

### Data do Último Login
- [ ] **Automação:** A data deve ser automaticamente atualizada para a data atual cada vez que o usuário iniciar uma sessão.
