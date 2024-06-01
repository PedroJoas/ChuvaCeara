BRONZE_DIR = data/bronze/txt
SILVER_DIR = data/silver/csv


.DEFAULT_GOAL := help

.PHONY: all
all: create_dirs
	@echo "Estrutura de diretórios criada."

.PHONY: create_dirs
create_dirs: $(BRONZE_DIR) $(SILVER_DIR)

$(BRONZE_DIR):
	mkdir -p $(BRONZE_DIR)

$(SILVER_DIR):
	mkdir -p $(SILVER_DIR)

.PHONY: clean
clean:
	rm -rf data/bronze data/silver
	@echo "Estrutura de diretórios removida."

.PHONY: help
help:
	@echo "Comandos disponíveis:"
	@echo "  all         - Cria a estrutura de diretórios (equivalente a 'create_dirs')"
	@echo "  create_dirs - Cria a estrutura de diretórios"
	@echo "  clean       - Remove a estrutura de diretórios"
	@echo "  help        - Mostra esta mensagem de ajuda"
