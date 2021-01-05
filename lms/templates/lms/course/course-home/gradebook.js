(function(fn) {
    'use strict';
    fn(window.jQuery, window, document);
}(function($, window, document) {
    'use strict';

    $(function() {
        $('.sort-btn').on('click', '[data-sort]', function(event) {
            event.preventDefault();

            var $this = $(this),
                sortDir = 'desc';

            if ($this.data('sort') !== 'asc') {
                sortDir = 'asc';
            }

            $this.data('sort', sortDir).find('.fa').attr('class', 'fa fa-sort-' + sortDir);

            // call sortDesc() or sortAsc() or whathaveyou...
        });
    });
}));

// window.onscroll = function() {scrollFunction()};

// function scrollFunction() {
//   if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
//     document.getElementById("navbar").style.top = "0";
//   } else {
//     document.getElementById("navbar").style.top = "-50px";
//   }
// }