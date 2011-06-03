(function($){
    $(document).ready(function(){
        $('ul.blog-archive ul.months').hide();
        $('ul.blog-archive ul.posts').hide();
        $('ul.blog-archive li.year a').click(function(){
            var months = $(this).parent().find('ul.months');
            months.toggle();
            if (months.is(':visible')) {
                $(this).parent().addClass('expanded');
            } else {
                $(this).parent().removeClass('expanded');
            }
            return false;
        });
        $('ul.blog-archive li.month a').click(function(){
            var posts = $(this).parent().find('ul.posts')
            posts.toggle();
            if (posts.is(':visible')) {
                $(this).parent().addClass('expanded');
            } else {
                $(this).parent().removeClass('expanded');
            }
            return false;
        });
    });
})(jQuery);
