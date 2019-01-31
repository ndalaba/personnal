jQuery(document).ready(function ($) {
    
    window.loadEditModal=function(event){
        event.preventDefault();
        var url= event.target.dataset.url;
        $.get(url, function (response) {
            $('#addMailForm').modal('show')
            $('#addMailForm .modal-body').html(response);
        });
    };

    $('#actionButton').click(function (e) {
        e.preventDefault();
        var url = $(this).data('url');
        $.get(url, function (response) {
            $('#addMailForm .modal-body').html(response);
        });
    });
});