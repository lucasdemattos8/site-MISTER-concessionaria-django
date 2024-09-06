document.addEventListener("DOMContentLoaded", function() {
    const activeFilters = document.getElementById('active-filters');

    // Função para mostrar ou ocultar a seção de filtros ativos
    function toggleActiveFiltersDisplay() {
        const activeFiltersCount = activeFilters.querySelectorAll('.active-filter').length;

        if (activeFiltersCount === 0) {
            activeFilters.style.display = 'none';
        } else {
            activeFilters.style.display = 'block';
        }
    }

    toggleActiveFiltersDisplay(); // Chama inicialmente para configurar a exibição

    activeFilters.addEventListener('click', function(event) {
        if (event.target.classList.contains('remove-filter')) {
            const type = event.target.getAttribute('data-type');
            if (type === 'cor') {
                // Desmarca todos os botões de rádio com o nome 'cor'
                const radios = document.querySelectorAll(`input[name="cor"]`);
                radios.forEach(radio => {
                    radio.checked = false;
                });
            } else {
                const select = document.getElementById(type);
                if (select) {
                    select.value = 'todos'; // Define o valor padrão para nenhum filtro
                }
            }
            // Atualiza a exibição dos filtros ativos após remover um filtro
            toggleActiveFiltersDisplay();

            // Submete o formulário para atualizar a página
            document.getElementById('filter-form').submit();
        }
    });

    // Atualiza a visualização do filtro de ano após a mudança
    const anoSelect = document.getElementById('ano');
    anoSelect.addEventListener('change', function() {
        // Atualiza a exibição dos filtros ativos
        toggleActiveFiltersDisplay();
    });

    // Mantém o valor selecionado após submeter o formulário
    const filtroForm = document.getElementById('filter-form');
    filtroForm.addEventListener('submit', function() {
        // Atualiza a exibição dos filtros ativos
        toggleActiveFiltersDisplay();
    });
});
