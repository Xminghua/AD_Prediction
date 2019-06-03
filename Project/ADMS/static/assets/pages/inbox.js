$( document ).ready(function() {
    
    $('.check-mail-all').click(function () {
        $('.checkbox-mail').click();
    });
    
    $('.checkbox-mail').each(function() {
        $(this).click(function() {
            if($(this).closest('tr').hasClass("checked")){
                $(this).closest('tr').removeClass('checked');
                hiddenMailOptions();
            } else {
                $(this).closest('tr').addClass('checked');
                hiddenMailOptions();
            }
        });
    });
    
    $('.mailbox-content table tr td').not(":first-child").on('click', function(e) {
        e.stopPropagation();
        e.preventDefault();

        window.location = "message-view.html";
    });
});
