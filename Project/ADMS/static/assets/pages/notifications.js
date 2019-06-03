
$(document).ready(function() {
	"use strict";


	$('.notification-info').on('click',function(e){
	    $.toast().reset('all'); 
		$("body").removeAttr('class');
		$.toast({
            heading: 'simply dummy text',
            text: 'Lorem Ipsum is simply dummy text of the printing and typesetting ',
            position: 'top-right',
            loaderBg:'#FFBD4A',
            icon: 'info',
            hideAfter: 3000, 
            stack: 6
        });
		return false;
    });

	$('.notification-warning').on('click',function(e){
        $.toast().reset('all');
		$("body").removeAttr('class');
		$.toast({
           heading: 'simply dummy text',
            text: 'Lorem Ipsum is simply dummy text of the printing and typesetting ',
            position: 'top-right',
            loaderBg:'#FFBD4A',
            icon: 'warning',
            hideAfter: 3500, 
            stack: 6
        });
		return false;
	});
	
	$('.notification-success').on('click',function(e){
        $.toast().reset('all');
		$("body").removeAttr('class');
		$.toast({
            heading: 'simply dummy text',
            text: 'Lorem Ipsum is simply dummy text of the printing and typesetting ',
            position: 'top-right',
            loaderBg:'#FFBD4A',
            icon: 'success',
            hideAfter: 3500, 
            stack: 6
          });
		return false;  
	});

	$('.notification-danger').on('click',function(e){
		$.toast().reset('all');
		$("body").removeAttr('class');
		$.toast({
            heading: 'simply dummy text',
            text: 'Lorem Ipsum is simply dummy text of the printing and typesetting ',
            position: 'top-right',
            loaderBg:'#FFBD4A',
            icon: 'error',
            hideAfter: 3500
        });
		return false;
    });
	
	$('.notification-tleft').on('click',function(e){
	    $.toast().reset('all');   
		$("body").removeAttr('class');
		$.toast({
            heading: 'top left',
            text: 'Lorem Ipsum is simply dummy text of the printing and typesetting ',
            position: 'top-left',
            loaderBg:'#FFBD4A',
            icon: 'error',
            hideAfter: 3500
        });
		return false;
    });
	
	$('.notification-tright').on('click',function(e){
		$.toast().reset('all');
		$("body").removeAttr('class');
		$.toast({
            heading: 'top right',
            text: 'Lorem Ipsum is simply dummy text of the printing and typesetting ',
            position: 'top-right',
            loaderBg:'#FFBD4A',
            icon: 'error',
            hideAfter: 3500
        });
		return false;
    });
	
	$('.notification-bleft').on('click',function(e){
		$.toast().reset('all');
		$("body").removeAttr('class');
		$.toast({
            heading: 'bottom left',
            text: 'Lorem Ipsum is simply dummy text of the printing and typesetting ',
            position: 'bottom-left',
            loaderBg:'#FFBD4A',
            icon: 'error',
            hideAfter: 3500
        });
		return false;
    });
	
	$('.notification-bright').on('click',function(e){
	    $.toast().reset('all');   
		$("body").removeAttr('class');
		$.toast({
            heading: 'bottom right',
            text: 'Lorem Ipsum is simply dummy text of the printing and typesetting ',
            position: 'bottom-right',
            loaderBg:'#FFBD4A',
            icon: 'error',
            hideAfter: 3500
        });
		return false;
	});
	
	$('.notification-tfull').on('click',function(e){
	    $.toast().reset('all');   
		$("body").removeAttr('class').removeClass("bottom-center-fullwidth").addClass("top-center-fullwidth");
		$.toast({
            heading: 'top center',
            text: 'Lorem Ipsum is simply dummy text of the printing and typesetting ',
            position: 'top-center',
            loaderBg:'#FFBD4A',
            icon: 'error',
            hideAfter: 3500
        });
		return false;
	});
	
	$('.notification-btfull').on('click',function(e){
	    $.toast().reset('all');
		$("body").removeAttr('class').addClass("bottom-center-fullwidth");
		$.toast({
            heading: 'bottom right',
            text: 'Lorem Ipsum is simply dummy text of the printing and typesetting ',
            position: 'bottom-center',
            loaderBg:'#FFBD4A',
            icon: 'error',
            hideAfter: 3500
        });
		return false;
	});
});
          
