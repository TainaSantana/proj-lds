/*$('#exampleModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) // Botão que acionou o modal
    var recipient = button.data('whatever') // Extrai informação dos atributos data-*
    // Se necessário, você pode iniciar uma requisição AJAX aqui e, então, fazer a atualização em um callback.
    // Atualiza o conteúdo do modal. Nós vamos usar jQuery, aqui. No entanto, você poderia usar uma biblioteca de data binding ou outros métodos.
    var modal = $(this)
    modal.find('.modal-title').text('Enviar convites')
    modal.find('.modal-body input').val(recipient)
  })*/

  $( document ).ready(function() {

    
    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    
    $(deleteBtn).on('click', function(e) {

        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Quer deletar esta tarefa?');

        if(result) {
            window.location.href = delLink;
        }

    });

    $(searchBtn).on('click', function(e) {
        searchForm.submit();
    });
    

});