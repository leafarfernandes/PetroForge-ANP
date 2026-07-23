# ROADMAP — PetroForge-ANP

## Etapa 0 — Planejamento

- [x] Criar o repositório no GitHub
- [x] Configurar o ambiente virtual
- [x] Definir o objetivo e o escopo do projeto
- [x] Definir a estrutura inicial de pastas
- [x] Escolher as principais tecnologias
- [x] Criar os arquivos-base do repositório

## Versão 1 — Coleta, tratamento e análise exploratória

### Leitura e tratamento

- [x] Adicionar o arquivo CSV público da ANP
- [x] Implementar o carregamento dos dados com Pandas
- [x] Interpretar vírgula decimal e ponto de milhar
- [x] Padronizar os nomes das colunas
- [x] Converter a coluna `Mês/Ano` para `datetime`
- [x] Investigar valores ausentes
- [x] Investigar registros repetidos
- [x] Preservar valores ausentes com significado operacional
- [ ] Implementar download automático dos dados da ANP

### Análises de produção

- [x] Produção de óleo por estado
- [x] Produção de óleo por bacia
- [x] Produção de óleo por campo
- [x] Produção de óleo por poço
- [x] Produção mensal de óleo
- [x] Variação percentual mensal
- [x] Produção mensal de óleo e gás
- [x] Produção por estado e mês
- [x] Produção hierárquica por estado e campo
- [x] Calcular participação percentual sobre a produção total
- [x] Preservar categorias ausentes nos agrupamentos
- [x] Diferenciar produção zero de produção ausente

### Indicadores

- [x] Criar módulo de estatísticas gerais
- [x] Criar módulo de KPIs
- [x] Calcular produção total
- [x] Calcular produção média, máxima e mínima
- [x] Contabilizar estados produtores
- [x] Contabilizar bacias, campos e poços
- [x] Criar logger centralizado

## Versão 2 — Visualizações

- [x] Adotar Plotly como biblioteca de visualização
- [x] Criar módulo reutilizável de gráficos
- [x] Criar gráfico de produção mensal
- [x] Criar gráfico de produção por estado
- [x] Criar gráfico de produção por bacia
- [x] Criar gráfico dos principais campos
- [x] Criar gráfico dos principais poços
- [x] Criar comparação mensal entre óleo e gás
- [x] Criar heatmap de produção por estado e mês
- [x] Criar Treemap por estado e campo
- [ ] Revisar títulos, unidades e formatação dos gráficos
- [ ] Validar a interpretação técnica de cada visualização
- [ ] Integrar todos os gráficos ao dashboard

## Versão 3 — Dashboard Streamlit

- [x] Criar a estrutura inicial do dashboard
- [x] Configurar a página do Streamlit
- [x] Adicionar título e descrição do projeto
- [x] Integrar o pipeline de carregamento e limpeza
- [x] Criar cards de KPIs
- [x] Exibir produção total, poços, campos e estados
- [x] Registrar Plotly e Streamlit nas dependências
- [ ] Adicionar os gráficos Plotly
- [ ] Criar sidebar
- [ ] Adicionar filtro por estado
- [ ] Adicionar filtro por bacia
- [ ] Adicionar filtro por campo
- [ ] Adicionar filtro por período
- [ ] Atualizar KPIs e gráficos dinamicamente
- [ ] Tratar estados vazios dos filtros
- [ ] Refinar o layout e a hierarquia visual

## Versão 4 — Refinamento e publicação

- [ ] Adicionar cache para carregamento e processamento
- [ ] Revisar desempenho
- [ ] Adicionar testes automatizados
- [ ] Revisar type hints e docstrings
- [ ] Remover código e dependências não utilizados
- [ ] Atualizar o README
- [ ] Documentar a fonte e o período dos dados
- [ ] Documentar instalação e execução
- [ ] Adicionar capturas de tela ou GIF do dashboard
- [ ] Preencher e revisar a licença
- [ ] Preparar o projeto para deploy
- [ ] Publicar o dashboard
- [ ] Preparar a apresentação para LinkedIn e portfólio