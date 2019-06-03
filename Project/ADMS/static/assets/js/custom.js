$(document).ready(function() {

        //tooltip
        $(function() {
            $('[data-toggle="tooltip"]').tooltip()
        })

        // Initialize Popovers
        jQuery('[data-toggle="popover"], .js-popover').popover({
            container: 'body',
            animation: true,
            trigger: 'hover'
        });

    });

   
