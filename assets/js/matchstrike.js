$(document).ready(function(){
	var news = [];
	$.getJSON("/more_news/"+$(".items li:last").attr('id').split('time')[1]+"/", function(data){
		news = data.news;
		append_news(news, 3);
	});
	$(".items").each(function(i) {
		$(this).replaceWith("<div class='scrollable'><div class='items'>" + this.innerHTML + "</div></div>");
	});
	fix_lis_for_scrollable();
	var scroll_api = $("div.scrollable").scrollable({
			onBeforeSeek: function(){
				append_news(news, 3);				
			},
			size: 3,
			keyboard:false,
			api:true,
			clickable: false
	});
	
	$('.atlibs').cycle({ 
	    fx:     'fade', 
	    speed:  'fast', 
	    timeout: 0, 
	    pager:  '#atlibs_nav', 
	    pagerAnchorBuilder: function(idx, slide) { 
		// return selector string for existing anchor 
		return '#atlibs_nav li:eq(' + idx + ') a'; 
	    } 
	});
	
	$('.hootcourse').cycle({ 
	    fx:     'fade', 
	    speed:  'fast', 
	    timeout: 0, 
	    pager:  '#hootcourse_nav', 
	    pagerAnchorBuilder: function(idx, slide) { 
		// return selector string for existing anchor 
		return '#hootcourse_nav li:eq(' + idx + ') a'; 
	    } 
	});
	
	$('.happo').cycle({ 
	    fx:     'fade', 
	    speed:  'fast', 
	    timeout: 0, 
	    pager:  '#happo_nav', 
	    pagerAnchorBuilder: function(idx, slide) { 
		// return selector string for existing anchor 
		return '#happo_nav li:eq(' + idx + ') a'; 
	    } 
	});

	$('.ppm').cycle({ 
	    fx:     'fade', 
	    speed:  'fast', 
	    timeout: 0, 
	    pager:  '#ppm_nav', 
	    pagerAnchorBuilder: function(idx, slide) { 
		// return selector string for existing anchor 
		return '#ppm_nav li:eq(' + idx + ') a'; 
	    } 
	});
	
	$.ga("UA-10208886-2");
});

function fix_lis_for_scrollable() {
	$(".items li").each(function(i) {
		$(this).replaceWith("<div class='" + $(this).attr('class')+ "'>" + this.innerHTML + "</div>");
	});
}

function append_news(list, amount) {
	var cnt = 0;
	while (cnt < amount) {
		$('.items').append(list.shift());
		cnt++;
	}
	fix_lis_for_scrollable();
	try {
		$('#related_content').supersleight();
	} catch(err) {
		
	}
}