$(function () {
        window.alert = function (message, type = 'red') {
            $.alert({title: 'Alert!', content: message, type: type});
        };
        window.confirmation = function (content = "", callback, title = "Confirmation", dialogType = "dark", btnClass = "btn-primary") {
            $.confirm({
                title: title,
                content: content,
                columnClass: 'col-md-5 col-md-offset-4',
                icon: 'fa fa-question-circle',
                type: dialogType,
                buttons: {
                    ok: {
                        text: "OK",
                        btnClass: btnClass,
                        keys: ['enter'],
                        action: callback
                    },
                    cancel: {
                        text: 'Annuler'
                    }
                }
            });
        };

        $('.delete').click(function (event) {
            event.preventDefault();
            const message = $(this).attr('title');
            const goto = $(this).attr('href');
            confirmation(message, function () {
                window.location.href = goto;
            })
        });
    }
);